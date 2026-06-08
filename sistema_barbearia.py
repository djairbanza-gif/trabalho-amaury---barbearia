# Sistema de Gestão de Barbearia

clientes = []
servicos_realizados = 0
clientes_atendidos = 0
valor_faturado = 0

while True:
    print("\n===== BARBEARIA =====")
    print("1 - Adicionar cliente")
    print("2 - Chamar próximo cliente")
    print("3 - Mostrar fila")
    print("4 - Encerrar sistema")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do cliente: ")

        quantidade = int(input("Quantos serviços serão realizados? "))

        servicos = []
        total = 0

        for i in range(quantidade):
            nome_servico = input(f"Nome do serviço {i + 1}: ")
            preco = float(input("Preço do serviço: R$ "))

            servicos.append((nome_servico, preco))
            total += preco

        clientes.append({
            "nome": nome,
            "servicos": servicos,
            "total": total
        })

        print("Cliente adicionado à fila!")

    elif opcao == "2":
        if len(clientes) == 0:
            print("Não há clientes na fila.")
        else:
            cliente = clientes.pop(0)

            print("\nCliente atendido:", cliente["nome"])
            print("Serviços:")

            for servico, preco in cliente["servicos"]:
                print(f"- {servico}: R$ {preco:.2f}")

            print(f"Total: R$ {cliente['total']:.2f}")

            clientes_atendidos += 1
            servicos_realizados += len(cliente["servicos"])
            valor_faturado += cliente["total"]

    elif opcao == "3":
        if len(clientes) == 0:
            print("Fila vazia.")
        else:
            print("\nFila de clientes:")
            for i, cliente in enumerate(clientes, start=1):
                print(f"{i} - {cliente['nome']}")

    elif opcao == "4":
        print("\n===== RELATÓRIO FINAL =====")
        print(f"Quantidade de serviços: {servicos_realizados}")
        print(f"Clientes atendidos: {clientes_atendidos}")
        print(f"Valor faturado: R$ {valor_faturado:.2f}")
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida!")
