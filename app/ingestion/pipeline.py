
import os

from app.config import DATA_DIR, CHUNK_SIZE, CHUNK_OVERLAP
from app.ingestion.document_loader import load_document
from app.ingestion.chunking import overlapchunking


def process_documents():

    # Store all generated chunks
    all_chunks = []

    # Generate unique chunk IDs
    chunk_counter = 1

    # Read all files from the raw data folder
    for filename in os.listdir(DATA_DIR):

        file_path = os.path.join(DATA_DIR, filename)

        # Skip folders
        if not os.path.isfile(file_path):
            continue

        print(f"Processing: {filename}")

        # Step 1: Load document
        documents = load_document(file_path)

        # Step 2: Process each page or sheet
        for document in documents:

            text = document["text"]

            # Step 3: Convert text into words
            words = text.split()

            # Skip empty documents
            if not words:
                continue

            # Step 4: Create overlapping chunks
            chunks = overlapchunking(
                words,
                CHUNK_SIZE,
                CHUNK_OVERLAP
            )

            # Step 5: Attach metadata to each chunk
            for chunk in chunks:

                chunk_data = {
                    "chunk_id": chunk_counter,
                    "text": chunk,
                    "source": document["source"],
                    "page": document.get("page"),
                    "sheet": document.get("sheet")
                }

                # Step 6: Store chunk
                all_chunks.append(chunk_data)

                chunk_counter += 1

    print("\nDocument processing completed!")
    print("Total chunks:", len(all_chunks))

    # Step 7: Return all chunks
    return all_chunks
