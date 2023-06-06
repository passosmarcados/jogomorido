import random

print("printf")
palavras = ["morte", "destruição", "maria", "claudia", "issoaqehsimples"]
print(palavras)


ondeg = random.choice(palavras)


display=[]

for n in range(len(ondeg)):
        display.append("_")

print(display)

vida=6
cont=0

while vida > 0 and "_" in display:
    chute=input("Digite uma letra:")
    print(chute)
    i = 0 
    acertou = False
    for letra in ondeg:
        if chute == letra:
            display[i] = chute
            acertou = True
        i += 1
    if not acertou:
        vida -= 1
    print(display)
    print(vida)
if vida > 0:
    print("Voce ganhou")


#print(ondeg)

#x=5

# if x%2 == 0:
    # print("par")
# elif x%2==1:
    # print("impar")

# for numero in range()