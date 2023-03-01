const hostname = window.location.origin

// Constantes globales
const clase = document.querySelector('#id_clase').value
const periodo = document.querySelector('#id_periodo').value
const seccion = document.querySelector('#id_seccion').value

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
// obtener_evaluaciones()

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

// El primer thead son los datos de la sección, el segundo son los datos de las evaluaciones,
// hay que restar 2 porque corresponden a los nombres de cada estudiante
const evaluaciones = document.querySelectorAll('thead > tr')[1].childElementCount - 2

// Leer inscripciones
const obtener_inscripciones = async () => {
    const respuesta = await fetch(`${hostname}/api/inscripciones?seccion=${seccion}`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' }
    })

    if (respuesta.ok) {
        const inscripciones = document.querySelector('#inscripciones')
        const datos = await respuesta.json()

        // Limpiar el div de inscripciones
        inscripciones.innerHTML = ''

        // Añadir una fila para cada inscripción
        datos.map(inscripcion => { inscripciones.innerHTML += inscripcion_a_fila(inscripcion) })
    }
}
obtener_inscripciones()

// Agregar inscripción
document.getElementById('guardar_inscripcion').addEventListener('click', async () => {
    const matricula = document.querySelector('#id_matricula')

    const respuesta = await fetch(`${hostname}/api/inscripciones`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            periodo: periodo,
            seccion: seccion,
            matricula: matricula.value
        })
    })

    if (respuesta.ok) {
        // Eliminar la opción si ya se usa
        document.querySelector(`#id_matricula option[value="${matricula.value}"]`).remove()

        matricula.value = ''

        obtener_inscripciones()

        bootstrap.Modal.getInstance(document.getElementById('modal_inscripcion')).hide()
    }
})

function inscripcion_a_fila(inscripcion) {
    const tr = document.createElement('tr')

    // Atributos fijos
    tr.dataset.id = inscripcion.id
    tr.innerHTML = `<td>${inscripcion.nombre}</td><td>${inscripcion.apellido}</td>`

    // Así rellenamos las celdas de todas las evaluaciones
    while (tr.childElementCount < evaluaciones + 2) tr.innerHTML += '<td></td>'

    // Cada evaluación lleva el número así que usamos eso para determinar dónde debe ir
    for (const nota of inscripcion.notas) tr.children[nota.evaluacion__numero + 1].innerHTML = nota.nota

    return tr.outerHTML
}

// Botón para actualizar las notas
document.querySelector('#actualizar_notas').addEventListener('click', async () => {
    const respuesta = await fetch(`${hostname}/api/actualizar_notas`, {
        method: 'POST',
        body: JSON.stringify({
            seccion: seccion,
        })
    })

    if (!respuesta.ok) {
        alert((await respuesta.json())['mensaje_error'])
        return
    }

    obtener_inscripciones()
})

// Convierte una evaluación al html correspondiente
function evaluacion_a_fila(evaluacion) {
    return `
        <tr>
            <td>${evaluacion.numero}</td>
            <td>${parseFloat(evaluacion.porcentaje) * 100}%</td>
        </tr>
    `
}