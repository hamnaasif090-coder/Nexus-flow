from langchain_ollama import OllamaLLM
from app.core.vector_store import VectorBrain
from app.utils.file_handler import FileHandler
from app.config import PATHS
import gc
import os

class SOPGenerator:
    def __init__(self):
        self.handler = FileHandler()

    def generate_sop(self, topic_query, template_name="sop_template.md", category="sops"):
        """
        Generates content based on a topic, a specific template, and saves to a category folder.
        """
        print(f"🔍 Searching local knowledge for: {topic_query}...")
        
        # Step A: Search and Destroy (to save RAM)
        brain = VectorBrain()
        context = brain.search_context(topic_query)
        del brain 
        gc.collect() 
        
        print(f"✍️ Brain cleared. Loading Llama3.2:1b...")
        
        # Step B: Load the LLM
        llm = OllamaLLM(model="llama3.2:1b")
        
        # Step C: Dynamic Template Loading
        t_path = PATHS["templates"] / template_name
        
        if t_path.exists():
            print(f"📂 Loading template: {t_path}")
            with open(t_path, "r", encoding="utf-8") as file_in:
                sop_template = file_in.read()
        else:
            print(f"⚠️ Template '{template_name}' not found. Using fallback.")
            sop_template = "Context: {context}\n\nTask: Generate documentation for {user_input}"
        
        # Step D: Formatting and Execution
        final_prompt = sop_template.format(context=context, user_input=topic_query)
        
        try:
            print("🤖 LLM is processing...")
            response = llm.invoke(final_prompt)
            
            # Save result using the dynamic category (e.g., 'sops' or 'onboarding')
            out_path = self.handler.write_markdown(response, topic_query, category=category)
            print(f"\n✨ SUCCESS! Content generated.")
            print(f"📂 Saved to: {out_path}")
            return response
        except Exception as e:
            print(f"❌ Generation failed: {e}")
            return f"Error: {e}"

if __name__ == "__main__":
    gen = SOPGenerator()
    # Test call
    gen.generate_sop("Test Process", template_name="sop_template.md", category="sops")