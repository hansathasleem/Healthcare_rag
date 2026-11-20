
import faiss
import numpy as np

# Create FAISS vector database
def vector_database(embedding):

    emb = np.array(embedding, dtype="float32")

    # Normalize vectors
    faiss.normalize_L2(emb)

    # Get vector dimension
    dim = emb.shape[1]

    # Create FAISS index
    index = faiss.IndexFlatL2(dim)

    # Add embeddings to index
    index.add(emb)

    return index
