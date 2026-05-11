from pathlib import Path
from pypdf import PdfReader
from docx import Document
from app.utils.file_handler import FileHandler
from app.core.vector_store import VectorBrain
from app.config import PATHS

class IngestEngine:
    def __init__(self):
        self.brain = VectorBrain()
        self.handler = FileHandler()

    def extract_text(self, file_path):
        suffix = file_path.suffix.lower()
        
        if suffix == '.txt':
            return self.handler.read_file(file_path)
        
        elif suffix == '.pdf':
            reader = PdfReader(file_path)
            return " ".join([page.extract_text() for page in reader.pages])
        
        elif suffix == '.docx':
            doc = Document(file_path)
            return " ".join([para.text for para in doc.paragraphs])
        
        return None

    def run(self):
        files = list(PATHS["uploads"].glob("*.*"))
        if not files:
            print("📭 No new files in /uploads.")
            return

        for file_path in files:
            print(f"📂 Extracting: {file_path.name}...")
            text = self.extract_text(file_path)
            
            if text:
                self.brain.process_and_add_document(text, {"source": file_path.name})
                self.handler.move_to_processed(file_path)
                print(f"✅ Indexed {file_path.name}")

if __name__ == "__main__":
    IngestEngine().run()