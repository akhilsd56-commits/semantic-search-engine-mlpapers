import csv
import faiss
import numpy as np
import os
from django.conf import settings

# Load FAISS index once
faiss_index = faiss.read_index(settings.FAISS_INDEX_PATH)

# Load embeddings CSV

PAPERS = []
with open(settings.PAPERS_CSV_PATH, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        PAPERS.append(row)


def run_search(query):
    # Convert query → vector (dummy example)
    query_vector = np.random.rand(384).astype("float32")

    # Search
    distances, indices = faiss_index.search(query_vector.reshape(1, -1), 5)

    results = []
    for idx in indices[0]:
        if idx < len(PAPERS):
            results.append(PAPERS[idx])

    return results
