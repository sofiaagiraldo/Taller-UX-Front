"""Inicialización de SQLite y operaciones de registro."""

import sqlite3
from pathlib import Path

# Ruta del archivo .db junto a este módulo (carpeta Backend)
DB_PATH = Path(__file__).resolve().parent / "taller_ux.db"


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = get_connection()
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS registros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                observacion TEXT,
                creado_en TEXT NOT NULL DEFAULT (datetime('now'))
            )
            """
        )
        conn.commit()
    finally:
        conn.close()


def insert_registro(nombre: str, cantidad: int, observacion: str) -> int:
    conn = get_connection()
    try:
        cur = conn.execute(
            """
            INSERT INTO registros (nombre, cantidad, observacion)
            VALUES (?, ?, ?)
            """,
            (nombre.strip(), cantidad, observacion.strip() or None),
        )
        conn.commit()
        return int(cur.lastrowid)
    finally:
        conn.close()
