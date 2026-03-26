m = []
n = int(input("Adicione um número à lista: "))
m.append(n)
print(m)

for n in m:
    cont = input("Deseja adicionar outro número?")
    if cont == "SIM":
        n = int(input("Digite outro número: "))
        m.append(n)
        print(m)
        continue
    elif cont == "NAO":
        break