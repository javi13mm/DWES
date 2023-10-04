from random import randint

list_pal = [
    [
        "CASA",
        "AGUA",
        "AZUL"
    ],
    [
        "GARAJE",
        "CABEZA",
        "GUARDIA"
    ],
    [
        "CURIOSIDAD",
        "PARACAIDAS",
        "COAGULACION"
    ]
]

otro = 'S'
while(otro == 'S'):
    nivel = 0
    otro = ' '
    print("\nDIFICULTAD:")
    print("\t1 - Fácil")
    print("\t2 - Normal")
    print("\t3 - Difícil")
    while (nivel < 1) | (nivel > 3):
        nivel = int(input("Introduzca opción (1-3): "))
    
    pal = list_pal[nivel-1][randint(0,2)]
    length = len(pal)

    huecos = []
    for i in range(length):
        huecos.append("_")

    fallos = 0
    aciertos = 0
    acierto = False
    
    while(fallos < 6) & (aciertos != length):
        acierto = False
        print("\nADIVINA LA PALABRA...")
        for i in range(length):
            print(huecos[i], end = " ")
        print()

        letra = ''
        while(not letra.isalpha()):
            letra = input("Introduce una letra: ").upper()
        
        for i in range(length):
            if(letra == pal[i]) & (letra != huecos[i]):
                huecos[i] = letra
                aciertos += 1
                acierto = True
            elif (letra != pal[i]):
                if(i == length-1) & (not acierto):
                    fallos += 1
            elif(letra == huecos[i]):
                acierto = True
        print("Fallos: "+str(fallos))

    if (fallos == 6):
        print("\nHAS PERDIDO!")
    else:
        print("\nHAS GANADO!")
    print("La palabra era: "+pal)

    while(otro != 'S') & (otro != 'N'):
        otro = input("\nJugar de nuevo? (s/n): ").upper()

print("\n\tHASTA OTRA...")
