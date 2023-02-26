const hostname = window.location.origin

const obtener_estudiantes = async () => {
    const respuesta = await fetch(`${hostname}/api/estudiantes`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' }
    })

    if (respuesta.ok) {
        const estudiantes = document.getElementById('estudiantes')
        const datos = await respuesta.json()

        // Limpiar el div de estudiantes
        estudiantes.innerHTML = ''

        // Agregar una carta para cada estudiante
        datos.map(estudiante => {
            estudiantes.innerHTML += estudiante_a_carta(estudiante)
        })
    }

}

// Obtener los estudiantes al cargar la página
obtener_estudiantes()

// Agregar un estudiante con una petición POST
document.getElementById('guardar').addEventListener('click', async () => {
    const nombre = document.getElementById('id_nombre')
    const apellido = document.getElementById('id_apellido')

    const respuesta = await fetch(`${hostname}/api/estudiantes`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify({
            nombre: nombre.value,
            apellido: apellido.value
        })
    })

    if (respuesta.ok) {
        // Limpiar los campos del formulario
        nombre.value = ''
        apellido.value = ''

        // Volver a cargar los estudiantes
        obtener_estudiantes()

        // Cerrar el modal
        bootstrap.Modal.getInstance(document.getElementById('modal')).hide()
    }
})

function estudiante_a_carta(estudiante) {
    return `
        <div class="col">
            <div class="card">
                <div class="card-body text-center d-flex justify-content-center align-items-center"> 
                    ${estudiante.nombre} ${estudiante.apellido}
                    <a href="/${estudiante.id}/" class="stretched-link"></a>
                </div>
            </div>
        </div>
    `
}