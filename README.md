# Enterprise RAG Assistant

An enterprise-grade Retrieval Augmented Generation (RAG) system that enables intelligent question answering over internal documents using Large Language Models.

This project demonstrates how to build a scalable AI assistant that retrieves relevant information from enterprise documents and generates accurate responses using LLMs.

---

## Project Overview

Traditional LLMs often hallucinate or lack domain-specific knowledge.  
This project solves that problem by implementing **Retrieval Augmented Generation (RAG)**.

The system retrieves relevant document chunks from a **vector database** and provides them as context to the LLM to generate accurate answers.

---

## Architecture

User Question  
↓  
Embedding Model  
↓  
Vector Database (FAISS)  
↓  
Relevant Document Retrieval  
↓  
LLM (HuggingFace / OpenAI)  
↓  
Generated Response  

---

## Tech Stack

- Python
- LangChain
- HuggingFace Transformers
- FAISS Vector Database
- FastAPI
- Docker
- PyTorch

---

## Key Features

- Document ingestion (PDF, TXT)
- Automatic document chunking
- Semantic vector embeddings
- Similarity search using FAISS
- LLM-powered question answering
- REST API for inference
- Scalable architecture for enterprise use

---

## Repository Structure
