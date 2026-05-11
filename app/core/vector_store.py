import chromadb
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from app.config import PATHS, EMBED_MODEL

class VectorBrain:
    def __init__(self):
        # Using the updated langchain-huggingface class
        # model_kwargs helps ensure it runs on CPU correctly without memory spikes
        self.embeddings = HuggingFaceEmbeddings(
            model_name=EMBED_MODEL,
            model_kwargs={'device': 'cpu'} 
        )
        self.db_path = str(PATHS["docs"] / "chroma_db")
        
        self.vector_db = Chroma(
            persist_directory=self.db_path,
            embedding_function=self.embeddings,
            collection_name="nexusflow_kb"
        )

    def process_and_add_document(self, text: str, metadata: dict):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500, # Smaller chunks to save memory during processing
            chunk_overlap=50,
            length_function=len
        )
        chunks = text_splitter.split_text(text)
        
        self.vector_db.add_texts(texts=chunks, metadatas=[metadata] * len(chunks))
        print(f"✅ Indexed {len(chunks)} chunks into the Knowledge Base.")

    def search_context(self, query: str, k=3):
        results = self.vector_db.similarity_search(query, k=k)
        return "\n\n".join([doc.page_content for doc in results])