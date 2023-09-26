from operaciones import suma, rest, mult, divi
operacion = [
    "S - Suma.",
    "R - Resta.",
    "M - Multiplicación.",
    "D - División."
]
seguir = 's'
while (seguir == 's'):
    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))
    opcion = 0
    for i in range(4):
        print(operacion[i])
    oper = input("Elija operación a realizar: ")
    for i in range(4):
        if oper == operacion[i][0]:
            opcion = i
    if opcion == 0:
        print(suma(num1,num2))
    elif opcion == 1:
        print(rest(num1,num2))
    elif opcion == 2:
        print(mult(num1,num2))
    elif opcion == 3:
        print(divi(num1,num2))
    seguir = ' '
    while (seguir != 'n') & (seguir != 's'):
        seguir = input("\nSeguir? (s/n): ")
