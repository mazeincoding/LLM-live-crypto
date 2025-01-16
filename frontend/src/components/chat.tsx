"use client";

import { cn } from "@/lib/utils";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "./ui/accordion";
import { ScrollArea } from "./ui/scroll-area";
import { Input } from "./ui/input";
import { MessageSquare } from "lucide-react";
import { useState } from "react";
import { Button } from "./ui/button";
import { TMessage } from "@/types/message";

export function Chat() {
  return (
    <div className="border flex-1 rounded-lg flex flex-col">
      <ChatHeader />
      <ChatMessages />
      <ChatFooter />
    </div>
  );
}

function ChatHeader() {
  const [accordionValue, setAccordionValue] = useState<string | undefined>(
    undefined
  );

  const generateFakeData = () => {
    return Array.from({ length: 40 }, (_, i) => ({
      coin: "BTC",
      timestamp: new Date(Date.now() - i * 5000)
        .toISOString()
        .slice(0, 19)
        .replace("T", " "),
      volume: "2.24M",
      price: (Math.random() * (100000 - 90000) + 90000).toFixed(3),
    }));
  };

  const fakeData = generateFakeData();

  return (
    <div className="flex flex-col gap-4 p-4">
      <div className="flex items-center gap-2">
        <MessageSquare className="w-6 h-6" />
        <h2 className="text-xl font-bold">AI Chat</h2>
      </div>
      <Accordion
        type="single"
        collapsible
        value={accordionValue}
        onValueChange={setAccordionValue}
      >
        <AccordionItem
          value="item-1"
          className={cn(
            "border rounded-lg transition-all duration-200",
            accordionValue === "item-1" && "bg-accent/50"
          )}
        >
          <AccordionTrigger
            className={cn(
              "hover:no-underline !p-3 pb text-muted-foreground hover:text-foreground",
              accordionValue === "item-1" && "!text-foreground"
            )}
          >
            Watching BTC...
          </AccordionTrigger>
          <AccordionContent className="p-3 pt-0">
            <ScrollArea className="h-[200px]">
              <div className="animate-in fade-in duration-200">
                {fakeData.map((entry, index) => (
                  <div key={index} className="text-sm text-muted-foreground">
                    {`${entry.coin}, ${entry.timestamp}, ${entry.volume}, $${entry.price}`}
                  </div>
                ))}
              </div>
            </ScrollArea>
          </AccordionContent>
        </AccordionItem>
      </Accordion>
    </div>
  );
}

function ChatMessages() {
  const messages: TMessage[] = [
    {
      id: "msg-1",
      message: "Yo, see anything?",
      type: "user",
      timestamp: new Date(),
    },
    {
      id: "msg-2",
    message:
        "Yes, I can see BTC is currently at $100,000 Let's keep watching",
      type: "ai",
      timestamp: new Date(),
    },
  ];

  return (
    <ScrollArea className="flex-1 p-4 pt-0">
      <div className="flex flex-col gap-4">
        {messages.map((message) => (
          <ChatBubble key={message.id} message={message} />
        ))}
      </div>
    </ScrollArea>
  );
}

function ChatBubble({ message }: { message: TMessage }) {
  return (
    <div
      className={cn("flex", {
        "justify-end": message.type === "user",
        "justify-start": message.type === "ai",
      })}
    >
      <div
        className={cn("flex flex-col gap-2 rounded-lg p-3 max-w-[80%]", {
          "bg-primary text-primary-foreground": message.type === "user",
          "bg-muted": message.type === "ai",
        })}
      >
        <div className="text-sm font-medium">
          {message.type === "user" ? "You" : "Claude 3.5 Sonnet"}
        </div>
        <p className="text-sm">{message.message}</p>
      </div>
    </div>
  );
}

function ChatFooter() {
  return (
    <div className="border-t p-4 flex gap-2">
      <Input type="text" placeholder="Type a message..." className="flex-1" />
      <Button>Send</Button>
    </div>
  );
}
