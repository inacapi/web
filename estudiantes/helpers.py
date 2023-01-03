def iniciar_sesion(request, estudiante):
    request.session['nombre_estudiante'] = estudiante.nombre_estudiante
    request.session['apellido_estudiante'] = estudiante.apellido_estudiante

