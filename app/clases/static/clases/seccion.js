const hostname = window.location.origin

// Constantes globales
const clase = document.querySelector('#id_clase').value
const periodo = document.querySelector('#id_periodo').value
const seccion = document.querySelector('#id_seccion').value

// El primer thead son los datos de la sección, el segundo son los datos de las evaluaciones,
// hay que restar 2 porque corresponden a los nombres de cada estudiante
const evaluaciones = document.querySelectorAll('thead > tr')[1].childElementCount - 2

// Leer inscripciones
const obtener_inscripciones = async () => {
    const respuesta = await fetch(`${hostname}/api/clases/${clase}/${seccion}/inscripciones/`, {
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

    const respuesta = await fetch(`${hostname}/api/clases/${clase}/${seccion}/inscripciones/`, {
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
    const respuesta = await fetch(`${hostname}/api/clases/actualizar_notas/`, {
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