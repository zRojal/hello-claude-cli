import os 
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

def call_claude(prompt: str, model: str="claude-sonnet-4-6") -> str: 
    """ Send a prompt to claude"""
    response = client.messages.create(
        model=model,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text