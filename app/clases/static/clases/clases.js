// Convierte una clase en una carta de bootstrap
const clase_a_carta = (clase) => {
    return `
        <div class="col">
            <div class="card h-100">
                <div class="card-body text-center">
                    ${clase.nombre}
                    <a href="/clases/${clase.id}" class="stretched-link"></a>
                </div>
            </div>
        </div>
    `
}

// Lee las clases con una petición GET
const obtener_clases = async () => {
    const respuesta = await fetch('http://localhost:8000/api/clases/', {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' }
    })

    if (respuesta.ok) {
        const clases = document.getElementById('clases')
        const datos = await respuesta.json()

        // Limpiar el div de clases
        clases.innerHTML = ''

        // Agregar una carta para agregar una clase
        clases.innerHTML += `
            <div class="col">
                <div class="card h-100">
                    <div class="card-body text-center">
                        <button class="btn btn-primary" data-bs-target="#modal" data-bs-toggle="modal">Agregar clase</button>
                    </div>
                </div>
            </div>
        `

        // Agregar una carta para cada clase
        datos.map(clase => {
            clases.innerHTML += clase_a_carta(clase)
        })
    }
}

// Ejecuta la función obtener_clases() al cargar la página
obtener_clases()

// Añade una clase con una petición POST
document.getElementById('guardar').addEventListener('click', async () => {
    const nombre = document.getElementById('id_nombre')
    const semestre = document.getElementById('id_semestre')

    const respuesta = await fetch('http://localhost:8000/api/clases/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify({
            'nombre': nombre.value,
            'semestre': semestre.value
        })
    })

    if (respuesta.ok) {
        // Limpiar los campos del formulario
        nombre.value = ''
        semestre.value = ''

        // Volver a obtener las clases
        obtener_clases()

        // Cerrar el modal
        bootstrap.Modal.getInstance(document.getElementById('modal')).hide()
    }
})