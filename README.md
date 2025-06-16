# File-Automation
File monitoring and execution based on .txt input / Monitoreo y ejecución según archivos .txt

---

### 🤖  Automatizador de tareas con archivos


# Automatizador de Tareas con Archivos 📂🔁

Script que monitorea una carpeta específica para detectar archivos nuevos, procesarlos y eliminarlos tras su lectura.

## 🧠 Funcionalidad
- Lee archivos `.json` que contienen datos de usuario de un sistema de contro de acceso fisico a instalaciones de un gimnasio
- Ejecuta procesos con los datos leídos
- Elimina el archivo tras el uso
- Inserta Datos en una Base de datos Postgres luego de haber extraido los datos del json y eso datos se usan para iniciar sesion en el sistema desarrollado en django
- Opcional: notificación por consola o log

## 🔧 Tecnologías
- Python
- Watchdog
- OS / Pathlib
- Logging
