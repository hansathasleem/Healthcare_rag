
from app.ingestion.pipeline import process_documents
from app.embeddings.embedding_model import generate_embeddings
from app.vectorstore.faiss_store import vector_database
from app.retrieval.search import similarity_search
from app.generation.gemini_llm import generate_answer


# Build the healthcare knowledge base
def build_knowledge_base():

    # Load and chunk documents
    chunks = process_documents()

    if not chunks:
        raise ValueError("No document chunks found!")

    # Extract text from chunks
    texts = [chunk["text"] for chunk in chunks]

    # Generate embeddings
    embeddings = generate_embeddings(texts)

    # Create FAISS database
    index = vector_database(embeddings)

    print("Healthcare knowledge base created!")
    print("Total chunks:", len(chunks))

    return index, chunks


# Answer user question
def answer_question(userquery, index, chunks):

    # Retrieve relevant document chunks
    results = similarity_search(
        userquery,
        index,
        chunks,
        top_k=3
    )

    if not results:
        return {
            "answer": "NO DATA FOUND",
            "sources": []
        }

    # Prepare context for Gemini
    context_parts = []

    for result in results:

        context_parts.append(
            f"""
            Source: {result['source']}
            Page: {result.get('page')}
            Sheet: {result.get('sheet')}

            Content:
            {result['text']}
            """
        )

    context = "\n".join(context_parts)

    # Generate answer using Gemini
    answer = generate_answer(userquery, context)

    # Collect source information
    sources = []

    for result in results:

        sources.append({
            "source": result["source"],
            "page": result.get("page"),
            "sheet": result.get("sheet")
        })

    return {
        "answer": answer,
        "sources": sources
    }
