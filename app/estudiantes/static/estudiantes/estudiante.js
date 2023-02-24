const hostname = window.location.origin

const obtener_matriculas = async () => {
    const id_estudiante = document.getElementById('id_estudiante').value

    const respuesta = await fetch(`${hostname}/api/estudiantes/${id_estudiante}/matriculas/`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' }
    })

    if (respuesta.ok) {
        const matriculas = document.getElementById('matriculas')
        const datos = await respuesta.json()

        // Limpiar el div de matriculas
        matriculas.innerHTML = ''

        // Agregar una carta para cada matricula
        datos.map(matricula => {
            matriculas.innerHTML += matricula_a_carta(matricula)
        })
    }
}

// Obtiene las matriculas al cargar la página
obtener_matriculas()

// Añade una matricula con una petición POST
document.getElementById('guardar').addEventListener('click', async () => {
    const id_estudiante = document.getElementById('id_estudiante').value
    const id = document.getElementById('id_id')
    const periodo = document.getElementById('id_periodo')

    const respuesta = await fetch(`${hostname}/api/estudiantes/${id_estudiante}/matriculas/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
        body: JSON.stringify({
            id: id.value,
            periodo: periodo.value,
            estudiante: id_estudiante,
        }),
    })

    if (respuesta.ok) {
        // Limpiar los campos del formulario
        id.value = ''
        periodo.value = ''

        // Volver a cargar las matriculas
        obtener_matriculas()

        // Cerrar el modal y actualizar opciones
        document.querySelector(`#id_periodo option[value="${periodo.value}"]`).remove()
        bootstrap.Modal.getInstance(document.getElementById('modal')).hide()
    }
})

function matricula_a_carta(matricula) {
    return `
        <div class="col">
            <div class="card">
                <div class="card-body d-flex align-content-center justify-content-center"> 
                    ${matricula.nombre_periodo}
                    <a href="/${matricula.id}" class="stretched-link"></a>
                </div>
            </div>
        </div>
    `
}