from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
emb = model.encode(["test"])[0]
print("Embedding dimension =", len(emb))
