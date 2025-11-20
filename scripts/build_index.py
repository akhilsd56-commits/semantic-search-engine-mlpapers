import csv
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import os

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Paths
CSV_PATH = "scripts/papers.csv"
INDEX_PATH = "embeddings/vector_index.faiss"
META_PATH = "embeddings/metadata.npy"

titles = []
abstracts = []
ids = []

# Load CSV
with open(CSV_PATH, newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        ids.append(i)                    # Auto-generate ID
        titles.append(row["title"])
        abstracts.append(row["abstract"])

# Create embeddings
texts = [t + " " + a for t, a in zip(titles, abstracts)]
embeddings = model.encode(texts, convert_to_numpy=True)

# Create FAISS index
d = embeddings.shape[1]  # should be 384
index = faiss.IndexFlatL2(d)
index.add(embeddings)

# Save index and metadata
faiss.write_index(index, INDEX_PATH)
np.save(META_PATH, {
    "ids": ids,
    "titles": titles,
    "abstracts": abstracts
})

print("Vector index created!")
