marcas = ["Toyota", "Ford", "Honda", "Jeep"]
modelos = {
    "Toyota": ["Corolla", "Camry", "RAV4"],
    "Ford": ["Mustang", "F-150", "Explorer"],
    "Honda": ["Civic", "Accord", "CR-V"],
    "Jeep": ["Wrangler", "Grand Cherokee", "Renegade"]
}

#tabela FIPE
precos_carr = {
    ("Toyota", "Corolla"): 50000,
    ("Toyota", "Camry"): 86000,
    ("Toyota", "RAV4"): 77000,
    ("Ford", "Mustang"): 68000,
    ("Ford", "F-150"): 70000,
    ("Ford", "Explorer"): 59000,
    ("Honda", "Civic"): 49000,
    ("Honda", "Accord"): 97000,
    ("Honda", "CR-V"): 63000,
    ("Jeep", "Wrangler"): 88000,
    ("Jeep", "Grand Cherokee"): 52000,
    ("Jeep", "Renegade"): 61000,
}

#lista de carros disponíveis para aluguel
carros_alugar_disp = [f"{marca} {modelo}" for marca in marcas for modelo in modelos[marca]]
carros_vendidos = []

print("----------- BEM-VINDOS ------------")
nome = input("Informe seu nome: ")
numero = input("Informe seu número de telefone: ")
saldo = float(input("Informe seu saldo: "))
print("--------------------------------------")

