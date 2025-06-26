import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

def get_openrouter_response(prompt: str, model: str = "deepseek/deepseek-r1:free") -> tuple[str, str]:
    if not OPENROUTER_API_KEY:
        raise RuntimeError("OpenRouter API key not configured in OPENROUTER_API_KEY.")

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(OPENROUTER_API_URL, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        chat_response = data["choices"][0]["message"]["content"]
        model_used = data.get("model", model)
        return chat_response, model_used
    except Exception as e:
        raise RuntimeError(f"Erro ao conectar com OpenRouter: {str(e)}") 