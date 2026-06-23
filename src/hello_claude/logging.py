import json
import os 
from datetime import datetime, timezone

LOG_DIR = os.path.expanduser("~/.hello-claude")
LOG_FIL = os.path.join(LOG_DIR, "calls.jsonl")

def log_call(model, system, prompt, response, input_tokens, output_tokens, latency_ms, cost_usd): 
    """Append one record of a Claude Call to the JSONL Log"""
    os.makedirs(LOG_DIR, exist_ok=True)

    entry = {
        "timestamp": datetime.now(timezone.utc) .isoformat(),
        "model": model,
        "system": system, 
        "prompt": prompt,
        "response": response,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "latency_ms": latency_ms,
        "cost_usd": cost_usd,
    }

    with open(LOG_FIL, "a") as f: 
        f.write(json.dumps(entry) + "\n")