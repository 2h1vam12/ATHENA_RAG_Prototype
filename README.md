# ATHENA RAG PROTOTYPE

> Retrieval-Augmented Generation Pipeline for the Adaptive Tutor Platform – CU Denver CSCI 4738 (Fall 2025)

##  Overview

**ATHENA** (Adaptive Tutoring Hub Empowered by Neural Agents) is our project and I am making the Retrieval-Augmented Generation (RAG) system designed to serve as the backend intelligence for our AI tutoring platform. This local prototype is the first stage of our personalized learning assistant and supports context-aware question answering over instructor-uploaded course materials.

This repo is maintained by **Shivam Pathak** for the **RAG subcomponent** of the CSCI 4738 Senior Design project.

---

## Current Goal

> **Phase 1 (Aug 30 – Sept 6, 2025):**  
> Set up core tech stack, embed sample documents, and run basic local retrieval queries using ChromaDB and sentence-transformers.

---

## Tech Stack

| Layer           | Tool/Library                              |
|----------------|--------------------------------------------|
| Embedding       | `sentence-transformers` (`all-MiniLM-L6-v2`) |
| Vector Store    | `ChromaDB` (local persistent DB)           |
| Text Processing | `LangChain` (document loaders, splitters)  |
| PDF Support     | `PyMuPDF` via LangChain's `PyMuPDFLoader`  |
| Language Model  | Initially external (GPT-4/Claude), later optional local |
| Interface (TBD) | CLI or Streamlit/Gradio for demo UI       |

---

## Project Structure

```bash
ATHENA-RAG-PROTOTYPE/
├── data/                  # Sample course files (.txt, .pdf)
├── rag_index/             # Persisted ChromaDB index
├── main.py                # Current prototype script
├── requirements.txt       # Python dependencies
└── README.md              # This file

##  Running the Prototype

### 1. Install dependencies

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Add test content

Place a `.txt` or a `.pdf` file in the `data/` folder. For now, you can use instructor notes, syllabus content, or cognitive debt readings.

### 3. Run the prototype

```bash
python main.py
```

---

##  Roadmap

| Date Range        | Milestone                                   |
| ----------------- | ------------------------------------------- |
| Aug 30 – Sept 6   | Tech stack setup, embedding sample files    |
| Sept 7 – Sept 20  | End-to-end query → retrieve → respond loop  |
| Sept 21 – Sept 30 | Prompt similarity + chunk selection tuning  |
| Oct 1 – Oct 12    | Course/context separation + filtering logic |
| Oct 13 – Oct 24   | Polish + integrate with frontend/backend    |

---

##  References

* [NVIDIA RAG Pipeline Blueprint](https://build.nvidia.com/nvidia/build-an-enterprise-rag-pipeline)
* [LangChain RAG Use Case](https://docs.langchain.com/docs/use-cases/question-answering/)
* [ChromaDB Docs](https://docs.trychroma.com/getting-started)
* [What is RAG? (NVIDIA Blog)](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)
* [Model Context Protocol](https://modelcontextprotocol.io/docs/learn/server-concepts)
* [Your Brain on ChatGPT (Cognitive Debt)](https://arxiv.org/abs/2505.02581)


##  About the Author

**Shivam Pathak**
Systems Engineer Intern @ Visa | CU Denver ‘26
Lead – Retrieval-Augmented Generation
[LinkedIn](https://www.linkedin.com/in/shivampathak04)


##  Disclaimer

This repo is a work-in-progress prototype for a student-led senior design project and is not yet production-ready. All content and code are subject to rapid iteration.

```