#loop principal
while True:
    print("Antes de continuar, observe as opções abaixo:")
    print("1 - Venda de veículo.")
    print("2 - Alugar um veículo.")
    print("3 - Comprar um veículo.")
    print("4 - Sair do programa.")
    
    opcao = int(input("Digite o número para selecionar a alternativa desejada: "))
    
    if opcao < 1 or opcao > 4:
        print("Opção inválida. Por favor, escolha um número entre 1 e 4.")
        continue
    
    print("--------------------------------------")
    
    match opcao:
        case 1:
            print("---------------- Venda de Veículo -----------------")
            #mostra marcas disponíveis
            for i in range(len(marcas)):
                print(f"{i + 1} - {marcas[i]}")
                
            marca_escolhida = int(input("Escolha o número da marca desejada: ")) - 1
            
            if marca_escolhida < 0 or marca_escolhida >= len(marcas):
                print("Escolha inválida. Tente novamente.")
                continue
            
            marca_desej = marcas[marca_escolhida]
            
            #mostra modelos disponíveis da marca escolhida
            print("Modelos disponíveis:")
            for i in range(len(modelos[marca_desej])):
                print(f"{i + 1} - {modelos[marca_desej][i]}")
                
            modelo_selecionado = int(input("Escolha o número do modelo desejado: ")) - 1
            
            if modelo_selecionado < 0 or modelo_selecionado >= len(modelos[marca_desej]):
                print("Escolha inválida. Tente novamente.")
                continue
            
            modelo_desej = modelos[marca_desej][modelo_selecionado]
            
            print(f"Para confirmar: você digitou a marca {marca_desej} e o modelo {modelo_desej}, correto?")
            pergunta = input("Digite sim/não ou s/n para confirmar: ")
            
            if pergunta.lower() in ["sim", "s"]:
                print("Okay! Vamos prosseguir!")
                carro_escolhido = (marca_desej, modelo_desej)
                
                if carro_escolhido in precos_carr:
                    preco_carro = precos_carr[carro_escolhido]
                    desconto = preco_carro * 0.12
                    preco_final = preco_carro - desconto
                    
                    print(f"O valor do carro sem a proposta da empresa: R$ {preco_carro}")
                    print("--------------------------------------------------------------------------")
                    proposta = input(f"A proposta da empresa é de: R$ {preco_final}. Gostaria de fechar negócio? (sim ou não): ")
                    
                    if proposta.strip().lower() == "sim":
                        saldo += preco_final  
                        carros_vendidos.append((marca_desej, modelo_desej, preco_final))
                        #adiciona o carro vendido às opções de aluguel.
                        carros_alugar_disp.append(f"{marca_desej} {modelo_desej}")
                        print(f"A proposta fechada com sucesso! Seu saldo novo é de: R$ {saldo}")
                    else:
                        print("Você decidiu não fechar o negócio.")
                else:
                    print("Este carro e modelo não foram identificados. Por favor, tente novamente!")

        case 2:
            print("---------------- Alugar um veículo -----------------")
            #mostra marcas disponíveis para aluguel
            for i in range(len(marcas)):
                print(f"{i + 1} - {marcas[i]}")
                
            marca_alugar_opcao = int(input("Escolha o número da marca desejada para alugar: ")) - 1
            
            if marca_alugar_opcao < 0 or marca_alugar_opcao >= len(marcas):
                print("Escolha inválida. Tente novamente.")
                continue
            
            marca_alugar_desej = marcas[marca_alugar_opcao]
            
            #mostra modelos disponíveis da marca escolhida para aluguel
            print("Modelos disponíveis:")
            
            modelos_aluguel = modelos[marca_alugar_desej]
            
            #mostra os modelos que estão disponíveis para aluguel
            modelos_disponiveis = [f"{marca_alugar_desej} {modelo}" for modelo in modelos_aluguel if f"{marca_alugar_desej} {modelo}" in carros_alugar_disp]
            
            if not modelos_disponiveis:
                print(f"Não há modelos disponíveis para aluguel na marca {marca_alugar_desej}.")
                continue

            for i in range(len(modelos_disponiveis)):
                print(f"{i + 1} - {modelos_disponiveis[i]}")
                
            modelo_alugar_opcao = int(input("Escolha o número do modelo desejado para alugar: ")) - 1
            
            if modelo_alugar_opcao < len(modelos_disponiveis):
                modelo_alugar_desej = modelos_disponiveis[modelo_alugar_opcao]

                if modelo_alugar_desej in carros_alugar_disp:
                    #mostrando informações sobre o aluguel
                    print(f"O preço do aluguel do {modelo_alugar_desej} é de: R$ 77 por dia.")
                    dias_alugar = int(input("Quantos dias deseja alugar o carro? "))
                    aluguel_a_pagar = dias_alugar * 77
                    
                    print(f"O custo total para alugar o {modelo_alugar_desej} será de R$: {aluguel_a_pagar}. Gostaria de concluir? (sim/s ou não):")
                    pergunta_alugar = input()
                    
                    if pergunta_alugar.lower() in ["sim", "s"]:
                        if saldo >= aluguel_a_pagar:
                            saldo -= aluguel_a_pagar
                            print(f"Parabéns, o cliente {nome} alugou o carro {modelo_alugar_desej} por {dias_alugar} dias. Seu saldo atual é de: R$ {saldo}")
                            
                            #remover o carro alugado da lista disponível
                            carros_alugar_disp.remove(modelo_alugar_desej)

                        else:
                            print("O seu saldo é insuficiente para realizar o aluguel. Tente novamente.")
                    else:
                        print("Você decidiu não alugar o veículo. Retornando ao menu principal.")
                else:
                    print(f"O modelo {modelo_alugar_desej} não está disponível para aluguel.")
            else:
                print("Modelo selecionado inválido. Retornando ao menu principal.")

        case 3:
            print("-------------------- Compra de Veículos ----------------------------")
            #mostra marcas disponíveis para compra
            for i in range(len(marcas)):
                print(f"{i + 1} - {marcas[i]}")
                
            marca_compra_opcao = int(input("Escolha o número da marca desejada para compra: ")) - 1
            
            if marca_compra_opcao < 0 or marca_compra_opcao >= len(marcas):
                print("Escolha inválida. Tente novamente.")
                continue
            
            marca_compra = marcas[marca_compra_opcao]
            
            #mostra modelos disponíveis para compra da marca escolhida
            for i in range(len(modelos[marca_compra])):
                modelo_nome = modelos[marca_compra][i]
                modelo_completo_nome = f"{marca_compra} {modelo_nome}"
                
                #verifica se o modelo está disponível na lista de aluguel antes de exibir
                if modelo_completo_nome in carros_alugar_disp:
                    print(f"{i + 1} - {modelo_nome}")
                
            modelo_compra_opcao = int(input("Escolha o número do modelo desejado para compra: ")) - 1
            
            if modelo_compra_opcao < 0 or modelo_compra_opcao >= len(modelos[marca_compra]):
                print("Escolha inválida. Tente novamente.")
                continue
            
            modelo_compra_nome = modelos[marca_compra][modelo_compra_opcao]
            
            carro_comprar = (marca_compra, modelo_compra_nome)
            
            if carro_comprar in precos_carr:
                preco_compra = precos_carr[carro_comprar]
                acrescimo = preco_compra * 0.25
                valor_final = preco_compra + acrescimo
                
                #mostrando preços original e final com acréscimo
                print(f"O valor original do carro é: R$ {preco_compra}")
                print(f"O valor com acréscimo será: R$ {valor_final}")

                confirmar_compra = input("Gostaria de confirmar a compra? (sim ou não): ")
                
                if confirmar_compra.lower() == "sim":
                    if saldo >= valor_final:
                        saldo -= valor_final
                        print(f"Parabéns!!! O cliente {nome} realizou a compra do carro {carro_comprar}.")
                        print(f"Seu saldo final é de R$ {saldo}")

                        #remover o carro comprado da lista de aluguel, se estiver disponível
                        modelo_comprar_nome = f"{marca_compra} {modelo_compra_nome}"
                        if modelo_comprar_nome in carros_alugar_disp:
                            carros_alugar_disp.remove(modelo_comprar_nome)
                        
                    else:
                        print("Saldo insuficiente para realização da compra.")
                else:
                    print("Você decidiu não comprar o veículo. Retornando ao menu principal.")

        case 4:
            print("Saindo do programa. Obrigado e até logo!")
            break