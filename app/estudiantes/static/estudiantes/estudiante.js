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
    document.querySelector(`#id_periodo option[value="${periodo.value}"]`).remove();
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
  for (const matricula of matriculas) {
    contenedor_matricula.innerHTML += `
  <div class="col"> 
    <div class="card">
      <div class="card-body d-flex align-content-center justify-content-center"> 
        ${matricula.nombre_periodo}
        <a href="/${id_estudiante}/${matricula.periodo}/${matricula.id}" class="stretched-link"></a>
      </div>
    </div>
  </div>
  `;
  }
}
cargar_matricula();

document.getElementById("guardar").addEventListener("click", guardar);
