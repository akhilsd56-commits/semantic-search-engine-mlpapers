# Semantic Search Engine for Research Papers  
**Sentence Transformers + FAISS + Django REST**

A production-style semantic search engine that enables fast and relevant retrieval of research papers using dense vector embeddings instead of traditional keyword-based search.

This project emphasizes **low-latency retrieval, clean API design, and scalable indexing**, reflecting real-world search and recommendation system design.

---

## Problem Statement

Keyword-based search struggles with semantic meaning, synonyms, and contextual relevance.  
This system enables **semantic search** by encoding research paper abstracts into dense vector embeddings and performing similarity search using FAISS.

Primary goals:
- Accurate semantic matching beyond keywords
- Sub-100ms query latency
- Clean, extensible REST APIs
- Scalable embedding and indexing pipeline

---

## High-Level Architecture

Client
|
v
Django REST API
|
v
Sentence Transformer Encoder
|
v
FAISS Vector Index
|
v
Top-K Ranked Results

yaml
Copy code

### Component Overview
- **API Layer**: Django REST Framework exposes stateless search endpoints
- **Embedding Layer**: Sentence Transformers generate dense vector representations
- **Indexing Layer**: FAISS enables efficient approximate nearest-neighbor search
- **Ranking Layer**: Results ranked by cosine similarity scores

---

## Key Features

- Dense semantic embeddings using Sentence Transformers
- FAISS-based vector similarity search
- RESTful API interface for easy integration
- Modular ingestion and indexing pipeline
- **Sub-100ms search latency** on 10K+ documents
- Windows-compatible FAISS setup

---

## Tech Stack

- **Language**: Python 3.10  
- **API Framework**: Django, Django REST Framework  
- **Embeddings**: Sentence Transformers  
- **Vector Search**: FAISS (CPU)  
- **Data Processing**: NumPy, Pandas  

> ⚠️ FAISS is not compatible with Python 3.13.  
> This project requires **Python 3.10**.

---

## API Design

### Search Endpoint
POST /api/search/

pgsql
Copy code

**Request**
```json
{
  "query": "deep learning in NLP",
  "top_k": 5
}
Response

json
Copy code
[
  {
    "paper": "Neural Networks for NLP",
    "abstract": "This paper discusses NLP using neural networks...",
    "score": -0.92
  }
]
The API is designed to be stateless, idempotent, and extensible, following REST best practices.

Performance
Latency: < 100ms per query

Dataset Size: 10,000+ research papers

Search Type: Approximate nearest neighbor (ANN)

FAISS indexing enables fast similarity search while maintaining high recall.

How to Run Locally
Prerequisites
Python 3.10

pip

Setup
bash
Copy code
git clone https://github.com/akhilsd56-commits/semantic-search-engine-mlpapers.git
cd semantic-search-engine-mlpapers

python -m venv venv
source venv/bin/activate   # Mac/Linux
# .\venv\Scripts\activate  # Windows

pip install -r requirements.txt
pip install faiss-cpu
Build Index
bash
Copy code
cd scripts
python load_papers.py
python build_index.py
cd ..
Run Server
bash
Copy code
python manage.py runserver
Server starts at:

cpp
Copy code
http://127.0.0.1:8000/
Project Structure
graphql
Copy code
semantic-search-engine-mlpapers/
│
├── api/              # REST API endpoints
├── embeddings/       # Vector index and embedding logic
├── scripts/          # Data ingestion and FAISS index creation
├── settings/         # Django configuration
├── manage.py
├── requirements.txt
└── README.md
Design Considerations
Embeddings are generated once and reused to optimize query performance

Clear separation between API, embedding, and indexing layers

Optimized for read-heavy workloads

Architecture is extensible for re-ranking, metadata filtering, or hybrid search

Future Improvements
Incremental and streaming index updates

Hybrid keyword + semantic search

Metadata-based filtering (author, year, domain)

Horizontal scaling with sharded FAISS indexes

Why This Project Matters
This project demonstrates:

Applied NLP for real-world search problems

System-level thinking beyond model usage

Performance-driven backend engineering

Clean API and service architecture

It reflects the same principles used in production-grade search and retrieval systems.
