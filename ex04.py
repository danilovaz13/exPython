n1 = int(input("Digite um número: "))
if n1 < 0:
    print("Digite um número positivo!!!")
elif n1 >= 0:
    i=0
    fatoracao=0
    while i != n1:
        if n1-i != 0:
            print("Número",i+1," = ",n1-i)
        fatoracao  = fatoracao*(n1-i)
        i = i + 1
        print("O fatorial de",n1,",ou seja,",n1,"!, vale: ",fatoracao)
        
          
    
    
    