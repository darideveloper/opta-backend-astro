document.addEventListener('DOMContentLoaded', function () {
    // Elementos del DOM
    const tipoLeadToggle = document.getElementById('tipo-lead-toggle');
    const programaSelect = document.getElementById('programa-select');
    const momentoSelect = document.getElementById('momento-select');
    const submomentoSelect = document.getElementById('submomento-select');
    const chatDisplay = document.getElementById('chat-display');
    const historialBtn = document.getElementById('historial-btn');
    const nuevaConversacionBtn = document.getElementById('nueva-conversacion-btn');

    // Validación del DOM
    if (!tipoLeadToggle || !programaSelect || !momentoSelect || !submomentoSelect || !chatDisplay || !historialBtn || !nuevaConversacionBtn) {
        console.error('Algunos elementos no se encontraron en el DOM. Revisa el HTML.');
        return;
    }

    // Evento para el toggle de tipo de lead
    tipoLeadToggle.addEventListener('change', function () {
        const tipoLeadValue = tipoLeadToggle.checked ? 1 : 2; // Asume 1 para New Lead y 2 para Seguimiento
        fetch(`/get-programa/?tipo_lead_id=${tipoLeadValue}`)
            .then(response => {
                if (!response.ok) throw new Error('Error al obtener programas');
                return response.json();
            })
            .then(data => {
                programaSelect.innerHTML = '<option value="">Seleccione un programa</option>';
                data.programas.forEach(programa => {
                    const option = document.createElement('option');
                    option.value = programa.id;
                    option.textContent = programa.nombre;
                    programaSelect.appendChild(option);
                });
                momentoSelect.innerHTML = ''; // Resetea momentos y submomentos
                submomentoSelect.innerHTML = '';
            })
            .catch(error => console.error('Error cargando programas:', error));
    });

    // Evento para la selección de programa
    programaSelect.addEventListener('change', function () {
        const programaId = programaSelect.value;
        if (!programaId) return; // Asegura que un programa está seleccionado
        fetch(`/get-momento/?programa_id=${programaId}`)
            .then(response => {
                if (!response.ok) throw new Error('Error al obtener momentos');
                return response.json();
            })
            .then(data => {
                momentoSelect.innerHTML = '<option value="">Seleccione un momento</option>';
                data.momentos.forEach(momento => {
                    const option = document.createElement('option');
                    option.value = momento.id;
                    option.textContent = momento.nombre;
                    momentoSelect.appendChild(option);
                });
                submomentoSelect.innerHTML = ''; // Resetea submomentos
            })
            .catch(error => console.error('Error cargando momentos:', error));
    });

    // Evento para la selección de momento
    momentoSelect.addEventListener('change', function () {
        const momentoId = momentoSelect.value;
        if (!momentoId) return; // Asegura que un momento está seleccionado
        fetch(`/get-submomento/?momento_id=${momentoId}`)
            .then(response => {
                if (!response.ok) throw new Error('Error al obtener submomentos');
                return response.json();
            })
            .then(data => {
                submomentoSelect.innerHTML = '<option value="">Seleccione un submomento</option>';
                data.submomentos.forEach(submomento => {
                    const option = document.createElement('option');
                    option.value = submomento.id;
                    option.textContent = submomento.nombre;
                    submomentoSelect.appendChild(option);
                });
            })
            .catch(error => console.error('Error cargando submomentos:', error));
    });

    // Botón historial
    historialBtn.addEventListener('click', function () {
        fetch('/get-historial/')
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    // Muestra el historial en el chatDisplay o en un modal
                    console.log('Historial cargado:', data.historial);
                    const historialModal = document.createElement('div');
                    historialModal.className = 'modal';
                    historialModal.innerHTML = `
                        <div class="modal-content">
                            <span class="close-button">&times;</span>
                            <h3>Historial</h3>
                            <ul>
                                ${data.historial.map(item => `<li>${item.contenido}</li>`).join('')}
                            </ul>
                        </div>`;
                    document.body.appendChild(historialModal);
                    const closeButton = historialModal.querySelector('.close-button');
                    closeButton.addEventListener('click', () => historialModal.remove());
                } else {
                    console.error('Error al cargar historial:', data.message);
                }
            })
            .catch(error => console.error('Error cargando historial:', error));
    });

    // Botón nueva conversación
    nuevaConversacionBtn.addEventListener('click', function () {
        fetch('/nueva-conversacion/')
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    chatDisplay.innerHTML = ''; // Limpia el chat
                    alert('Nueva conversación iniciada.');
                } else {
                    alert('Error al iniciar nueva conversación.');
                }
            })
            .catch(error => console.error('Error iniciando nueva conversación:', error));
    });
});
