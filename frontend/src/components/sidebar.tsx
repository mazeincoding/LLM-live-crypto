import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "./ui/select";
import { Button } from "./ui/button";

export function Sidebar() {
  return (
    <aside className="w-[350px] p-4 flex flex-col gap-4 border-r">
      <div className="flex-1 flex flex-col gap-4">
        <div className="flex items-center">
          <h2 className="text-xl font-bold">Select cryptocurrency</h2>
        </div>

        <Select>
          <SelectTrigger>
            <SelectValue placeholder="Choose a cryptocurrency" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="btc">Bitcoin (BTC)</SelectItem>
            <SelectItem value="eth">Ethereum (ETH)</SelectItem>
            <SelectItem value="usdt">Tether (USDT)</SelectItem>
          </SelectContent>
        </Select>
      </div>

      <Button variant="outline">Watch</Button>
    </aside>
  );
}
