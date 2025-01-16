import ccxt
from datetime import datetime

class CryptoStream:
    def __init__(self):
        self.exchange = ccxt.binance()

    def format_volume(self, volume):
        if volume >= 1_000_000:
            return f"{volume/1_000_000:.2f}M"
        elif volume >= 1_000:
            return f"{volume/1_000:.2f}K"
        return f"{volume:.2f}"

    def get_crypto_data(self, symbol='BTC/USDT'):
        try:
            ticker = self.exchange.fetch_ticker(symbol)
            
            return {
                'coin': symbol.split('/')[0],
                'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'volume': self.format_volume(ticker['quoteVolume']),
                'price': f"${ticker['last']:.3f}"
            }
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None
