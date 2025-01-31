import { CircleChevronDown, CircleChevronUp } from "lucide-react";

const ChatMessages = ({ messages }) => (
    <>
        {messages.map((message, index) => (
            <div key={index} className="mb-4 p-4 rounded-lg bg-white shadow">
                <div className="font-medium text-[#7D3C98] mb-2">{message.title}</div>
                <p>{message.content}</p>
                <div className="flex space-x-2 mt-2">
                    <button className="text-[#7D3C98] hover:text-purple-800">
                        <CircleChevronDown className="w-5 h-5" />
                    </button>
                    <button className="text-red-600 hover:text-red-800">
                        <CircleChevronUp className="w-5 h-5" />
                    </button>
                </div>
            </div>
        ))}
    </>
);

export default ChatMessages;
