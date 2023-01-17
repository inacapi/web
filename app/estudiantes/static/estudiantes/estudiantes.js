async  function guardar() {
  const nombre = document.getElementById("id_nombre")
  const apellido = document.getElementById("id_apellido")
  await fetch("http://localhost:8000/api/estudiantes/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
    },
    body: JSON.stringify({
      nombre: nombre.value,
      apellido: apellido.value,
    }),
  })
  bootstrap.Modal.getInstance(document.getElementById("modal")).hide();
  nombre.value = "";
  apellido.value = "";
  cargar_estudiantes();
}

async function cargar_estudiantes() {
  const respuesta = await fetch("http://localhost:8000/api/estudiantes/", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  const contenedor_estudiantes = document.getElementById("estudiantes");

  const estudiantes = await respuesta.json();
  contenedor_estudiantes.innerHTML = "";
  contenedor_estudiantes.innerHTML += `
  <div class="col"> 
    <div class="card">
      <div class="card-body"> 
        <button type="button" class="btn btn-secondary" data-bs-target="#modal" data-bs-toggle="modal">Crear estudiante </button>
      </div>
    </div>
  </div>
  `;
  for (const estudiante of estudiantes) {
    contenedor_estudiantes.innerHTML += `
  <div class="col"> 
    <div class="card">
      <div class="card-body"> 
        <a href="/${estudiante.id}" class="stretched-link"></a>
        <h5 class="card-title">${estudiante.nombre} ${estudiante.apellido}</h5>
      </div>
    </div>
  </div>
  `;
  }
}
cargar_estudiantes();

document.getElementById("guardar").addEventListener("click", guardar);
