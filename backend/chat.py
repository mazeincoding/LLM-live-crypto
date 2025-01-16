from core.ai import AIHandler
import json
import signal

def signal_handler(sig, frame):
    print("\nChat session ended... 👋")
    exit(0)

def main():
    # Register signal handler
    signal.signal(signal.SIGINT, signal_handler)
    
    ai = AIHandler()
    
    print("🤖 Crypto Chat Started 🤖\n")
    print("Ask me anything about the crypto data I'm watching!\n")
    
    while True:
        user_input = input("You: ")
        
        # Add to queue instead of immediate processing
        ai.add_to_queue(user_input)
        print("\nMessage queued! Watch the other terminal for response...\n")

if __name__ == "__main__":
    main() 