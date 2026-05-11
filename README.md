# 🚀 NexusFlow: Local AI Knowledge Architect

NexusFlow is a production-grade, privacy-first Retrieval-Augmented Generation (RAG) engine. It transforms fragmented engineering notes, messy transcripts, and corporate PDFs into structured, actionable Standard Operating Procedures (SOPs) and Onboarding Guides.

**Built for the "Zero-Trust" Enterprise:** 100% of processing happens locally on your hardware. No data ever leaves your drive.

---

## 🏗️ System Architecture
NexusFlow uses a modular architecture designed to bypass hardware limitations through intelligent memory management.



### 🧩 Core Components
* **Ingestion Engine:** Handles multi-format extraction (PDF, DOCX, TXT).
* **Vector Brain:** Powered by **ChromaDB** and `all-MiniLM-L6-v2` embeddings for semantic search.
* **Generation Core:** Orchestrated via **LangChain** using **Llama 3.2 (1B)** for high-speed, low-RAM inference.
* **Memory Manager:** Implements a "Search and Destroy" pattern, clearing the embedding model from RAM before spinning up the LLM to prevent system crashes on limited hardware.

---

## 📸 Workflow & Interface
The system features a **Streamlit** Command Center for seamless interaction.

### 1. Ingestion Phase
Drop files into `/data/uploads`. The system verifies the folder structure and indexes content into the persistent vector store located in your project root.

### 2. Generation Phase
Select between **SOP Mode** (for technical processes) or **Onboarding Mode** (for new hire guides).

---

## 🛠️ Setup Guide

### Prerequisites
* **Python 3.10+**
* **Ollama** installed and running.
* **Hardware:** Minimum 4GB RAM (optimized for 1.6GiB available RAM environments).

### Installation
1. **Clone the repository to your drive:**
   ```powershell
   git clone [https://github.com/hamnaasif090-coder/nexus-flow.git](https://github.com/hamnaasif090-coder/nexus-flow.git)
   cd nexus-flow

2. **Initialize Virtual Environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate

3. **Install Production Dependencies:**
   ```powershell
   pip install langchain-ollama langchain-huggingface langchain-chroma streamlit pypdf python-docx
   
4. **Pull the Local Model:**

Download the optimized local LLM used by NexusFlow for document synthesis and response generation.
   ```powershell
   ollama pull llama3.2:1b
   ```

5. **Launch the UI:**

Start the Streamlit interface to access the ingestion and generation workflow.

  ```powershell
  streamlit run interface.py
  ```

Once launched, the UI becomes available locally in your browser.

---


# 🔄 System Flow

NexusFlow follows a Retrieval-Augmented Generation (RAG) pipeline optimized for low-resource environments.

### 1. Upload Phase
Place your source documentation inside the uploads directory.

```plaintext
/data/uploads/engineering_handbook.pdf
```

Supported formats include:

* PDF
* DOCX
* TXT

The ingestion engine automatically detects and processes new files.

---

### 2. Synchronization & Vectorization
The `IngestEngine` extracts raw text, performs intelligent chunking, and generates embeddings for semantic retrieval.

#### Processing Pipeline
```python
# Extract document text
# Split content using RecursiveCharacterTextSplitter
# Generate embeddings via all-MiniLM-L6-v2
# Store vectors in persistent ChromaDB
```

This creates a searchable knowledge base stored locally on disk.

---

### 3. User Query Phase
Users interact with the system through natural language prompts.

#### Example Request
```text
"Generate an onboarding guide for junior developers"
```

The system supports:

* SOP generation
* Technical onboarding
* Process documentation
* Knowledge summarization

---

### 4. Semantic Retrieval
The `VectorBrain` performs similarity search against the vector database to retrieve the most contextually relevant knowledge fragments.

```python
results = vector_store.similarity_search(query)
```

This ensures the LLM only receives highly relevant context, reducing hallucinations and improving output quality.

---

### 5. AI Draft Generation
Using the retrieved context, **Llama 3.2 (1B)** synthesizes a structured Markdown document tailored to the selected workflow mode.

#### Output Location
```plaintext
/data/generated/onboarding/
```

Generated documents are automatically saved locally for further review and editing.

---

# ✍️ Prompt Engineering Framework

NexusFlow uses specialized system prompts to guide document generation based on the selected workflow.

### SOP Generation Template
Designed for operational workflows, technical procedures, and standardized documentation.

```text
"You are a Professional Operations Architect. Your goal is to transform messy, unstructured notes into a high-quality Standard Operating Procedure (SOP)."
```

---

### Onboarding Generation Template
Optimized for creating beginner-friendly employee onboarding guides.

```text
"You are a Senior Team Lead. Transform the following messy process notes into a welcoming, easy-to-follow guide for a new employee."
```

---

# 🚀 Future Improvements

### Multi-Agent Review Pipeline
Introduce a secondary LLM validation layer to review generated outputs for:

* factual accuracy
* formatting consistency
* procedural safety
* hallucination reduction

```python
# Secondary AI validation pipeline
# Automated quality assurance pass
```

---

### OCR & Diagram Understanding
Extend ingestion capabilities using Optical Character Recognition (OCR) for extracting insights from diagrams, screenshots, and scanned PDFs.

```python
# OCR pipeline for embedded images and diagrams
```

---

### Automated Slack Delivery
Enable direct integration with Slack for automated publishing of generated Markdown files.

```python
# Send generated SOPs directly to Slack channels
```

---

### Dynamic Quantization Scaling
Allow intelligent model switching based on available hardware resources.

```python
# Dynamic model selection
# llama3.2:1b  -> Low RAM systems
# llama3:8b    -> High VRAM systems
```

---

# 🛠️ Technology Stack

NexusFlow is built using a fully local AI stack optimized for privacy and lightweight deployment.

```text
Python
LangChain
Ollama
ChromaDB
Streamlit
HuggingFace Embeddings
Llama 3.2 (1B)
```

---

# 📁 Project Structure

```plaintext
nexus-flow/
│
├── interface.py                 # Streamlit command center UI
├── main.py                      # Main application entry point
├── requirements.txt             # Python dependencies
│
├── app/
│   │
│   ├── config.py                # Global configuration settings
│   │
│   ├── core/
│   │   │
│   │   ├── generator.py         # LLM generation pipeline
│   │   ├── ingest.py            # Document ingestion & chunking
│   │   ├── vector_store.py      # ChromaDB semantic retrieval engine
│   │   │
│   │   └── __pycache__/         # Python cache files
│   │
│   ├── utils/
│   │   │
│   │   ├── file_handler.py      # File validation & handling utilities
│   │   │
│   │   └── __pycache__/
│   │
│   └── __pycache__/
│
├── data/
│   │
│   ├── docs/
│   │   │
│   │   ├── engineering_handbook.pdf
│   │   ├── meeting_notes.txt
│   │   │
│   │   └── chroma_db/           # Persistent Chroma vector database
│   │
│   ├── generated/
│   │   │
│   │   └── onboarding/          # AI-generated onboarding guides
│   │
│   ├── sops/                    # Generated SOP documents
│   │
│   └── uploads/                 # User-uploaded source documents
│
└── prompts/
    │
    ├── onboarding_template.md   # Onboarding system prompt
    └── sop_template.md          # SOP generation system prompt
```
