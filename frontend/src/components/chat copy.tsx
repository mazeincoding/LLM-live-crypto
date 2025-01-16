import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "./ui/accordion";
import { ScrollArea } from "./ui/scroll-area";
import { MessageSquare } from "lucide-react";
import { Button } from "./ui/button";

export function Chat() {
  const generateFakeData = () => {
    return Array.from({ length: 10 }, (_, i) => ({
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
    <div className="flex-1 p-4 flex flex-col border rounded-lg">
      <div className="flex items-center gap-2">
        <MessageSquare className="w-6 h-6" />
        <h2 className="text-xl font-bold">AI Chat</h2>
      </div>

      <ScrollArea className="flex-1 pr-4">
        <div className="space-y-4">
          <div className="p-3 bg-muted">
            <Accordion type="single" collapsible>
              <AccordionItem value="data" className="border-none">
                <AccordionTrigger className="py-0 hover:no-underline">
                  <p className="text-sm text-muted-foreground">
                    Watching cryptocurrency data in real-time...
                  </p>
                </AccordionTrigger>
                <AccordionContent>
                  <ScrollArea className="h-[200px] w-full border rounded-md">
                    <div className="space-y-2 p-2 text-sm font-mono animate-in fade-in duration-200">
                      {fakeData.map((entry, index) => (
                        <div key={index} className="text-xs">
                          {`${entry.coin}, ${entry.timestamp}, ${entry.volume}, $${entry.price}`}
                        </div>
                      ))}
                    </div>
                  </ScrollArea>
                </AccordionContent>
              </AccordionItem>
            </Accordion>
          </div>
        </div>
      </ScrollArea>

      <div className="flex gap-2">
        <input
          type="text"
          placeholder="Ask a question..."
          className="flex-1 px-3 py-2 rounded-md border"
        />
        <Button>Send</Button>
      </div>
    </div>
  );
}
