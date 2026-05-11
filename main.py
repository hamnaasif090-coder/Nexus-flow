import sys
from app.config import PATHS
from app.utils.file_handler import FileHandler

def initialize_system():
    """
    Ensures the local environment is prepped and the 
    folder-based database is ready.
    """
    print("🚀 NexusFlow AI Architect: Initializing...")
    
    try:
        # Check if directories exist (created via config.py)
        for name, path in PATHS.items():
            if path.exists():
                print(f"✅ Folder Verified: {name}")
            else:
                path.mkdir(parents=True, exist_ok=True)
                print(f"📁 Folder Created: {name}")
        
        print("\n--- System Status: Online ---")
        print("📍 Drop raw notes in: ./data/uploads")
        print("📍 SOPs will appear in: ./data/sops")
        
    except Exception as e:
        print(f"❌ Initialization failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    initialize_system()