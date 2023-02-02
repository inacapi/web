const hostname = window.location.origin

async function guardar() {
    const id_estudiante = document.getElementById("id_estudiante").value;
    const id = document.getElementById("id_id")
    const periodo = document.getElementById("id_periodo")
    const respuesta = await fetch(`${hostname}/api/estudiantes/${id_estudiante}/matriculas/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
        },
        body: JSON.stringify({
            id: id.value,
            periodo: periodo.value,
            estudiante: id_estudiante,
        }),
    })
    if (respuesta.ok) {
        bootstrap.Modal.getInstance(document.getElementById("modal")).hide();
        id.value = "";
        periodo.value = "";
        cargar_matricula();
    }
}

async function cargar_matricula() {
    const id_estudiante = document.getElementById("id_estudiante").value;
    const respuesta = await fetch(`${hostname}/api/estudiantes/${id_estudiante}/matriculas/`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    });
    const contenedor_matricula = document.getElementById("matriculas");
    const matriculas = await respuesta.json();
    contenedor_matricula.innerHTML = "";
    contenedor_matricula.innerHTML += `
  <div class="col"> 
    <div class="card">
      <div class="card-body"> 
        <button type="button" class="btn btn-secondary" data-bs-target="#modal" data-bs-toggle="modal">Crear Matricula</button>
      </div>
    </div>
  </div>
  `;
    for (const matricula of matriculas) {
        contenedor_matricula.innerHTML += `
  <div class="col"> 
    <div class="card">
      <div class="card-body"> 
        <a href="/${id_estudiante}/${matricula.periodo}/${matricula.id}" class="stretched-link"></a>
        <h5 class="card-title">${matricula.id} ${matricula.periodo}</h5>
      </div>
    </div>
  </div>
  `;
    }
}
cargar_matricula();

document.getElementById("guardar").addEventListener("click", guardar);
