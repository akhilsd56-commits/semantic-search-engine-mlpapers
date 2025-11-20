import pandas as pd

data = {
    "title": [
        "Neural Networks for NLP",
        "Vision Transformers Explained",
        "Reinforcement Learning Basics",
        "FAISS for Vector Search",
        "Sentence Transformers Guide"
    ],
    "abstract": [
        "This paper discusses NLP using neural networks...",
        "This explains ViT architecture...",
        "Introduction to RL...",
        "FAISS enables fast vector similarity search...",
        "Sentence-Transformers are used for embeddings..."
    ]
}

df = pd.DataFrame(data)
df.to_csv("papers.csv", index=False)
print("papers.csv created.")
