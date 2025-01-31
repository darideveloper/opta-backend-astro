const MessageInput = ({ inputMessage, setInputMessage, setMessages }) => (
    <div className="p-4 bg-white border-t border-gray-200">
        <div className="flex space-x-2">
            <input
                type="text"
                className="flex-1 p-2 border border-gray-300 rounded-l-md focus:outline-none focus:border-[#7D3C98]"
                placeholder="Escribe un mensaje..."
                value={inputMessage}
                onChange={(e) => setInputMessage(e.target.value)}
            />
            <button
                className="px-4 py-2 bg-[#7D3C98] text-white rounded-r-md hover:bg-[#7D3C98]"
                onClick={() => {
                    if (inputMessage.trim()) {
                        const now = new Date();
                        const formattedDate = now.toISOString();
                        const newMessage = { content: inputMessage, title: 'Usuario', timestamp: formattedDate };
                        setMessages((prevMessages) => [...prevMessages, newMessage]);
                        setInputMessage('');
                    }
                }}
            >
                ENVIAR
            </button>
        </div>
    </div>
);

export default MessageInput;
