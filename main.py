"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file
def main():
    try: 
        if len(sys.argv)<0:
            raise IndexError("Insufficient arguments provided!")
        if sys.argv[1]=="--help":
             print("""Usage: python main.py <file_path> <command> [arguments]...
Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.
Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")
             return
        ruta=sys.argv[1]
        tasks=read_todo_file(ruta)
        contador=2
        while contador<len(sys.argv):
            comando=sys.argv[contador]

            if comando=="view":
                print("Tasks:")
                for t in tasks:
                    print(t)
                contador+=1
            elif comando=="add":
                if contador+1>=len(sys.argv):
                    raise IndexError("Task description required for "add".")
                tarea_nueava=sys.argv[contador+1]
                tasks.append(tarea_nueava)
                print(f'Task "{tarea_nueava}" added.')
                contador += 2
            elif comando == "remove":
                if contador + 1 >= len(sys.argv):
                    raise IndexError('Task description required for "remove".')
                remover=sys.argv[contador+1]
                if remover in tasks:
                 tasks.remove(remover)
                 print(f"Task {remover} removed.")
                else:
                 print(f'Task "{remover}" not found.')
                contador += 2
            else:
                raise ValueError("Command not found!")
        if len(sys.argv)>2:
             write_todo_file(ruta, tasks)
    
    except (IndexError, ValueError) as e:
        print(e)


if __name__ == "__main__":
    main()
    