// Convierte una evaluación al html correspondiente
const evaluacion_a_fila = (evaluacion) => {
    return `
        <tr>
            <td>${evaluacion.numero}</td>
            <td>${parseFloat(evaluacion.porcentaje) * 100}%</td>
        </tr>
    `
}

// Obtiene las evaluaciones de la clase
const obtener_evaluaciones = async () => {
    const clase = document.getElementById('id_clase').value
    const respuesta = await fetch(`http://localhost:8000/api/clases/${clase}/evaluaciones/`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' }
    })

    if (respuesta.ok) {
        const evaluaciones = document.getElementById('evaluaciones')
        const datos = await respuesta.json()

        // Limpiar el div de evaluaciones
        evaluaciones.innerHTML = ''

        // Agregar una fila para cada evaluación
        datos.map(evaluacion => {
            evaluaciones.innerHTML += evaluacion_a_fila(evaluacion)
        })
    }
}
obtener_evaluaciones()

document.getElementById('guardar_evaluacion').addEventListener('click', async () => {
    const clase = document.getElementById('id_clase')
    const numero = document.getElementById('id_numero')
    const porcentaje = document.getElementById('id_porcentaje')

    const respuesta = await fetch(`http://localhost:8000/api/clases/${clase.value}/evaluaciones/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify({
            numero: numero.value,
            porcentaje: porcentaje.value,
            clase: clase.value
        })
    })

    if (respuesta.ok) {
        // Limpiar los campos del formulario
        numero.value = ''
        porcentaje.value = ''

        // Volver a obtener las clases
        obtener_evaluaciones()

        // Cerrar el modal
        bootstrap.Modal.getInstance(document.getElementById('modal_evaluacion')).hide()
    }
})