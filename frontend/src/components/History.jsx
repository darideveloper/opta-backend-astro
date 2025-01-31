const HistoryComponent = ({ messages, onClose }) => {
    return (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-end">
            <div className="w-80 bg-white h-full p-4">
                <div className="flex justify-between items-center mb-4">
                    <h2 className="text-xl font-bold">Historial</h2>
                    <button
                        onClick={onClose}
                        className="text-gray-500 hover:text-gray-700"
                    >
                        ×
                    </button>
                </div>
                {/* Mostrar los mensajes pasados como prop*/}
                <div className="space-y-4">
                    {messages.map((message, index) => {
                        return (
                            <div key={index} className="p-2 bg-gray-100 rounded-md shadow">
                                <p className="font-medium text-[#7D3C98]">{message.title}</p>
                                <p>{message.content}</p>
                                <p className="text-sm text-gray-500">{message.timestamp}</p>
                            </div>
                        );
                    })}
                </div>
            </div>
        </div>
    );
};
export default HistoryComponent