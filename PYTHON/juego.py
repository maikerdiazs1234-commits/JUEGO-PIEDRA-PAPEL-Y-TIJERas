import random

print("================================")
print("  JUEGO: PIEDRA, PAPEL O TIJERA")
print("================================")

# Mostrar menú
print("\nSeleccione una opción:")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")

# Entrada del usuario
opcion = int(input("Ingrese su elección (1-3): "))

# Generar elección de la computadora
pc = random.randint(1, 3)

print(f"\nLa computadora eligió: {pc}")

# Proceso (estructura condicional)
if opcion == pc:
    print("Resultado: Empate")
elif (opcion == 1 and pc == 3) or \
     (opcion == 2 and pc == 1) or \
     (opcion == 3 and pc == 2):
    print("Resultado: ¡Ganaste!")
else:
    print("Resultado: Perdiste")

# Cierre
print("\nGracias por jugar.")