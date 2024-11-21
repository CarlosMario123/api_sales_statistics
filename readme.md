# Configuraciones iniciales

## Instalacion de dependencias

```bash
pip install -r requirements.txt
```
Nota usar un entorno virtual de python
## ¿Como ejecutar migraciones?

| **Comando**               | **Descripción**                                                       |
|---------------------------|-----------------------------------------------------------------------|
| `flask db init`           | Inicializa el sistema de migraciones.                                |
| `flask db migrate -m "msg"` | Genera un script de migración basado en los modelos definidos.       |
| `flask db upgrade`        | Aplica las migraciones pendientes a la base de datos.               |
| `flask db downgrade`      | Revierte la última migración aplicada.                              |
| `flask db current`        | Muestra la versión actual de la base de datos (última migración).   |

