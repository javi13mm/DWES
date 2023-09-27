import random

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
list_order = [0,1,2]
score = 0
ran = random.sample(list_order,2)
for i in range(2):
    print(list_adivin[ran[i]][0]+"\n\t"+list_adivin[ran[i]][1]+"\n\t"+list_adivin[ran[i]][2]+"\n\t"+list_adivin[ran[i]][3])
    answer = input("\nEscriba a/b/c: ")
    if answer == list_adivin[ran[i]][list_adivin[ran[i]][4]][0]:
        print("\tCORRECTO!")
        score = score + 10
    else:
        print("\tINCORRECTO!")
        score = score - 5
print("Puntuación: "+str(score)+"\n")