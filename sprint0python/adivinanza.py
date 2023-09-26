list_adivin = [
    "Adivina adivinanza, ¿qué tiene el rey en la panza?",
    "a. El ombligo.",
    "b. La corona.",
    "c. Un donut.",
    1
]
print(list_adivin[0]+"\n\t"+list_adivin[1]+"\n\t"+list_adivin[2]+"\n\t"+list_adivin[3])
answer = input("\nEscriba a/b/c: ")
if answer == list_adivin[list_adivin[4]][0]:
    print("\tCORRECTO!")
else:
    print("INCORRECTO!")