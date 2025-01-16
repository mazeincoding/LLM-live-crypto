from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.crypto import CryptoStream
from core.ai import AIHandler

app = FastAPI()
crypto = CryptoStream()
ai = AIHandler()

# CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/crypto/{symbol}")
async def get_latest_crypto(symbol: str):
    data = crypto.get_crypto_data(symbol)
    return data

@app.post("/api/chat")
async def chat_with_ai(message: dict):
    response = ai.process_ai_response(message)
    return response 