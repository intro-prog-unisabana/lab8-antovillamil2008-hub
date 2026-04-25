"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file

try: 
    if len(sys.argv)<0:
        raise IndexError("Insufficient arguments provided!")
    
    ruta=sys.argv[1]
    tareas=read_todo_file(ruta)
    if len(sys.argv)>2: 
        c=sys.argv[2]


print("Command-line arguments:")
for arg in sys.argv[1:]:
    print(arg)
print("Tasks")
for t in tareas:
    print(t)


    
