import requests
import os
import dotenv
dotenv.load_dotenv()

def get_car_ai_bio_gemini(model, brand, year):
    api_key = os.getenv("GEMINI_API_KEY")
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
    headers = {
        "Content-Type": "application/json"
    }
    prompt = (
        f"Me mostre uma descrição de venda para o carro {brand} {model} {year} em até 250 caracteres. "
        "Fale coisas específicas desse modelo e destaque pontos positivos."
    )
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    response = requests.post(f"{url}?key={api_key}", headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        try:
            return result['candidates'][0]['content']['parts'][0]['text']
        except (KeyError, IndexError):
            return "Erro: resposta inesperada da API Gemini."
    else:
        return f"Erro Gemini: {response.status_code} - {response.text}"