import axios from 'axios'
export const getTipoLead = () => {
    return axios.get(`http://127.0.0.1:8000/api/tipolead/`)
}

export const getPrograma = () => {
    return axios.get(`http://127.0.0.1:8000/api/programa/`)
}

export const getMomento = () => {
    return axios.get(`http://127.0.0.1:8000/api/momento/`)
}

export const getSubmomento = () => {
    return axios.get(`http://127.0.0.1:8000/api/submomento/`)
}
export const getRespuesta = () => {
    return axios.get(`http://127.0.0.1:8000/api/respuesta/`)
}
export const getdocumento = () => {
    return axios.get(`http://127.0.0.1:8000/api/documento/`)
}