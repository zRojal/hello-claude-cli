import os 
import time
from anthropic import Anthropic
from dotenv import load_dotenv
from hello_claude.logging import log_call
from hello_claude.pricing import compute_cost


load_dotenv()
client = Anthropic()

def call_claude(prompt: str, model: str="claude-sonnet-4-6", system: str="") -> str: 
    """ Send a prompt to claude"""
    start = time.time()
    response = client.messages.create(
        model=model,
        max_tokens=1024,
        system=system,
        messages=[{"role": "user", "content": prompt}]
    )

    latency_ms = int((time.time() - start)) * 1000

    text = response.content[0].text
    input_tokens = response.usage.input_tokens
    output_tokens = response.usage.output_tokens
    cost = compute_cost(model, input_tokens, output_tokens)

    log_call(model=model,
        system=system,
        prompt=prompt,
        response=text,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        latency_ms=latency_ms,
        cost_usd=cost,)

    return text
    
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
        
     