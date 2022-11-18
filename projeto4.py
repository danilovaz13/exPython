#projeto numero par ou impar
while True:

    num = int(input("Digite um número: "))
    if num % 2 == 0:
            print("Esse número é par!")
    elif num % 2 == 1:
        print("Esse número é impar!")
    else:     
        print("Digite apenas números")