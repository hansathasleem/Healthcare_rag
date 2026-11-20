
from app.generation.gemini_llm import generate_answer


context = """
Source: healthcare_policy.pdf
Page: 1

Hospitalization is covered under the policy,
subject to the applicable plan terms and conditions.
"""

userquery = "Is hospitalization covered under the policy?"

answer = generate_answer(userquery, context)

print("\nGemini Answer:")
print(answer)
