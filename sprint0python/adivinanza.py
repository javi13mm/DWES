list_adivin = [
    [
        "Adivina adivinanza, ¿qué tiene el rey en la panza?",
        "a. El ombligo.",
        "b. La corona.",
        "c. Un donut.",
        1
    ],
    [
        "Oro parece, plata no es, quien no lo adivine, muy listo no es. ¿Qué es?",
        "a. Plata.",
        "b. Un limón.",
        "c. Un plátano.",
        3
    ],
    [
        "En este banco hay sentados un padre y un hijo. El padre se llama Juan, y el hijo ya te lo he dicho.\n¿Cómo se llama el hijo?",
        "a. Juan.",
        "b. Esteban.",
        "c. Guamedo.",
        2
    ]
]
score = 0
for i in range(3):
    print(list_adivin[i][0]+"\n\t"+list_adivin[i][1]+"\n\t"+list_adivin[i][2]+"\n\t"+list_adivin[i][3])
    answer = input("\nEscriba a/b/c: ")
    if answer == list_adivin[i][list_adivin[i][4]][0]:
        print("\tCORRECTO!")
        score = score + 10
    else:
        print("INCORRECTO!")
        score = score - 5
print("Puntuación: "+str(score))