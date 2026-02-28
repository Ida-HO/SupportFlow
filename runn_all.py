"""
Script para ejecutar en paralelo la API Flask y la aplicacioón CRUD en consola.
"""
import subprocess
import time
import sys
import os

def run():
    """Inicia la API Flask y la aplicación CRUD."""
    base_dir = os.path.dirname(os.path.abspath(__file__))

    api_path = os.path.join(base_dir, "api", "app.py")

    print("Iniciando API Flask...")
    api_process = subprocess.Popen(
        [sys.executable, api_path],
        cwd=base_dir
    )

    time.sleep(2)

    print("Iniciando aplicación CRUD (consola)...")
    crud_process = subprocess.Popen(
        [sys.executable, "-m", "CrudSistemaTickets.main"],
        cwd=base_dir
    )

    try:
        crud_process.wait()
    except KeyboardInterrupt:
        print("\nCerrando aplicación...")

    api_process.terminate()
    crud_process.terminate()

if __name__ == "__main__":
    run()
