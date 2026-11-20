from app.ingestion.pipeline import process_documents

chunks = process_documents()

print("\nFirst 3 chunks:")

for chunk in chunks[:3]:

    print("\n--------------------")
    print("Chunk ID:", chunk["chunk_id"])
    print("Source:", chunk["source"])
    print("Page:", chunk["page"])
    print("Sheet:", chunk["sheet"])
    print("Text:", chunk["text"][:200])