import logo from "../assets/título.png";

const Sidebar = ({ isNewLead, setIsNewLead, programs, moments, handleMomentClick }) => (
    <div className="w-64 bg-white border-r border-gray-200 flex flex-col">
        <div className="p-4 border-b border-gray-200">
            <div className="flex items-center justify-between mb-4">
                <div className="flex items-center space-x-2">
                    <img src={logo} className="w-9 h-9" alt="Logo" />
                    <span className="text-sm font-medium">
                        {isNewLead ? 'New Lead' : 'Seguimiento'}
                    </span>
                </div>
                <label className="relative inline-flex items-center cursor-pointer">
                    <input
                        type="checkbox"
                        className="sr-only peer"
                        checked={!isNewLead}
                        onChange={() => setIsNewLead(!isNewLead)}
                    />
                    <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-purple-300 rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-[#7D3C98]"></div>
                </label>
            </div>
            <select className="w-full p-2 border border-gray-300 rounded-md bg-[#7D3C98] text-white">
                <option value="">Carreras</option>
                {programs.map((program) => (
                    <option key={program.id} value={program.id}>
                        {program.name}
                    </option>
                ))}
            </select>
        </div>
        <div className="flex-1 overflow-y-auto p-4">
            {moments.map((moment) => (
                <button
                    key={moment.id}
                    onClick={() => handleMomentClick(moment)}
                    className="w-full p-2 mb-2 text-left border-2 border-[#7D3C98] rounded-lg hover:bg-[#7D3C98] hover:text-white transition-colors"
                >
                    {moment.name}
                </button>
            ))}
        </div>
    </div>
);

export default Sidebar;
