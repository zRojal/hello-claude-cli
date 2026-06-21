import os 
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

def call_claude(prompt: str, model: str="claude-sonnet-4-6", system: str="") -> str: 
    """ Send a prompt to claude"""
    response = client.messages.create(
        model=model,
        max_tokens=1024,
        system=system,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

def stream_claude(prompt: str, model: str="claude-sonnet-4-6", system: str=""):
     """ Send a prompt to claude and you'll get text by text"""

     with client.messages.stream(
          model=model,
          max_tokens=1024,
          system=system,
          messages=[{"role": "user", "content": prompt}], 
     ) as stream: 
        for text in stream.text_stream:
            yield text
        
     