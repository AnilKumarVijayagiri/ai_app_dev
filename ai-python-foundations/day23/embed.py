from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
sentences=[
    "I love eating pizza",
    "I enjoy eating burgers",
    "Python is a programming language"
]
embeddings=model.encode(sentences)
print(embeddings)