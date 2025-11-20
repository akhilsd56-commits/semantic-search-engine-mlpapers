import numpy as np
import pandas as pd
import faiss
from django.conf import settings
from sentence_transformers import SentenceTransformer


class SemanticSearchEngine:
    def __init__(self):
        self.model = SentenceTransformer(
            "sentence-transformers/all-mpnet-base-v2")
        self.index = faiss.read_index(settings.FAISS_INDEX_PATH)
        self.papers = pd.read_csv(settings.PAPERS_CSV_PATH)

    def search(self, query, top_k=5):
        emb = self.model.encode([query])
        D, I = self.index.search(np.array(emb).astype("float32"), top_k)

        results = []
        for score, idx in zip(D[0], I[0]):
            row = self.papers.iloc[idx]
            results.append({
                "paper": row["title"],
                "abstract": row["abstract"],
                "score": float(score)
            })
        return results
