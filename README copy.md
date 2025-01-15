# What is this?

It's a cool project that allows LLMs to look at crypto in real-time. Imagine having an AI crypto buddy available 24/7 watching the market data without breaks, who can both proactively share insights and respond to your questions.

## How it works

LLMs typically operate in a simple input/output pattern:
```
user: question
AI: answer
```

This project breaks that limitation by:
1. Running a loop every 5 seconds that feeds market data to the AI
2. Using a "watching..." response when nothing notable is detected
3. Allowing the AI to proactively comment on interesting patterns
4. Managing a message queue to handle user questions seamlessly

## Example Flow

```
User:
  Coin: BTC
  Timestamp: 2023-04-15 14:37:52
  Volume: 2.24M
  Price: $99.242
  
[User asks "do you see anything?"]
[Question added to queue]

AI: watching...

User:
  Coin: BTC
  Timestamp: 2023-04-15 14:37:53
  Volume: 2.24M
  Price: $99.242
  User message: do you see anything?

AI: Yes, I can see...
```

The 5-second loop ensures user questions are processed quickly enough to maintain context with the real-time data.