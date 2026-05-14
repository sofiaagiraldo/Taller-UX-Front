"""
Orquestador: inicializa el backend y lanza la interfaz gráfica.
Ejecutar desde la raíz del proyecto: python main.py
"""

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from Backend import database  # noqa: E402

from Frontend.gui import run_app  # noqa: E402


def main() -> None:
    database.init_db()
    run_app()


if __name__ == "__main__":
    main()
