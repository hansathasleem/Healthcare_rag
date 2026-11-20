
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

from app.config import EMBEDDING_MODEL


# Load embedding model
model = SentenceTransformer(EMBEDDING_MODEL)


# Generate embeddings for semantic chunks
def generate_embeddings(data):

    embedding = model.encode(data)

    emb = np.array(embedding, dtype="float32")

    return emb


# Generate embedding for user query
def generate_query_embedding(userquery):

    useremb1 = model.encode(userquery)

    useremb = np.array(useremb1, dtype="float32").reshape(1, -1)

    return useremb
