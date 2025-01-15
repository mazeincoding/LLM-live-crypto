import ccxt
import time
from datetime import datetime

# Initialize exchange
binance = ccxt.binance()

def format_volume(volume):
    """Convert volume to M/K format"""
    if volume >= 1_000_000:
        return f"{volume/1_000_000:.2f}M"
    elif volume >= 1_000:
        return f"{volume/1_000:.2f}K"
    return f"{volume:.2f}"

def get_crypto_data(symbol='BTC/USDT'):
    try:
        ticker = binance.fetch_ticker(symbol)
        
        return {
            'coin': symbol.split('/')[0],
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'volume': format_volume(ticker['quoteVolume']),
            'price': f"${ticker['last']:.3f}"
        }
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Test continuous streaming
try:
    while True:
        data = get_crypto_data()
        if data:
            print(f"""
Coin: {data['coin']}
Time: {data['time']}
Volume: {data['volume']}
Price: {data['price']}
""")
        time.sleep(5)
except KeyboardInterrupt:
    print("\nStopping data stream...") 