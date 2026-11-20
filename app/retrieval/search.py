
import faiss
import numpy as np

from app.embeddings.embedding_model import generate_query_embedding


def similarity_search(userquery, index, chunks, top_k=3):

    # Convert user question into embedding
    useremb = generate_query_embedding(userquery)

    # Normalize query embedding
    faiss.normalize_L2(useremb)

    # Search in FAISS
    distances, indices = index.search(useremb, top_k)

    results = []

    for i in indices[0]:

        if i == -1:
            continue

        results.append(chunks[i])

    return results
