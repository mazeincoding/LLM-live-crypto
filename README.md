# What is this?

It's a cool project that allows LLMs to look at crypto in real-time. Imagine just having a crypto buddy available 24/7 watching the data without breaks, and the LLM can either respond by itself if it sees something interesting, or answer human questions.

Imagine an app like ChatGPT:
- You start by selecting a crypto currency you want to watch
- First, it'll automatically get up-to-date news from @CoinbaseAssets on X
- The LLM then sees these
- And it can also see a little history of the coin
- You can ask questions while the LLM is watching the crypto

Think about this for a sec:
- You're sitting with your friend, watching BTC
- You say to your friend "it's at a pretty good price to buy"
- Friend goes "Nah, I think it'll go further down"
- You both watch for 2 minutes
- Friend says "Might be a good time now"

(that friend is the AI in this project)

# How does the project work?

So we got a `frontend` and `backend` folder at the root.
- Frontend: Next.js app
- Backend: Python server

# How does the AI watch data in real-time?

The problem with LLMs is they go like input/output, you've probably seen it:
```
user
AI
user
AI
```

It's not able to respond whenever it wants. It's literally just a model receiving input, and then it gives output.

Humans can do that too... but they can also see something and react by themselves, without input. Example:
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

Because that's the key point about this project - being able to ask the LLM questions as it's watching data in real time.

The solution? Create a queue with user messages. So if a user sends a message right after the automated user message, it will put that message into the next automated message.

An example that shows this off really well:
```
User message: Coin: BTC, Timestamp: 2023-04-15 14:37:52, Volume: 2.24M, Price: $99.242
  
[user sends a message "do you see anything?"]
[message added to queue]

AI:
watching... (it hasn't seen the message yet)

[Now the queued messages will be added to the automated message]
User: Coin: BTC, Timestamp: 2023-04-15 14:37:53, Volume: 2.24M, Price: $99.242, User message: do you see anything?

[the AI sees the new data and user message]
AI: Yes, I can see...
```

"but what if the message gets delayed and the AI sees it too late, when the data is already old?"

The loop should be fast enough for that. 5 seconds might be too long, but we can always adjust.

Another problem: while the AI is answering the user, it can't see the data in real-time. How do we handle this?
- we could stop generating response after 5s to give it new data
- or just accept the limitation