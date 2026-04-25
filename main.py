"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file

try: 
    if len(sys.argv)<0:
        raise IndexError("Insufficient arguments provided!")
    
    ruta=sys.argv[1]
    tareas=read_todo_file(ruta)
    if ruta=="--help":
        print("""Usage: python main.py <file_path> <command> [arguments]...
Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.""")
        
        print("Command-line arguments:")
    for arg in sys.argv[1:]:
        print(arg)
        print("\nTasks:")
        for t in tareas:
            print(t)
    
    tareas=
    if len(sys.argv)>2: 
        c=sys.argv[2]
        if c=="view":
            print("Tasks:")
            for t in tareas:
                print(t)
        


print("Command-line arguments:")
for arg in sys.argv[1:]:
    print(arg)
print("Tasks")
for t in tareas:
    print(t)


    
