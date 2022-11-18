#Medidor de velocidade
velocidade_maxima = 80
velocidade_motorista = int(input("Qual sua velocidade:"))
if velocidade_motorista <= velocidade_maxima:
        print("Não houve multa!")
elif velocidade_motorista > velocidade_maxima and   velocidade_motorista <= velocidade_maxima + 10:
        print("Levou multa Leve!")
elif velocidade_motorista >= velocidade_maxima + 11 and velocidade_motorista <= velocidade_maxima + 20:
        print("Levou multa grave")
elif velocidade_motorista > velocidade_maxima + 20:
        print("Levou multa gravíssima")  
