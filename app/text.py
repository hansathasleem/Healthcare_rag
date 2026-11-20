from app.ingestion.document_loader import load_document

# PDF file path
file_path =r"G:\hansa AI\project\healthcare_rag\data\raw\healthcare_policy.pdf"

# Load document
result = load_document(file_path)

# Display extracted information
print("Number of pages:", len(result))

for item in result:

    print("\nSource:", item["source"])
    print("Page:", item["page"])
    print("Extracted text:")
    print(item["text"][:300])