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
    metadatos.classList.add('table', 'table-bordered', 'table-sm', 'text-center', 'align-middle')
    metadatos.innerHTML = `
        <tr>
            <th>Clase</th>
            <td>${inscripcion.clase}</td>
        </tr>
        <tr>
            <th>Docente</th>
            <td>${inscripcion.docente}</td>
        </tr>
        <tr>
            <th>Asistencia</th>
            <td>${inscripcion.asistencia !== null ? inscripcion.asistencia : ''}</td>
        </tr>
        <tr>
            <th>Promedio</th>
            <td></td>
        </tr>
        <tr>
            <th>Nota final</th>
            <td>${inscripcion.nota_final !== null ? inscripcion.nota_final : ''}</td>
        </tr>
        <tr>
            <th>Nota presentación</th>
            <td>${inscripcion.nota_presentacion !== null ? inscripcion.nota_presentacion : ''}</td>
        </tr>
        <tr>
            <th>Situación</th>
            <td>${inscripcion.situacion !== null ? inscripcion.situacion : ''}</td>
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
            <th>Restante</th>
        </tr>
    `

    evaluaciones_container.appendChild(evaluaciones)

    // Calcular el promedio y el promedio del curso
    let promedio = 0

    for (let i = 0; i < inscripcion.evaluaciones.length; i++) {
        const evaluacion = inscripcion.evaluaciones[i]
        const nota = inscripcion.notas[i] || { nota: '' }

        // Aumentar el promedio
        if (nota.nota !== '') {
            promedio += parseFloat(nota.nota) * parseFloat(evaluacion.porcentaje)
        }

        // Determinar el número de días restantes
        let restante = ''
        if (evaluacion.fecha) {
            const partes = evaluacion.fecha.split('-')
            const fecha = new Date(partes[2], partes[1] - 1, partes[0])
            const diff = Math.ceil((fecha - new Date()) / (1000 * 60 * 60 * 24))

            // Mostrar el número de días restantes o 'Pasó' si ya pasó
            if (diff >= 0) restante = diff
            else restante = 'Pasó'
        }

        evaluaciones.innerHTML += `
            <tr>
                <td>${parseFloat(evaluacion.porcentaje) * 100}%</td>
                <td>${nota.nota}</td>
                <td>${evaluacion.nota_promedio === null ? '' : evaluacion.nota_promedio}</td>
                <td class="text-nowrap">${evaluacion.fecha === null ? '' : evaluacion.fecha}</td>
                <td>${restante}</td>
            </tr>
        `
    }

    // Agregar el promedio y el promedio del curso
    if (promedio > 0) {
        promedio = Number(promedio.toFixed(2))
        metadatos.rows[3].cells[1].innerText = promedio
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