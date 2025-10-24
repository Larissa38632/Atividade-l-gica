sala_cinema=[[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0]]
def reservar(fileira,lugar):
    sala_cinema[fileira-1][lugar-1]=1
def cancelar(fileira,lugar):
    if sala_cinema[fileira-1][lugar-1] != 0:
        sala_cinema[fileira-1][lugar-1]=0
    else:
        print("Lugar já disponível para reserva!!!")
def exibir_mapa():
    for i in range(0,len(sala_cinema)):
        print(sala_cinema[i])

print("Olá, Estamos no central de atendimento!")
print("temos os seguintes serviços")
print("1-Reservar assento")
print("2-Cancelar reserva")
print("3-Sair")

opçao=int(input("Escolha uma opção: "))
if opçao==1:
    fileira = int(input("Digite o número da fileira (1 a 5): "))
    lugar = int(input("Digite o número do assento (1 a 8): "))
    if fileira>5 and lugar >8:
        print ("Sem alcançe de lugar")
    else:
        reservar(fileira,lugar)
        exibir_mapa()
elif opçao==2:
    fileira = int(input("Digite o número da fileira (1 a 5):"))
    lugar = int(input("Digite o número do assento(1 a 8):"))
    if fileira>5 and lugar>8:
        print ("Sem alcançe de lugar")
    else:
        cancelar(fileira,lugar)
        exibir_mapa()
elif opçao==3:
    print ("Saindo! Obrigado por ultilizar o sistema!")
else:
    print("Escolha uma opção!!") 
