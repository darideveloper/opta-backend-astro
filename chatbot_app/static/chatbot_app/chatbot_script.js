"use strict";

document.addEventListener("DOMContentLoaded", () => {
    const toggleInput = document.getElementById("tipo-lead-toggle");
    const leadDisplay = document.getElementById("lead-type-display");
    const programaSelect = document.getElementById("programa-select");
    const momentoSelect = document.getElementById("momento-select");
    const submomentoSelect = document.getElementById("submomento-select");
    const historialButton = document.getElementById("historial");
    const nuevaConversacionButton = document.getElementById("nueva-conversacion");
    const historialModal = document.getElementById("historialModal");
    const closeModal = document.querySelector(".close");


    fetch(`/api/get-tipo-lead/?tipo=New Lead`)
        .then(response => response.json())
        .then(data => console.log("Tipo de lead cargado:", data));
    // fetch("/api/tipo-lead/") // Asegúrate de usar la URL exacta
    //     .then(response => {
    //         if (!response.ok) throw new Error("Error al obtener tipo de lead");
    //         return response.json();
    //     })
    //     .then(data => console.log("Tipo de lead cargado:", data))
    //     .catch(error => console.error(error));
    // Toggle Lead Type
    toggleInput.addEventListener("change", () => {
        leadDisplay.textContent = toggleInput.checked ? "Seguimiento" : "New Lead";
        fetch(`/api/get-tipo-lead/?tipo=${leadDisplay.textContent}`)
            .then(response => response.json())
            .then(data => console.log("Tipo de lead cargado:", data));
    });

    // Cargar programas
    console.log(toggleInput.checked)
    fetch("/api/get-programa/?tipo_lead_id=1")
        .then(response => response.json())
        .then(data => {
            data.programas.forEach(prog => {
                const option = document.createElement("option");
                option.value = prog.id;
                option.textContent = prog.nombre;
                programaSelect.appendChild(option);
            });
        });

    // Cargar momentos
    document.getElementById('programa-select').addEventListener('change', function () {
        fetch("/api/get-momento/?programa_id=1")
            .then(response => response.json())
            .then(data => {
                const modal = false;
                document.getElementById("momentos-section").style.display = "block";
                const momentoSelect = document.getElementById("momento-select");
                data.momentos.forEach(momento => {
                    const option = document.createElement("button");
                    option.classList.add("moment-button");
                    option.dataset.moment = momento.nombre;
                    option.value = momento.id;
                    option.textContent = momento.nombre;
                    option.onclick = submoments;
                    console.log(option)
                    momentoSelect.appendChild(option);
                });
            });
    });


    const submoments = () => {
        fetch("/api/get-submomento/?momento_id=1")
            .then(response => response.json())
            .then(data => {
                document.getElementById("submomentos-section").style.display = "block";
                const submomentoSelect = document.getElementById("submoments-container");
                data.submomentos.forEach(submomento => {
                    const option = document.createElement("div");
                    option.classList.add("submoment-tag");
                    option.value = submomento.id;
                    option.textContent = submomento.nombre;
                    console.log(option)
                    submomentoSelect.appendChild(option);
                });
            });
    }

    document.getElementById('tipo-lead-toggle').addEventListener('change', function () {
        const tipoLeadId = this.checked ? 2 : 1; // Suponiendo que 1 es "New Lead" y 2 es "Seguimiento"
        fetch(`/api/get-programa/?tipo_lead_id=${tipoLeadId}`)
            .then(response => {
                if (!response.ok) throw new Error('Error al obtener programas');
                return response.json();
            })
            .then(data => {
                const programaSelect = document.getElementById('programa-select');
                programaSelect.innerHTML = '<option value="">Seleccione un programa</option>';
                data.programas.forEach(programa => {
                    const option = document.createElement('option');
                    option.value = programa.id;
                    option.textContent = programa.nombre;
                    programaSelect.appendChild(option);
                });
            })
            .catch(error => console.error('Error cargando programas:', error));
    });

    document.getElementById('nueva-conversacion-btn').addEventListener('click', function () {
        const modal = document.getElementById('nuevaConversacionModal');
        modal.style.display = 'block';
    });

    document.getElementById('closeNuevaConversacion').addEventListener('click', function () {
        const modal = document.getElementById('nuevaConversacionModal');
        modal.style.display = 'none';
    });

    document.getElementById('historial-btn').addEventListener('click', function () {
        document.getElementById('historialSidebar').classList.add('show');
    });

    document.getElementById('closeHistorial').addEventListener('click', function () {
        document.getElementById('historialSidebar').classList.remove('show');
    });

    //http://127.0.0.1:8000/get-momento/?programa_id=5   

    // Modal Historial
    historialButton.addEventListener("click", () => {
        historialModal.style.display = "flex";
    });

    closeModal.addEventListener("click", () => {
        historialModal.style.display = "none";
    });

    nuevaConversacionButton.addEventListener("click", () => {
        console.log("Nueva conversación iniciada.");
    });
});
