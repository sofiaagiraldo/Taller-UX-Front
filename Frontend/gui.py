"""Pantalla principal del reto: formulario con Tkinter, Pillow y validación."""

from __future__ import annotations

import sqlite3
import sys
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

from PIL import Image, ImageTk

# Raíz del proyecto (padre de la carpeta Frontend)
_ROOT = Path(__file__).resolve().parent.parent
_LOGO_PATH = Path(__file__).resolve().parent / "images" / "logo.png"

# Import tardío del backend para mantener orden de arranque desde main
def _backend():
    root_backend = _ROOT / "Backend"
    if str(root_backend) not in sys.path:
        sys.path.insert(0, str(_ROOT))
    from Backend import database as db

    return db


def run_app() -> None:
    db = _backend()

    root = tk.Tk()
    root.title("Autogestión — Registro")
    root.minsize(420, 480)
    root.configure(padx=16, pady=16)

    # --- Logo superior (Pillow + ImageTk) ---
    logo_frame = ttk.Frame(root)
    logo_frame.pack(fill=tk.X, pady=(0, 12))

    try:
        img = Image.open(_LOGO_PATH)
        # Ancho máximo razonable para el encabezado
        max_w = 280
        if img.width > max_w:
            ratio = max_w / img.width
            img = img.resize(
                (max_w, int(img.height * ratio)), Image.Resampling.LANCZOS
            )
        logo_photo = ImageTk.PhotoImage(img)
        lbl_logo = ttk.Label(logo_frame, image=logo_photo)
        lbl_logo.image = logo_photo  # evitar garbage collection
        lbl_logo.pack()
    except OSError:
        ttk.Label(
            logo_frame,
            text="(Coloque logo.png en Frontend/images/)",
            foreground="gray",
        ).pack()

    ttk.Label(root, text="Registro de ítems", font=("Helvetica", 14, "bold")).pack(
        pady=(0, 8)
    )

    form = ttk.Frame(root, padding=8)
    form.pack(fill=tk.BOTH, expand=True)

    ttk.Label(form, text="Nombre del ítem:").grid(row=0, column=0, sticky=tk.W, pady=4)
    entry_nombre = ttk.Entry(form, width=40)
    entry_nombre.grid(row=0, column=1, sticky=tk.EW, pady=4)

    ttk.Label(form, text="Cantidad:").grid(row=1, column=0, sticky=tk.W, pady=4)
    entry_cantidad = ttk.Entry(form, width=40)
    entry_cantidad.grid(row=1, column=1, sticky=tk.EW, pady=4)

    ttk.Label(form, text="Observación (opcional):").grid(
        row=2, column=0, sticky=tk.NW, pady=4
    )
    txt_obs = tk.Text(form, width=40, height=4, wrap=tk.WORD)
    txt_obs.grid(row=2, column=1, sticky=tk.EW, pady=4)

    form.columnconfigure(1, weight=1)

    def limpiar() -> None:
        entry_nombre.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)
        txt_obs.delete("1.0", tk.END)

    def registrar() -> None:
        try:
            nombre = entry_nombre.get()
            cantidad_raw = entry_cantidad.get().strip()
            observacion = txt_obs.get("1.0", tk.END)

            if not nombre.strip():
                messagebox.showerror("Validación", "El nombre es obligatorio.")
                return

            try:
                cantidad = int(cantidad_raw)
            except ValueError:
                messagebox.showerror(
                    "Validación",
                    "La cantidad debe ser un número entero.",
                )
                return

            if cantidad < 0:
                messagebox.showerror(
                    "Validación",
                    "La cantidad no puede ser negativa.",
                )
                return

            nuevo_id = db.insert_registro(nombre, cantidad, observacion)
            messagebox.showinfo(
                "Éxito",
                f"Registro guardado correctamente.\nID asignado: {nuevo_id}",
            )
            limpiar()
        except sqlite3.Error as e:
            messagebox.showerror(
                "Base de datos",
                f"No se pudo guardar el registro:\n{e}",
            )
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Ocurrió un error inesperado:\n{e}",
            )

    btn_frame = ttk.Frame(root)
    btn_frame.pack(fill=tk.X, pady=(12, 0))

    ttk.Button(btn_frame, text="Registrar", command=registrar).pack(
        side=tk.LEFT, padx=(0, 8)
    )
    ttk.Button(btn_frame, text="Limpiar", command=limpiar).pack(side=tk.LEFT)

    root.mainloop()


if __name__ == "__main__":
    _backend().init_db()
    run_app()
