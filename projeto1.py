#Fatorrial de um número
#crie um programa que recebe um número e imprime o su faotiral.

num = int(input('Digit um número: '))
if num > 0:
    fatorial = 1
    for item in range(1,num +1):
        fatorial = fatorial * item
print(fatorial)
        
        