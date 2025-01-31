import { useState, useEffect } from 'react';
import { Upload, Pencil, Trash2, Plus, X } from 'lucide-react';
import axios from 'axios';

function ContentManagement() {
    const [content, setContent] = useState([]);
    const [showModal, setShowModal] = useState(false);
    const [editingContent, setEditingContent] = useState(null);
    const [formData, setFormData] = useState({
        title: '',
        description: '',
        keywords: '',
        file: null
    });

    useEffect(() => {
        fetchContent();
    }, []);

    const fetchContent = async () => {
        try {
            const response = await axios.get('/api/content', {
                headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
            });
            setContent(response.data);
        } catch (error) {
            console.error('Error al obtener contenido:', error);
        }
    };

    const handleFileChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            setFormData({ ...formData, file });
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formDataToSend = new FormData();
        formDataToSend.append('title', formData.title);
        formDataToSend.append('description', formData.description);
        formDataToSend.append('keywords', formData.keywords);
        if (formData.file) {
            formDataToSend.append('file', formData.file);
        }

        try {
            if (editingContent) {
                await axios.put(`/api/content/${editingContent.id}`, formDataToSend, {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('token')}`,
                        'Content-Type': 'multipart/form-data'
                    }
                });
            } else {
                await axios.post('/api/content', formDataToSend, {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('token')}`,
                        'Content-Type': 'multipart/form-data'
                    }
                });
            }
            setShowModal(false);
            setEditingContent(null);
            setFormData({ title: '', description: '', keywords: '', file: null });
            fetchContent();
        } catch (error) {
            console.error('Error al guardar contenido:', error);
        }
    };

    const handleDelete = async (contentId) => {
        if (window.confirm('¿Está seguro de eliminar este contenido?')) {
            try {
                await axios.delete(`/api/content/${contentId}`, {
                    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
                });
                fetchContent();
            } catch (error) {
                console.error('Error al eliminar contenido:', error);
            }
        }
    };

    const handleEdit = (content) => {
        setEditingContent(content);
        setFormData({
            title: content.title,
            description: content.description,
            keywords: content.keywords,
            file: null
        });
        setShowModal(true);
    };

    return (
        <div className="p-6">
            <div className="flex justify-between items-center mb-6">
                <h2 className="text-2xl font-bold text-gray-800">Gestión de Contenido</h2>
                <button
                    onClick={() => {
                        setEditingContent(null);
                        setFormData({ title: '', description: '', keywords: '', file: null });
                        setShowModal(true);
                    }}
                    className="flex items-center gap-2 px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700"
                >
                    <Plus size={20} />
                    Nuevo Contenido
                </button>
            </div>

            <div className="bg-white rounded-lg shadow p-6 mb-6">
                <div className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center">
                    <Upload className="mx-auto h-12 w-12 text-gray-400" />
                    <p className="mt-2 text-sm text-gray-600">
                        Arrastra archivos aquí o
                        <label className="ml-1 text-purple-600 hover:text-purple-500 cursor-pointer">
                            <span>selecciona un archivo</span>
                            <input
                                type="file"
                                className="hidden"
                                onChange={handleFileChange}
                                accept=".pdf,.doc,.docx,.txt"
                            />
                        </label>
                    </p>
                    <p className="text-xs text-gray-500">
                        PDF, DOC, TXT hasta 10MB
                    </p>
                </div>
            </div>

            <div className="bg-white rounded-lg shadow">
                <table className="min-w-full">
                    <thead>
                        <tr className="border-b">
                            <th className="px-6 py-3 text-left text-sm font-semibold text-gray-600">NOMBRE</th>
                            <th className="px-6 py-3 text-left text-sm font-semibold text-gray-600">TIPO</th>
                            <th className="px-6 py-3 text-left text-sm font-semibold text-gray-600">FECHA</th>
                            <th className="px-6 py-3 text-right text-sm font-semibold text-gray-600">ACCIONES</th>
                        </tr>
                    </thead>
                    <tbody>
                        {content.map((item) => (
                            <tr key={item.id} className="border-b">
                                <td className="px-6 py-4 text-sm text-gray-800">{item.title}</td>
                                <td className="px-6 py-4 text-sm text-gray-800">{item.type}</td>
                                <td className="px-6 py-4 text-sm text-gray-800">
                                    {new Date(item.createdAt).toLocaleDateString()}
                                </td>
                                <td className="px-6 py-4 text-right">
                                    <button
                                        onClick={() => handleEdit(item)}
                                        className="text-blue-600 hover:text-blue-800 mr-3"
                                    >
                                        <Pencil size={18} />
                                    </button>
                                    <button
                                        onClick={() => handleDelete(item.id)}
                                        className="text-red-600 hover:text-red-800"
                                    >
                                        <Trash2 size={18} />
                                    </button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            {showModal && (
                <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
                    <div className="bg-white rounded-lg p-6 w-96">
                        <div className="flex justify-between items-center mb-4">
                            <h3 className="text-lg font-semibold">
                                {editingContent ? 'Editar Contenido' : 'Nuevo Contenido'}
                            </h3>
                            <button onClick={() => setShowModal(false)}>
                                <X size={20} />
                            </button>
                        </div>
                        <form onSubmit={handleSubmit}>
                            <div className="space-y-4">
                                <div>
                                    <label className="block text-sm font-medium text-gray-700">Título</label>
                                    <input
                                        type="text"
                                        value={formData.title}
                                        onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                                        className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-purple-500 focus:ring-purple-500"
                                        required
                                    />
                                </div>
                                <div>
                                    <label className="block text-sm font-medium text-gray-700">Descripción</label>
                                    <textarea
                                        value={formData.description}
                                        onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                                        className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-purple-500 focus:ring-purple-500"
                                        rows={3}
                                        required
                                    />
                                </div>
                                <div>
                                    <label className="block text-sm font-medium text-gray-700">Palabras clave</label>
                                    <input
                                        type="text"
                                        value={formData.keywords}
                                        onChange={(e) => setFormData({ ...formData, keywords: e.target.value })}
                                        className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-purple-500 focus:ring-purple-500"
                                        placeholder="Separadas por comas"
                                        required
                                    />
                                </div>
                                <div>
                                    <label className="block text-sm font-medium text-gray-700">Archivo</label>
                                    <input
                                        type="file"
                                        onChange={handleFileChange}
                                        className="mt-1 block w-full"
                                        accept=".pdf,.doc,.docx,.txt"
                                        required={!editingContent}
                                    />
                                </div>
                            </div>
                            <div className="mt-6 flex justify-end gap-3">
                                <button
                                    type="button"
                                    onClick={() => setShowModal(false)}
                                    className="px-4 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50"
                                >
                                    Cancelar
                                </button>
                                <button
                                    type="submit"
                                    className="px-4 py-2 bg-purple-600 text-white rounded-md hover:bg-purple-700"
                                >
                                    {editingContent ? 'Guardar Cambios' : 'Crear Contenido'}
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            )}
        </div>
    );
}

export default ContentManagement;