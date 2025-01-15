# What is this?

It's a cool project that allows LLMs to look at crypto in real-time. Imagine just having a crypto buddy available 24/7 watching the data without breaks, and the LLM can either respond by itself if it sees something interesting, or answer human questions.

Think about it, it's what humans do too:
- you can see something interesting and say something
- or answer all your friend's questions about what's going on

The problem with LLMs is they go like input/output, you've probably seen it:
```
user: blah
AI: blah
user: blah
AI: blah
```

It's designed to respond only when there's input. Humans can do that too...

but they can also see something and react by themselves, without input.

Example:
```
human: bitcoin just went up a lot
human: it went down again
human: but the volume is getting lower
```

LLMs are limited by that. This project works around the problem, and here's how it works:
- there's a loop every 5 sec that sends an automated user message with the price, volume, timestamp and coin
- the AI has instructions to respond with specifically "watching..." if it got nothing to say
- if it sees something interesting, it could respond out of the blue without input, like "I see the volume is starting to..."

If you think about it, there's still one problem left:

"what if the human asks the AI a question right after the automated user message sent?"

Because that's the key point about this project - being able to ask the LLM questions as it's watching data live.

The solution? Create a queue with user messages. So if a user sends a message right after the automated user message, it will put that message into the next automated message.

A cool example that shows this off really well:
```
User:
  Coin: BTC
  Timestamp: 2023-04-15 14:37:52
  Volume: 2.24M
  Price: $99.242
  
[user says "do you see anything?"]
[message added to queue]

AI:
watching...

[Now we can add the queued message to the automated message]
User:
  Coin: BTC
  Timestamp: 2023-04-15 14:37:53
  Volume: 2.24M
  Price: $99.242
  User message: do you see anything?

[the AI sees the new data and user message]
AI: Yes, I can see...
```

"but if the message gets delayed, the LLM might see it too late"

No! Because the loop is fast enough for exactly that. 5 seconds might be too long, but we can always adjust. Though the general idea works.