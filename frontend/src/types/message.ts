export interface TMessage {
  id: string;
  message: string;
  type: "user" | "ai";
  timestamp: Date;
}
