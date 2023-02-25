const hostname = window.location.origin

// Constantes globales
const estudiante = document.getElementById('id_estudiante').value
const periodo = document.getElementById('id_periodo').value
const matricula = document.getElementById('id_matricula').value

// Leer inscripciones
const obtener_inscripciones = async () => {
    const respuesta = await fetch(`${hostname}/api/estudiantes/${estudiante}/${matricula}/inscripciones/`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' }
    })

    if (respuesta.ok) {
        const inscripciones = document.querySelector('#inscripciones')
        const datos = await respuesta.json()

        // Limpiar el div de inscripciones
        inscripciones.innerHTML = ''

        // Añadir una fila para cada inscripción
        datos.map(inscripcion => {
            inscripciones.innerHTML += inscripcion_a_carta(inscripcion)
        })
    }
}

// Leer inscripciones al cargar la página
obtener_inscripciones()

function inscripcion_a_carta(inscripcion) {
    const body = document.createElement('div')
    body.classList.add('card-body')

    // Tabla con los metadatos
    const metadatos = document.createElement('table')
    metadatos.classList.add('table', 'table-borderless', 'table-sm')
    metadatos.innerHTML = `
        <tr>
            <th>Clase</th>
            <td>${inscripcion.clase}</td>
        </tr>
        <tr>
            <th>Docente</th>
            <td>${inscripcion.docente}</td>
        </tr>
    `

    // Tabla con las evaluaciones
    const evaluaciones = document.createElement('table')
    evaluaciones.classList.add('table', 'table-borderless', 'table-sm', 'mb-0')

    evaluaciones.innerHTML = `
        <tr>
            <th>Porcentaje</th>
            <th>Nota</th>
        </tr>
    `

    for (const nota of inscripcion.notas) {
        evaluaciones.innerHTML += `
            <tr>
                <td>${parseFloat(nota.evaluacion__porcentaje) * 100}%</td>
                <td>${nota.nota}</td>
            </tr>
        `
    }

    // Agregar los metadatos y evaluaciones a la carta
    body.appendChild(metadatos)
    body.appendChild(evaluaciones)

    // Agregar el body al resto de la carta
    const col = document.createElement('div')
    col.classList.add('col')
    const card = document.createElement('div')
    card.classList.add('card', 'h-100')
    card.appendChild(body)
    col.appendChild(card)

    // Retornar la carta final
    return col.outerHTML
}
