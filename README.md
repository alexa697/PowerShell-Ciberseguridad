# PowerShell-Ciberseguridad
¿Qué contiene?

Este repositorio contiene dos scripts desarrollados en PowerShell como parte de actividades prácticas relacionadas con auditoría y automatización en ciberseguridad.

Los scripts permiten revisar información del sistema y generar reportes que ayudan a identificar posibles riesgos o situaciones que requieren revisión.

¿Qué scripts se incluyen?

Actividad12_auditoria_usuarios.ps1
Script que analiza los usuarios locales del sistema y clasifica la información en diferentes grupos dependiendo de su estado.

Actividad13_validar_archivos.ps1
Script que valida si ciertos archivos existen y si pueden ser accedidos, manejando errores en caso de que el archivo no exista o no sea accesible.

¿Qué tareas de ciberseguridad resuelven?

Los scripts ayudan a automatizar tareas básicas de auditoría en un sistema.

El primer script permite identificar usuarios que nunca han iniciado sesión o que están deshabilitados, lo cual puede ser importante para detectar cuentas innecesarias o posibles riesgos de seguridad.

El segundo script permite validar la existencia de archivos importantes del sistema y registrar si hay problemas al acceder a ellos, lo cual puede ayudar a detectar errores o posibles modificaciones en archivos críticos.

¿Qué aprendí al desarrollarlos?

Al desarrollar estos scripts aprendí a usar PowerShell para automatizar revisiones del sistema, manejar errores usando estructuras como try, catch y finally, y generar reportes que pueden servir para auditorías básicas.

También aprendí que en scripting no solo importa el código, sino también cómo se guarda y se ejecuta el archivo. Durante la actividad tuve problemas al guardar el script en Bloc de notas, ya que algunas comillas o formatos provocaban errores al ejecutarlo, por lo que fue necesario revisar la codificación y la forma en que el archivo estaba guardado.

Estas actividades me ayudaron a entender mejor cómo la automatización puede apoyar tareas de ciberseguridad y monitoreo del sistema.
