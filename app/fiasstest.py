
from app.embeddings.embedding_model import generate_embeddings
from app.vectorstore.faiss_store import vector_database

data = [
    "Hospitalization is covered under the policy.",
    "Emergency treatment is covered.",
    "Pre-authorization is required for selected procedures."
]

# Generate embeddings
vector = generate_embeddings(data)

# Store embeddings in FAISS
index = vector_database(vector)

print("FAISS database created!")
print("Total vectors:", index.ntotal)
print("Vector dimension:", index.d)
