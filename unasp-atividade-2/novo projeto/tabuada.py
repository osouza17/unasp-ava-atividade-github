while True:
    try:
        num = int(input("Digite um número para ver a tabuada (ou 'sair' para encerrar): "))
        print(f"Tabuada do {num}:")
        for i in range(0, 11):
            print(f"{num} x {i} = {num * i}")
    except ValueError:
        print("Encerrando o programa.")
        break