from time import sleep
n = int(input("Tabuada do: "))

for i in range(11):
    print(f"{n} x {i} = {n * i}")
    sleep(0.5)
    if i in range(5, 12, 5):
        cont = input("Escolha outro número ou digite SAIR para fechar o programa: ")
        if cont == "Sim":
            n = int(input("Escolha um novo número: "))
        elif cont == "SAIR":
            break