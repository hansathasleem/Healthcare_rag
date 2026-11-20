
from app.embeddings.embedding_model import generate_embeddings
from app.vectorstore.faiss_store import vector_database
from app.retrieval.search import similarity_search


data = [
    {
        "text": "Hospitalization is covered under the policy.",
        "source": "healthcare_policy.pdf",
        "page": 1
    },
    {
        "text": "Emergency treatment is covered under eligible conditions.",
        "source": "claims_guidelines.pdf",
        "page": 2
    },
    {
        "text": "Pre-authorization is required for selected procedures.",
        "source": "provider_manual.docx",
        "page": None
    }
]

# Extract text from chunks
texts = [chunk["text"] for chunk in data]

# Generate embeddings
embedding = generate_embeddings(texts)

# Create FAISS database
index = vector_database(embedding)

# User question
userquery = "Is hospitalization covered under the policy?"

# Retrieve relevant chunks
results = similarity_search(userquery, index, data, top_k=2)

# Display results
for result in results:

    print("\nSource:", result["source"])
    print("Page:", result["page"])
    print("Text:", result["text"])
