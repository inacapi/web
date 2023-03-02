const hostname = window.location.origin

// Constantes globales
const estudiante = document.getElementById('id_estudiante').value
const periodo = document.getElementById('id_periodo').value
const matricula = document.getElementById('id_matricula').value

// Leer inscripciones
const obtener_inscripciones = async () => {
    const respuesta = await fetch(`${hostname}/api/inscripciones?matricula=${matricula}`, {
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
    const metadatos_containder = document.createElement('div')
    metadatos_containder.classList.add('table-responsive')

    const metadatos = document.createElement('table')
    metadatos.classList.add('table', 'table-bordered', 'table-sm', 'text-center')
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

    metadatos_containder.appendChild(metadatos)

    // Tabla con las evaluaciones
    const evaluaciones_container = document.createElement('div')
    evaluaciones_container.classList.add('table-responsive')

    const evaluaciones = document.createElement('table')
    evaluaciones.classList.add('table', 'table-bordered', 'table-sm', 'mb-0', 'text-center')

    evaluaciones.innerHTML = `
        <tr>
            <th>Porcentaje</th>
            <th>Nota</th>
            <th>Promedio</th>
            <th>Fecha</th>
        </tr>
    `

    evaluaciones_container.appendChild(evaluaciones)

    for (const nota of inscripcion.notas) {
        evaluaciones.innerHTML += `
            <tr>
                <td>${parseFloat(nota.evaluacion__porcentaje) * 100}%</td>
                <td>${nota.nota}</td>
                <td>${nota.evaluacion__nota_promedio === null ? '' : nota.evaluacion__nota_promedio}</td>
                <td class="text-nowrap">${nota.evaluacion__fecha === null ? '' : nota.evaluacion__fecha}</td>
            </tr>
        `
    }

    // Agregar los metadatos y evaluaciones a la carta
    body.appendChild(metadatos_containder)
    body.appendChild(evaluaciones_container)

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

// Añadir una inscripción
document.getElementById('guardar_inscripcion').addEventListener('click', async () => {
    const seccion = document.querySelector('#id_seccion')

    const respuesta = await fetch(`${hostname}/api/inscripciones`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            periodo: periodo,
            seccion: seccion.value,
            matricula: matricula
        })
    })

    if (respuesta.ok) {
        // Eliminar todas las secciones de la misma clase
        const nombre_completo = document.querySelector(`#id_seccion option[value="${seccion.value}"]`).innerText
        const nombre_seccion = nombre_completo.split(' - ')[1]
        document.querySelectorAll(`#id_seccion option`).forEach(opcion => {
            if (opcion.innerText.includes(nombre_seccion)) opcion.remove()
        })

        seccion.value = ''

        obtener_inscripciones()

        bootstrap.Modal.getInstance(document.getElementById('modal_inscripcion')).hide()
    }
})

// Botón para actualizar las notas
document.querySelector('#actualizar_notas').addEventListener('click', async () => {
    const respuesta = await fetch(`${hostname}/api/actualizar_notas`, {
        method: 'POST',
        body: JSON.stringify({
            matricula: matricula
        })
    })

    if (!respuesta.ok) {
        alert((await respuesta.json())['mensaje_error'])
        return
    }

    obtener_inscripciones()
})