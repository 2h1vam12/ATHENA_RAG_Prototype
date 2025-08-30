# main.py
# Author: Shivam Pathak
# DESC: Local RAG prototype with dynamic PDF/TXT loading + PDF deduplication + warning fixes

# ------------------------- IMPORTS -------------------------
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
embedding_fn = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

import os

# ------------------------- FILE CONFIG -------------------------
file_path = "data/CSCI-4931-DL-syllabus-Fall2025-UGrad.pdf"  # You can change this to .txt as needed

# ------------------------- DYNAMIC LOADING -------------------------
if file_path.endswith(".pdf"):
    loader = PyMuPDFLoader(file_path)
elif file_path.endswith(".txt"):
    loader = TextLoader(file_path)
else:
    raise ValueError("Unsupported file format. Please use .txt or .pdf")

docs = loader.load()

# ------------------------- TEXT SPLITTING -------------------------
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

if not chunks:
    raise ValueError("No text found in the document. Try a different file.")

# ------------------------- EMBEDDING + STORAGE -------------------------
# Optionally swap for updated HuggingFaceEmbeddings if you want to remove LangChainDeprecationWarning
embedding_fn = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
# from langchain_huggingface import HuggingFaceEmbeddings
# embedding_fn = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = Chroma.from_documents(chunks, embedding_fn, persist_directory="rag_index")

# ------------------------- RETRIEVAL LOOP -------------------------
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})  # Change k=5 to whatever top-K results you want

while True:
    query = input("\nAsk something (or 'q' to quit): ")
    if query.lower() == "q":
        break

    #  Updated to avoid LangChain deprecation warning
    results = retriever.invoke(query)

    print("\nTop Results:\n")
    #  Deduplicate results based on content
    seen = set()
    for i, doc in enumerate(results):
        if doc.page_content not in seen:
            seen.add(doc.page_content)
            print(f"{len(seen)}. {doc.page_content}\n")
