---user--admin: Cbsolo
---password--admin: Clave1234
---conexion--frontend
--- se comento el codigo de historial para que no muestre en admin
--- creacion de serializer y configuracion
--- creacion de requirements.txt python -m pip freeze > requirements.txt

---------Inicio del Proyecto:
El primer objetivo fue arreglar el HTML y CSS del proyecto.
Se trabajó en organizar el código de JavaScript y en conectar el backend de Django con el frontend, buscando que el sistema de chat tuviera historial y pudiera borrar los mensajes en el área del chat.
Complicaciones:
El backend de Django no estaba documentado, lo que requirió estudiar el código línea por línea para poder levantar el proyecto.
Hubo problemas al intentar levantar el backend de Django, lo que llevó a la decisión de reconstruir el backend usando Express.js.
En el frontend, aunque el HTML, CSS y JS funcionaban, el código no estaba modularizado y el CSS estaba desordenado.
Soluciones y lo que se hizo:
Backend en Express.js (descartado):
Objetivo:
Crear un backend funcional para la gestión de usuarios y contraseñas, junto con un sistema de dashboard y conexión a MongoDB Atlas.
Lo que se hizo:
Se implementó un sistema de autenticación con usuarios y contraseñas.
Se creó una plataforma de dashboard donde los usuarios podían ser administradores o subadministradores.
Se permitió que los usuarios pudieran cargar información a una base de datos en MongoDB Atlas y acceder a ella.
Razón del descarte:
Al cliente pedir más especificaciones y querer que el backend original en Django funcionara, se decidió descartar el backend en Express.js.
Backend en Django (finalmente usado):
Objetivo:
Hacer funcionar el backend original en Django, integrándolo con el frontend y cumpliendo con las especificaciones del cliente.
Lo que se hizo:
Se revisaron y ajustaron los archivos clave como urls.py y settings.py para mejorar la conexión y funcionamiento del proyecto.
Se instalaron nuevos módulos para asegurar que el backend pudiera comunicarse correctamente con el frontend.
Se logró que el backend de Django gestionara los datos, incluyendo la autenticación de usuarios y la conexión a la base de datos, manteniendo la funcionalidad que se esperaba del proyecto.
Resultado:
Finalmente, el backend en Django logró integrarse adecuadamente con el frontend y cumplir con los requerimientos del cliente, manteniendo la estructura y las funcionalidades necesarias.
Frontend en React con Vite y TailwindCSS:
Objetivo:
Reestructurar el frontend para hacerlo modular, reutilizable y organizado, mientras se implementaban funcionalidades complejas y requerimientos específicos del cliente.
Lo que se hizo:
Reestructuración del Código:
Modularización: El frontend original, que estaba en HTML, CSS y JS sin modularización, se reestructuró usando React. Esto permitió dividir la interfaz en componentes reutilizables y facilitar el mantenimiento y escalabilidad del código.
Componentes Reutilizables: Se crearon componentes como botones, formularios, y tarjetas que se pueden usar en diferentes partes del proyecto. Esto ahorró tiempo y esfuerzo al no tener que duplicar código.
Estilos con TailwindCSS:
Estilos Dinámicos: TailwindCSS permitió crear estilos rápidos y personalizables, sin necesidad de escribir clases CSS desde cero. Esto resultó en un frontend limpio y mantenible, sin la desorganización de estilos que había al inicio.
Diseño Responsive: Utilizando las clases de TailwindCSS, se aseguró que el diseño fuera completamente responsive, es decir, que se adaptara a diferentes tamaños de pantalla, desde dispositivos móviles hasta desktops.
Personalización: Aunque TailwindCSS es muy flexible, hubo que extenderlo para cubrir algunos estilos específicos del proyecto, ajustando configuraciones en su archivo de configuración para que se ajustara a las necesidades de diseño.
Conexión con Backend (Django):
Fetch/AXIOS: Se implementó la comunicación entre el frontend en React y el backend en Django usando Axios o el método fetch() para realizar solicitudes HTTP. Esto permitió al frontend acceder a los datos del servidor, como la información de usuarios, historial de chats y otros datos importantes.
Manejo de Autenticación: Para la autenticación, se usaron cookies o tokens (como JWT) para mantener las sesiones de usuario y gestionar el acceso a las diferentes funcionalidades del sistema (por ejemplo, dashboard, chat, administración de usuarios).
Gestión del Estado:
Context API o Redux: Para manejar el estado global de la aplicación (como el usuario autenticado, las configuraciones del chat o los datos del dashboard), se implementó React Context API o se usó Redux en caso de que la complejidad del estado lo requiriera. Esto permitió compartir y actualizar el estado entre diferentes componentes de manera eficiente.
Formulario y Validación: Se implementaron formularios con validaciones para el registro de usuarios, login y otros datos importantes, utilizando bibliotecas como Formik y Yup para gestionar la validación de formularios y evitar errores de entrada.
Rutas y Navegación:
React Router: Se utilizó React Router para gestionar la navegación entre diferentes páginas del proyecto, como la página de usuario, el dashboard y el chat. React Router permite una navegación fluida y eficiente sin tener que recargar la página completa.
Protección de Rutas: Algunas rutas, como las del dashboard o panel de administración, solo podían ser accesibles si el usuario estaba autenticado. Esto implicó el uso de rutas protegidas y un sistema de redirección en caso de que el usuario no estuviera logueado.
Interacción en Tiempo Real:
WebSockets: Para el sistema de chat, se implementó WebSockets para manejar la comunicación en tiempo real entre usuarios, lo cual fue clave para mantener la experiencia de usuario fluida, permitiendo la recepción de nuevos mensajes y actualizaciones sin tener que recargar la página.
Manejo de Historial del Chat: El historial del chat se gestionó en el frontend usando state management (Context API o Redux) para mostrar los mensajes previos y permitir que el usuario pudiera ver el historial completo, así como borrar los mensajes si era necesario.
Páginas Adicionales:
Página de Usuario: Se creó una página específica para los usuarios, donde podían ver su perfil, editar información y acceder a su historial de interacciones.
Dashboard: Se diseñó un dashboard para los administradores y subadministradores, donde podían gestionar la información de la plataforma (usuarios, contenido, chat, etc.). Aquí se integraron tablas interactivas y formularios complejos para editar y añadir información.
