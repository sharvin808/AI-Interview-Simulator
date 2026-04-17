from google import genai
import os

client = genai.Client(api_key=os.getenv("AI_Interview_API_KEY"))

def generate_question(role):
    try:
        prompt = f"Generate one interview question for a {role}. Keep it professional."

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print("ERROR:", e)
        return f"Tell me about yourself as a {role}"