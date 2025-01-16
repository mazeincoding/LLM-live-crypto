import { Sidebar } from "@/components/sidebar";
import { Chat } from "@/components/chat";

export default function Home() {
  return (
    <div className="flex gap-4 h-screen">
      <Sidebar />
      <main className="flex-1 p-6 flex">
        <Chat />
      </main>
    </div>
  );
}
