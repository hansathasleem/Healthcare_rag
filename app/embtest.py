from app.embeddings.embedding_model import generate_embeddings

semantic = [
    "Hospitalization is covered under the policy.",
    "Emergency treatment is covered.",
    "Pre-authorization is required for selected procedures."
]

vector = generate_embeddings(semantic)

print(vector)
print("Vector shape:", vector.shape)