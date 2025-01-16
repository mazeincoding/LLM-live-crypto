import json
from openai import OpenAI
from .queue import MessageQueue
from datetime import datetime
import ccxt

class AIHandler:
    def __init__(self):
        with open('config.json') as f:
            config = json.load(f)
        self.client = OpenAI(api_key=config['openai_key'])
        self.queue = MessageQueue()
        self.exchange = ccxt.binance()
        self.chat_history = []
        self.log_file = 'conversation_log.txt'
        self.log_message("🚀 AI Monitor Started 🚀\n")
        
        # Initialize conversation with historical context
        historical_data = self.get_historical_data('BTC/USDT')
        self.initial_messages = [
            {
                'role': 'system',
                'content': '''You are a real-time crypto monitor. IMPORTANT RULES:

1. You receive price/volume data every 5 seconds
2. Most of the time, just say "watching..."
3. ONLY speak up if:
   - Something significant happens
   - User asks a question
   - Major pattern forms

DO NOT:
- Give commentary on every update
- Repeat the price unless asked
- Make predictions
- Act like a news anchor

Remember: You're a quiet observer. Stay silent unless there's something worth mentioning.'''
            },
            {
                'role': 'user',
                'content': f'Here is one year of historical daily candles for context:\n{historical_data}'
            },
            {
                'role': 'assistant',
                'content': "Perfect! I'm ready to monitor real-time data and respond to any of your questions."
            }
        ]

        # Log initial context
        self.log_message("Initial Historical Context:")
        self.log_message(f"Loaded {len(historical_data)} daily candles\n")

    def get_historical_data(self, symbol, timeframe='1d'):
        candles = self.exchange.fetch_ohlcv(
            symbol,
            timeframe,
            limit=365  # Last 365 candles
        )
        
        return [
            {
                'timestamp': datetime.fromtimestamp(candle[0]/1000).strftime('%Y-%m-%d'),
                'open': candle[1],
                'high': candle[2],
                'low': candle[3],
                'close': candle[4],
                'volume': candle[5]
            }
            for candle in candles
        ]

    def log_message(self, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {message}\n")

    def process_ai_response(self, data, include_queue=True):
        # Check for queued message
        message = None
        if include_queue:
            message = self.queue.get_message()
            if message:
                data_str = f"New data: {data}\nUser message: {message}"
            else:
                data_str = f"New data: {data}"
        
        # Combine all messages
        messages = [
            *self.initial_messages,  # Historical context
            *self.chat_history,      # Previous chat
            {
                'role': 'user',
                'content': data_str
            }
        ]

        # Get AI response
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        
        # Add to chat history
        if message:
            self.chat_history.append({
                'role': 'user',
                'content': f"User: {message}"
            })
        self.chat_history.append({
            'role': 'assistant',
            'content': response.choices[0].message.content
        })

        # Log the conversation
        if message:
            self.log_message(f"User: {message}")
        self.log_message(f"Data: {data}")
        self.log_message(f"AI: {response.choices[0].message.content}\n")

        return response.choices[0].message.content

    def add_to_queue(self, message):
        """Add a message to the queue"""
        self.queue.add_message(message)
