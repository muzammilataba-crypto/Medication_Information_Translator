
import os
from google import genai


class AITranslator:

    def __init__(self):

        self.api_key = os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            raise ValueError(
                "Gemini API key not found. "
                "Please configure GEMINI_API_KEY."
            )

        self.client = genai.Client(
            api_key=self.api_key
        )

        self.model = "gemini-3.5-flash"

    def simplify(self, medical_text):

        if not medical_text or not medical_text.strip():
            return "No medical information is available to simplify."

        prompt = f"""
You are a medical information translator.

Your task is to explain complicated medical information
using simple, everyday English.

Follow these rules:

1. Use clear and simple language.
2. Explain difficult medical terms.
3. Preserve all important medical information.
4. Never invent medical facts.
5. Never change dosage instructions.
6. Do not diagnose medical conditions.
7. Explain possible side effects clearly.
8. Highlight important warnings and precautions.
9. If information is missing, say so.
10. Remind users to consult qualified healthcare professionals.

Organise your response using these headings:

WHAT THIS MEANS:
Explain the information simply.

IMPORTANT THINGS TO KNOW:
Highlight important details.

WARNINGS:
Explain any relevant precautions.

Remember that you are simplifying existing medical
information, not providing independent medical advice.

MEDICAL INFORMATION:

{medical_text}
"""

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )

            if response.text:
                return response.text.strip()

            return (
                "The AI could not generate an explanation. "
                "Please try again."
            )

        except Exception as error:

            print(f"Gemini API error: {error}")

            return (
                "Unable to simplify the medical information "
                "at the moment. Please check your internet "
                "connection and API configuration, then try again."
            )
