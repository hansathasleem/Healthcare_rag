
from app.services.rag_service import (
    build_knowledge_base,
    answer_question
)

# Build knowledge base
index, chunks = build_knowledge_base()

# Ask user question
userquery = input("\nEnter your healthcare question: ")

# Generate answer
result = answer_question(
    userquery,
    index,
    chunks
)

print("\nHealthcare RAG Answer:")
print(result["answer"])

print("\nSources:")

for source in result["sources"]:
    print(source)
