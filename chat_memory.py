from collections import deque

class ChatMemory:
    def __init__(self, max_turns=3):
        self.buffer = deque(maxlen=max_turns)

    def add_turn(self, user_input, bot_response):
        self.buffer.append((user_input, bot_response))

    def get_context(self):
        return "\n".join([f"User: {u}\nBot: {b}" for u, b in self.buffer])
