from core.crypto import CryptoStream
from core.ai import AIHandler
import time
import json
import signal

def signal_handler(sig, frame):
    print("\nGracefully shutting down... 👋")
    exit(0)

def main():
    # Register signal handler
    signal.signal(signal.SIGINT, signal_handler)
    
    crypto = CryptoStream()
    ai = AIHandler()
    
    print("🔥 Crypto Watcher Started 🔥\n")
    
    while True:
        # Get crypto data
        data = crypto.get_crypto_data('BTC/USDT')
        
        # Save latest state for chat.py
        with open('state.json', 'w') as f:
            json.dump(data, f)
            
        # Format data string
        data_str = f"""
Coin: {data['coin']}
Time: {data['time']}
Volume: {data['volume']}
Price: {data['price']}
"""
        print(data_str)
        
        # Get AI response (will include queued messages)
        ai_response = ai.process_ai_response(data_str, include_queue=True)
        print(f"AI: {ai_response}\n")
        
        time.sleep(5)

if __name__ == "__main__":
    main() 