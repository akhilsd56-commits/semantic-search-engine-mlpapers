📘 README.md (Final GitHub Version — Copy This)
Semantic Search Engine (Sentence Transformers + FAISS)

A modern vector-based semantic search engine built using:

Python 3.10

Django REST Framework

Sentence Transformers

FAISS (vector similarity search)

NumPy + Pandas

This API performs semantic search on research paper abstracts using embeddings instead of keyword search.

🚀 Features

Transform text into dense embeddings

Build FAISS vector index for instant similarity lookup

Expose a clean REST API for semantic search

<100ms retrieval time

Windows-compatible FAISS installation

Ready for production scaling

📦 Requirements
Python Version
Python 3.10.x  (required)


⚠️ FAISS does NOT work on Python 3.13.
You must use Python 3.10 for this project.

Python Packages

Listed in requirements.txt:

django==4.2
djangorestframework==3.14.0
sentence-transformers==2.2.2
numpy
pandas

🛠️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/yourusername/semantic-search-engine-mlpapers.git
cd semantic-search-engine-mlpapers

2️⃣ Create virtual environment (Python 3.10)
py -3.10 -m venv venv

3️⃣ Activate environment
Windows:
.\venv\Scripts\activate

Mac/Linux:
source venv/bin/activate


You should now see:

(venv)

📥 Install Dependencies
4️⃣ Install base requirements
pip install -r requirements.txt

5️⃣ Install FAISS (Windows compatible)
pip install faiss-cpu


If above fails:

pip install faiss-cpu-windows

🧱 Build the Search Index
6️⃣ Generate sample papers dataset
cd scripts
python load_papers.py

7️⃣ Build FAISS vector index
python build_index.py
cd ..


This creates:

embeddings/vector_index.faiss

▶️ Run the API Server
python manage.py runserver


You will see:

Starting development server at http://127.0.0.1:8000/

🔍 API Usage
POST /api/search/
Example Request:
POST http://127.0.0.1:8000/api/search/
Content-Type: application/json

{
  "query": "deep learning in NLP"
}

Example Response:
[
  {
    "paper": "Neural Networks for NLP",
    "abstract": "This paper discusses NLP using neural networks...",
    "score": -0.92
  }
]

🏗 Project Structure
semantic-search-engine-mlpapers/
│
├── api/
│   ├── search_service.py
│   ├── views.py
│   ├── urls.py
│   └── apps.py
│
├── embeddings/
│   └── vector_index.faiss
│
├── models/
│
├── scripts/
│   ├── load_papers.py
│   └── build_index.py
│
├── settings/
│   ├── base.py
│   └── __init__.py
│
├── manage.py
├── requirements.txt
└── README.md