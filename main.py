"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file

try: 
    nombre=(sys.argv[1])
    ruta=(sys.argv[2])
    print("")
except IndexError:
    print("Insufficient arguments provided!")