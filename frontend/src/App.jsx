import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './contexts/AuthContext';
//import PrivateRoute from './components/PrivateRoute';
//import Login from './pages/Login';
import Chat from './pages/Chat';
import AdminPanel from './pages/AdminPanel';

function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          {/* <Route path="/login" element={<Login />} /> */}
          <Route
            path="/chat"
            element={

              <Chat />

            }
          />
          <Route
            path="/admin/*"
            element={

              <AdminPanel />

            }
          />
          <Route path="/" element={<Navigate to="/chat" replace />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;