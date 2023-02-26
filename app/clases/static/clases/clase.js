const hostname = window.location.origin

// Variables globales
const clase = document.getElementById('id_clase').value

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
    const respuesta = await fetch(`${hostname}/api/evaluaciones?clase=${clase}`, {
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
    const numero = document.getElementById('id_numero')
    const porcentaje = document.getElementById('id_porcentaje')

    const respuesta = await fetch(`${hostname}/api/evaluaciones`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify({
            numero: numero.value,
            porcentaje: porcentaje.value,
            clase: clase
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

const seccion_a_carta = (seccion) => {
    return `
        <div class="col">
            <div class="card h-100">
                <div class="card-body text-center d-flex justify-content-center align-items-center">
                    ${seccion.nombre_periodo} - ${seccion.nombre_docente}
                    <a href="/clases/${seccion.clase}/${seccion.id}/" class="stretched-link"></a>
                </div>
            </div>
        </div>
    `
}

const obtener_secciones = async () => {
    const respuesta = await fetch(`${hostname}/api/secciones?clase=${clase}`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' }
    })

    if (respuesta.ok) {
        const secciones = document.getElementById('secciones')
        const datos = await respuesta.json()

        // Limpiar el div de secciones
        secciones.innerHTML = ''

        // Agregar una fila para cada sección
        datos.map(seccion => {
            secciones.innerHTML += seccion_a_carta(seccion)
        })
    }
}
obtener_secciones()

document.getElementById('guardar_seccion').addEventListener('click', async () => {
    const id = document.getElementById('id_id')
    const periodo = document.getElementById('id_periodo')
    const docente = document.getElementById('id_docente')

    const respuesta = await fetch(`${hostname}/api/secciones`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify({
            periodo: periodo.value,
            docente: docente.value,
            id: id.value,
            clase: clase,
        })
    })

    if (respuesta.ok) {
        // Limpiar los campos del formulario
        id.value = ''
        periodo.value = ''
        docente.value = ''

        // Volver a obtener las secciones
        obtener_secciones()

        // Cerrar el modal
        bootstrap.Modal.getInstance(document.getElementById('modal_seccion')).hide()
    }
})
