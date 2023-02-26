const hostname = window.location.origin

// Variables globales
const estudiante = document.getElementById('id_estudiante').value

const obtener_matriculas = async () => {
    const respuesta = await fetch(`${hostname}/api/matriculas?estudiante=${estudiante}`, {
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
    const id = document.getElementById('id_id')
    const periodo = document.getElementById('id_periodo')

    const respuesta = await fetch(`${hostname}/api/matriculas`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
        body: JSON.stringify({
            id: id.value,
            periodo: periodo.value,
            estudiante: estudiante,
        }),
    })

    if (respuesta.ok) {
        // Eliminar la matrícula del select
        document.querySelector(`#id_periodo option[value="${periodo.value}"]`).remove()

        // Limpiar los campos del formulario
        id.value = ''
        periodo.value = ''

        // Volver a cargar las matriculas
        obtener_matriculas()

        // Cerrar el modal
        bootstrap.Modal.getInstance(document.getElementById('modal')).hide()
    }
})

function matricula_a_carta(matricula) {
    return `
        <div class="col">
            <div class="card">
                <div class="card-body d-flex align-content-center justify-content-center"> 
                    ${matricula.nombre_periodo}
                    <a href="/${matricula.estudiante}/${matricula.id}/" class="stretched-link"></a>
                </div>
            </div>
        </div>
    `
}