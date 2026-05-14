# Taller UX — Autogestión (Python + Tkinter + SQLite)

Aplicación de escritorio con interfaz en **Tkinter**, persistencia en **SQLite** e imagen de cabecera con **Pillow**. Incluye validación de datos, mensajes con **messagebox** y estructura separada en **Backend**, **Frontend** y orquestador **`main.py`**.

---

## Estructura del proyecto

```
Taller-UX-Front/
├── main.py                 # Orquestador: inicializa BD y abre la GUI
├── requirements.txt
├── Backend/
│   ├── database.py        # Conexión SQLite, creación de tablas e inserción
│   └── taller_ux.db       # Base de datos (se crea/actualiza al ejecutar)
├── Frontend/
│   ├── gui.py             # Ventana principal (labels, entries, botones)
│   └── images/
│       └── logo.png       # Logo superior (pueden reemplazarlo)
└── PowerBI/
    └── conexion_powerbi.txt   # Guía para conectar Power BI al .db
```

---

## Requisitos

- **Python 3.10+** (recomendado 3.11 o 3.12)
- Sistema con entorno gráfico (la app abre una ventana de escritorio)

---

## Instalación

Abra una terminal en la **raíz del proyecto** (donde está `main.py`).

### 1. Crear un entorno virtual (recomendado)

En macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

En Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

La dependencia principal es **Pillow**, usada para mostrar el logo en la interfaz.

---

## Cómo ejecutar la aplicación

Desde la raíz del proyecto, con el entorno virtual activado:

```bash
python main.py
```

**Flujo:** `main.py` llama a `Backend.database.init_db()` (crea la tabla si no existe) y luego inicia la ventana definida en `Frontend/gui.py`.

También puede ejecutar solo la interfaz (inicializa la BD antes de abrir la ventana):

```bash
python Frontend/gui.py
```

---

## Uso de la interfaz

| Elemento | Descripción |
|----------|-------------|
| **Nombre del ítem** | Obligatorio. Texto libre. |
| **Cantidad** | Obligatorio. Debe ser un **número entero** ≥ 0. Si no es numérico, verá un mensaje de error. |
| **Observación** | Opcional. Texto multilínea. |
| **Registrar** | Valida los datos y guarda el registro en `Backend/taller_ux.db`. Muestra mensaje de éxito o error. |
| **Limpiar** | Vacía los campos del formulario. |

El logo se carga desde `Frontend/images/logo.png`. Puede sustituir ese archivo por su propio **PNG** o **JPG**; si cambia la extensión a `.jpg`, deberá ajustar la ruta en `Frontend/gui.py` (constante del archivo de imagen).

---

## Base de datos (SQLite)

- **Ubicación:** `Backend/taller_ux.db`
- **Tabla:** `registros`

| Columna       | Tipo    | Notas |
|---------------|---------|--------|
| `id`          | INTEGER | Clave primaria, autoincremental |
| `nombre`      | TEXT    | |
| `cantidad`    | INTEGER | |
| `observacion` | TEXT    | Puede ser NULL |
| `creado_en`   | TEXT    | Fecha/hora por defecto (`datetime('now')`) |

Puede inspeccionar los datos con [DB Browser for SQLite](https://sqlitebrowser.org/) u otra herramienta compatibles.

---

## Power BI

En **Power BI Desktop**: *Obtener datos* → buscar **SQLite** → seleccionar el archivo `Backend/taller_ux.db` → elegir la tabla `registros`.

Pasos más detallados en `PowerBI/conexion_powerbi.txt`. El archivo **.pbix** del informe debe crearse en Power BI y subirse al repositorio si la entrega lo exige.

---

## Problemas frecuentes

| Problema | Qué hacer |
|----------|-----------|
| `No module named 'Pillow'` | Ejecute `pip install -r requirements.txt` dentro del entorno virtual. |
| Error de “externally managed environment” (PEP 668) | Use siempre un **venv** (`python3 -m venv .venv`) e instale ahí; no use `pip` global en el sistema. |
| No aparece el logo | Verifique que exista `Frontend/images/logo.png` y que ejecute desde la raíz o `Frontend/` según la documentación. |
| `No module named 'Backend'` | Ejecute la app con `python main.py` desde la **raíz** del proyecto. |

---

## Entrega sugerida (GitHub)

Incluya en el repositorio, como mínimo:

- Carpeta **Backend** (código + `taller_ux.db`).
- Carpeta **Frontend** (código + carpeta **images** con el logo).
- **main.py** en la raíz.
- Archivo/informe de **Power BI** si la rúbrica lo pide.
- Este **README** para que quien clone el repo pueda instalar y ejecutar sin adivinar pasos.

---

## Reflexión (curso)

> Una aplicación profesional no es aquella que nunca falla, sino aquella que sabe manejar el error con elegancia sin culpar al usuario.

---

*Proyecto académico — Taller UX / Frontend.*
