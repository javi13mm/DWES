from random import randint

opciones = [
    "1. Piedra",
    "2. Papel",
    "3. Tijera"
]
contJ1 = 0
contCPU = 0
while ((contJ1+contCPU) < 5):
    print("\nRONDA "+str(contJ1+contCPU))
    ran = randint(1,3)
    opc = 0
    while (opc != 1) & (opc != 2) & (opc != 3):
        for i2 in range(3):
            print(opciones[i2])
        opc = int(input("Intro opción (1/2/3): "))
    print("\nJ1 jugó: "+opciones[opc-1][3:])
    print("CPU jugó: "+opciones[ran-1][3:])
    if (opc == ran+1) | (opc == 1) & (ran == 3):
        print("Has ganado, "+opciones[opc-1][3:]+" gana a "+opciones[ran-1][3:])
        contJ1 += 1
    elif (opc == ran):
        print("Empate. Se repite la ronda.")
    else:
        print("Has perdido, "+opciones[ran-1][3:]+" gana a "+opciones[opc-1][3:])
        contCPU += 1
print("\nRondas ganadas por J1: "+str(contJ1))
print("Rondas ganadas por CPU: "+str(5-contJ1))
if (contJ1 > 2):
    print("TÚ GANAS! Has ganado más rondas que el rival.")
else:
    print("TÚ PIERDES! Ha ganado más rondas el rival.")

