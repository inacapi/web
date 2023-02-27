# Web
Este proyecto permite manejar los datos de inacapi de forma gráfica, de tal
forma que sea más simple de usar y se pueda hacer desde cualquier lugar. Las
siguientes notas serán principalmente para nosotros, ya que no creo que alguien
más use esto.

## Descripción
El programa está diseñado para correr en un servidor, aunque también se puede
usar de forma local. Para contar con https contratamos un dominio. El servidor
Linux en que corra puede ser casi cualquiera, solo hace falta Docker.

## Instalación
Ejecutar el programa es bastante simple cuando ya se tiene el servidor y el
dominio. Esta lista ayuda a seguir cada paso hasta terminar.

- Clonar el repositorio
- Crear .env en base a .env.sample
- Apuntar el dominio o subdominio a el servidor
- Obtener el certificado ssl la primera vez
```
docker compose --file docker-compose-deploy.yml run --rm certbot /opt/certify-init.sh
```
- Conectarse al contenedor de django
```
docker exec -it web-app-1 sh
```
- Aplicar las migraciones
```
python manage.py migrate
```
- Copiar los archivos estáticos
```
python manage.py collectstatic
```
- Crear un usuario admin
```
python manage.py createsuperuser
```
- Crear más usuarios desde el panel admin
- Reinicar los servicios para que nginx use https en adelante
- Renovar el certificado cada 3 meses
```
docker compose --file docker-compose-deploy.yml run --rm certbot certbot renew
```

### Actualizaciones
Solo hay que descargar los nuevos cambios desde github y volver a correr los
servicios con Docker.
