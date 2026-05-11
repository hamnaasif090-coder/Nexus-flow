import os
from pathlib import Path

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Folder Structure
PATHS = {
    "uploads": BASE_DIR / "data/uploads",
    "docs": BASE_DIR / "data/docs",
    "sops": BASE_DIR / "data/sops",
    "generated": BASE_DIR / "data/generated",
    "templates": BASE_DIR / "prompts",
    "onboarding": BASE_DIR / "data/generated/onboarding", # Add this line!
}

# Model Settings (Local via Ollama)
LLM_MODEL = "llama3" 
EMBED_MODEL = "all-MiniLM-L6-v2" # Runs locally on CPU/GPU

# Ensure directories exist
for path in PATHS.values():
    path.mkdir(parents=True, exist_ok=True)