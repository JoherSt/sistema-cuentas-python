# D.Software

Repositorio de proyectos de práctica desarrollados en Python y PHP, organizados por módulos y paquetes.

---

## Proyectos

### Python

| Proyecto | Descripción | Archivo principal |
|----------|-------------|-------------------|
| `cajero` | Sistema de cajero automático con registro de operaciones bancarias | `cajero/main.py` |
| `biblioteca` | Gestión de libros en una biblioteca | `biblioteca/main.py` |
| `calculadora_operaciones` | Calculadora con operaciones e inventario | `calculadora_operaciones/menu.py` |
| `furbolistas_agendar` | Agenda de jugadores de fútbol | `furbolistas_agendar/menu.py` |
| `gestion_estudiante` | Registro y gestión de estudiantes | `gestion_estudiante/main.py` |
| `Hotel` | Sistema de gestión hotelera | `Hotel/main.py` |
| `inicio_sesion` | Sistema de autenticación de usuarios | `inicio_sesion/main.py` |
| `inventario_celulares` | Inventario de celulares | `inventario_celulares/main.py` |
| `Inventario_equipos` | Inventario y gestión de equipos | `Inventario_equipos/menu.py` |
| `notas_estudiantes` | Registro de notas de estudiantes | `notas_estudiantes/main.py` |
| `ventas_equipos` | Sistema de ventas y préstamo de equipos | `ventas_equipos/model.py` |

### PHP

| Proyecto | Descripción |
|----------|-------------|
| `Php` | Aplicación web con PHP — gestión de usuarios, tareas, categorías y comentarios con base de datos |

### Módulos y prácticas

| Carpeta | Contenido |
|---------|-----------|
| `modulo/Modulo.py` | Ejercicios de manejo de archivos (leer, escribir TXT, CSV, pandas) y expresiones regulares |
| `B.Datos` | Bases de datos de práctica (SQLite, Northwind) |

---

## Estructura general

```
D.Software/
├── cajero/
├── biblioteca/
├── calculadora_operaciones/
├── furbolistas_agendar/
├── gestion_estudiante/
├── Hotel/
├── inicio_sesion/
├── inventario_celulares/
├── Inventario_equipos/
├── notas_estudiantes/
├── ventas_equipos/
├── Php/
├── modulo/
└── B.Datos/
```

Cada proyecto sigue la misma estructura:
```
proyecto/
├── main.py (o menu.py)
└── paquete/
    ├── __init__.py
    ├── datos.py
    └── utils.py
```

---

## Cómo ejecutar un proyecto

```bash
# Entrar a la carpeta del proyecto
cd gestion_estudiante

# Ejecutar el archivo principal
python main.py
```

---

## Tecnologías usadas

- Python 3.14
- PHP 8
- SQLite
- Pandas

---

## Autor

**Joher Franco** — [github.com/JoherSt](https://github.com/JoherSt)
## Correo
joherstivenfrancoa@gmail.com
