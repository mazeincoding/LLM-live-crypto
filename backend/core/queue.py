import json
from pathlib import Path

class MessageQueue:
    def __init__(self):
        self.queue_file = 'message_queue.json'
        # Create empty queue file if it doesn't exist
        if not Path(self.queue_file).exists():
            self.save_queue([])

    def add_message(self, message):
        queue = self.load_queue()
        queue.append(message)
        self.save_queue(queue)

    def get_message(self):
        queue = self.load_queue()
        if queue:
            message = queue.pop(0)  # Get first message
            self.save_queue(queue)  # Save updated queue
            return message
        return None

    def load_queue(self):
        try:
            with open(self.queue_file, 'r') as f:
                return json.load(f)
        except:
            return []

    def save_queue(self, queue):
        with open(self.queue_file, 'w') as f:
            json.dump(queue, f) 