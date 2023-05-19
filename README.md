# proyecto_pruebat

indicaciones de uso:

despues de clonar el repositorio lo primero a realizar es inicializar el servidor: con el comando en el terminal d (py manage.py runserver)

en este punto se puede abrir por el puerto 1234 realizando el py manage.py runserver 1234 (seguido por ese comando) cuando se despliega el servidoer local se encontrará una API/REST en donde se encontrará el formulario con el microservicio requerido, donde al realizar el get, se obtiene en formato json donde se podra ser probado tambien al inicializar el servidor local se puede realizar las operaciones CRUD en el panel de administracion que nos ofrece django, el cual se podra ejecutar al inicializar el servidor seguido del /admin, http ://127.0.0.1:8000/admin/ (en este caso esta por el puerto 8000) en este punto el usuario es: uuario:davidhincapie23 contraseña: pipito1996
en este caso tambien podran crear usuarios con los elementos requeridos en el microservicio

esta API/REST está conectada a una base de datos local mysql en el puerto 3300, donde se puede visualizar la creación de usuarios del microservicio por igual.
este es el servidor local de la api rest cuando se inicializa http://127.0.0.1:8000/empleados//
