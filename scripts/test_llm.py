import json
from openai import OpenAI

# Load config
with open('config.json') as f:
    config = json.load(f)

client = OpenAI(api_key=config['openai_key'])

# Test basic message format
message = """
Coin: BTC
Time: 2024-01-15 14:37:52
Volume: 2.24M
Price: $99.242
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            'role': 'system',
            'content': 'You are monitoring crypto data. If you see something interesting, tell me. If not, just say "watching..."'
        },
        {
            'role': 'user',
            'content': message
        }
    ]
)

print(response.choices[0].message.content) 