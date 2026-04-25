"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""

# TODO: Implementar según README.md
import sys  

try: 
    total_load=int(sys.argv[1])
    num_supports=int(sys.argv[2])
    load_per_support = total_load / num_supports
    print(f"Load per support point: {load_per_support:.2f} N")
        
except ValueError: 
    print("Error: Invalid input! Enter numeric values only.")

except num_supports==0:
    print("Error: Cannot divide by zero! Supports must be greater than zero.")

except total_load==None or num_supports==None:
    print("Error: Invalid input! Enter numeric values only.")
