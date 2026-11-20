import fitz
from docx import Document
from openpyxl import load_workbook
import os
def load_pdf(file_path):

    documents = []

    pdf = fitz.open(file_path)

    for page_number, page in enumerate(pdf, start=1):

        text = page.get_text()

        if text.strip():

            documents.append({
                "text": text,
                "source": os.path.basename(file_path),
                "page": page_number
            })

    pdf.close()

    return documents
def load_docx(file_path):

    doc = Document(file_path)

    text = []

    for paragraph in doc.paragraphs:

        if paragraph.text.strip():

            text.append(paragraph.text)

    return [{
        "text": "\n".join(text),
        "source": os.path.basename(file_path),
        "page": None
    }]
def load_excel(file_path):

    workbook = load_workbook(
        file_path,
        data_only=True
    )

    documents = []

    for sheet in workbook.worksheets:

        rows = []

        for row in sheet.iter_rows(values_only=True):

            row_text = [
                str(cell)
                for cell in row
                if cell is not None
            ]

            if row_text:

                rows.append(" | ".join(row_text))

        documents.append({
            "text": "\n".join(rows),
            "source": os.path.basename(file_path),
            "sheet": sheet.title,
            "page": None
        })

    workbook.close()

    return documents

def load_document(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":

        return load_pdf(file_path)

    elif extension == ".docx":

        return load_docx(file_path)

    elif extension == ".xlsx":

        return load_excel(file_path)

    else:

        raise ValueError(
            f"Unsupported file format: {extension}"
        )
