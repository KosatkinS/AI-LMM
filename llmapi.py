import requests
import json
import os

AI_TOKEN="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"

def get_response(messages: list[dict]) -> str:
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {AI_TOKEN}"
    },
    data=json.dumps({
        "model": "openai/gpt-4o-mini", 
        "messages": messages
    })
    )

    return response.json()['choices'][0]['message']['content']