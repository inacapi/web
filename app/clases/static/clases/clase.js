const hostname = window.location.origin

// Variables globales
const clase = document.getElementById('id_clase').value

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
