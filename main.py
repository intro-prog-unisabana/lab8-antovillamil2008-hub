"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file

def main():
    try:
        if len(sys.argv) < 2:
            raise IndexError("Insufficient arguments provided!")
        
        if sys.argv[1] == "--help":
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

        ruta = sys.argv[1]
        tasks = read_todo_file(ruta)

        i = 2
        while i < len(sys.argv):
            comando = sys.argv[i]

            if comando == "view":
                print("Tasks:")
                for t in tasks:
                    print(t)
                i += 1  

            elif comando == "add":

                if i + 1 >= len(sys.argv):
                    raise IndexError('Task description required for "add".')
                
                tarea_nueva = sys.argv[i + 1]
                tasks.append(tarea_nueva)
                print(f'Task "{tarea_nueva}" added.')
                i += 2 

            elif comando == "remove":
                if i + 1 >= len(sys.argv):
                    raise IndexError('Task description required for "remove".')
                
                remover = sys.argv[i + 1]
                if remover in tasks:
                    tasks.remove(remover)
                    print(f'Task "{remover}" removed.')
                else:
                    print(f'Task "{remover}" not found.')

                i += 2  # ← Esto falta
        
            else:
                raise ValueError("Command not found!")
        if len(sys.argv) > 2:
            write_todo_file(ruta, tasks)

    except (IndexError, ValueError) as e:
        print(e)

if __name__ == "__main__":
    main()
