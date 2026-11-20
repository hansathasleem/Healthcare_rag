import os
from dotenv import load_dotenv

load_dotenv()

# Gemini configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)

# Embedding configuration
EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "all-MiniLM-L6-v2"
)

# Chunk configuration
CHUNK_SIZE = 200
CHUNK_OVERLAP = 40

# Retrieval configuration
TOP_K = 5

# Project directories
DATA_DIR = "data/raw"
STORAGE_DIR = "storage"

INDEX_PATH = "storage/faiss.index"
METADATA_PATH = "storage/metadata.json"

print("Healthcare RAG configuration loaded!")