import { Routes, Route, NavLink } from 'react-router-dom';
import { Users, FileText, LogOut } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import UserManagement from '../components/admin/UserManagement';
import ContentManagement from '../components/admin/ContentManagement';

function AdminPanel() {
  const { user, logout } = useAuth();

  return (
    <div className="flex h-screen bg-gray-100">
      <aside className="w-64 bg-white border-r">
        <div className="p-6">
          <h1 className="text-xl font-bold text-[#7D3C98]">Panel Admin</h1>
        </div>
        <nav className="px-4">
          <NavLink
            to="/admin/users"
            className={({ isActive }) =>
              `flex items-center gap-2 px-4 py-2 rounded-lg ${isActive ? 'bg-purple-50 text-[#7D3C98]' : 'text-gray-600 hover:bg-gray-50'
              }`
            }
          >
            <Users size={20} />
            Usuarios
          </NavLink>
          <NavLink
            to="/admin/content"
            className={({ isActive }) =>
              `flex items-center gap-2 px-4 py-2 rounded-lg ${isActive ? 'bg-purple-50 text-[#7D3C98]' : 'text-gray-600 hover:bg-gray-50'
              }`
            }
          >
            <FileText size={20} />
            Contenido
          </NavLink>
          <button
            onClick={logout}
            className="flex items-center gap-2 px-4 py-2 text-gray-600 hover:bg-gray-50 rounded-lg w-full mt-4"
          >
            <LogOut size={20} />
            Cerrar Sesión
          </button>
        </nav>
      </aside>

      <main className="flex-1 overflow-y-auto">
        <Routes>
          <Route path="users" element={<UserManagement />} />
          <Route path="content" element={<ContentManagement />} />
        </Routes>
      </main>
    </div>
  );
}

export default AdminPanel;