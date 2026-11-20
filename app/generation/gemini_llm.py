
from google import genai

from app.config import GEMINI_API_KEY, GEMINI_MODEL


# Create Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)


# Generate answer using retrieved context
def generate_answer(userquery, context):

    prompt = f"""
    You are a Healthcare Policy Assistant.

    Answer the user's question using ONLY the
    provided context.

    Rules:
    1. Do not invent information.
    2. Do not use outside knowledge.
    3. If the answer is not available in the context,
       respond exactly: NO DATA FOUND.
    4. Include the source document and page number
       when available.
    5. Do not make medical diagnoses or treatment
       recommendations.

    Context:
    {context}

    User Question:
    {userquery}

    Answer:
    """

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text
