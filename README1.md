# Semantic Search Engine for Research Papers  
Sentence Transformers + FAISS + Django REST

This project is a semantic search engine for research papers.  
Instead of relying on keyword matching, it uses vector embeddings to find papers that are *semantically* similar to a user query.

The focus of this project is building a **fast, practical search backend** with clean APIs and a simple, scalable design.

---

## Problem Statement

Traditional keyword-based search often fails when the wording does not exactly match the query.  
Synonyms, paraphrasing, and contextual meaning are usually missed.

This system solves that by:
- Encoding research paper abstracts into dense vector embeddings
- Performing similarity search using FAISS
- Returning the most relevant results based on semantic similarity

### Goals
- Accurate semantic matching beyond keywords  
- Sub-100ms query latency  
- Simple and extensible REST APIs  
- A clean embedding and indexing pipeline  

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

### Components
- **API Layer**: Django REST Framework handles incoming search requests  
- **Embedding Layer**: Sentence Transformers convert text into dense vectors  
- **Indexing Layer**: FAISS performs fast nearest-neighbor search  
- **Ranking Layer**: Results are sorted by similarity score  

---

## Key Features

- Semantic embeddings using Sentence Transformers  
- FAISS-based vector similarity search  
- REST API for easy integration  
- Modular scripts for ingestion and index creation  
- < 100ms search latency on 10K+ documents  
- Works with FAISS CPU on Windows  

---

## Tech Stack

- **Language**: Python 3.10  
- **API Framework**: Django, Django REST Framework  
- **Embeddings**: Sentence Transformers  
- **Vector Search**: FAISS (CPU)  
- **Data Processing**: NumPy, Pandas  

> Note: FAISS does not support Python 3.13.  
> This project is tested with **Python 3.10**.

---

## API Design

### Search Endpoint

POST /api/search/
**Request**
```json
{
  "query": "deep learning in NLP",
  "top_k": 5
}

Response
[
  {
    "paper": "Neural Networks for NLP",
    "abstract": "This paper discusses NLP using neural networks...",
    "score": -0.92
  }
]
Performance

Latency: < 100ms per query

Dataset Size: 10,000+ research papers

Search Type: Approximate Nearest Neighbor (ANN)

FAISS allows fast similarity search while keeping good accuracy as the dataset grows.

How to Run Locally
Prerequisites

Python 3.10

pip

Setup
git clone https://github.com/akhilsd56-commits/semantic-search-engine-mlpapers.git
cd semantic-search-engine-mlpapers

python -m venv venv
source venv/bin/activate   # Mac/Linux
# .\venv\Scripts\activate  # Windows

pip install -r requirements.txt
pip install faiss-cpu

Build the Index
cd scripts
python load_papers.py
python build_index.py
cd ..
Run the Server
python manage.py runserver
Server will be available at:
http://127.0.0.1:8000/

Project Structure
semantic-search-engine-mlpapers/
│
├── api/              # REST API endpoints
├── embeddings/       # Vector index and embedding logic
├── scripts/          # Data ingestion and FAISS index creation
├── settings/         # Django configuration
├── manage.py
├── requirements.txt
└── README.md

Design Notes
Embeddings are generated once and reused to keep query latency low
Clear separation between API, embedding, and indexing logic
Optimized for read-heavy workloads
Easy to extend with re-ranking, filters, or hybrid search

Future Improvements
Incremental index updates
Hybrid keyword + semantic search
Metadata-based filtering (author, year, domain)
Scaling FAISS with sharding

Why This Project Exists
This project was built to explore:
Practical semantic search systems
Vector-based retrieval using FAISS
Backend performance and API design
It reflects patterns commonly used in real-world search and retrieval services.
