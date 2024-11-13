def cadastrar_usuario():
    print("\nCadastro de Usuário")
    usuario['nome'] = input("Digite seu nome: ").strip()
    usuario['email'] = input("Digite seu email: ").strip()
    usuario['telefone'] = input("Digite seu telefone: ").strip()
    print(f"Usuário {usuario['nome']} cadastrado com sucesso!")

#Função para verificar se um input é um número inteiro
def num_inteiro(num):
    while not num.isnumeric():
        num = input('OPÇÃO INVÁLIDA. Digite um número inteiro')
    num = float(num)
    return num

#Função para calcular pacote de energia
def calcular_pacote(tipo_energia, consumo):
    precos_energia = {
    'solar': {
        'preco_kwh': 0.30,
        'consumo_minimo': 20
    },
    'eólica': {
        'preco_kwh': 0.20,
        'consumo_minimo': 40
    },
    'biomassa': {
        'preco_kwh': 0.25,
        'consumo_minimo': 30
    }
    }

    if consumo < precos_energia[tipo_energia]['consumo_minimo']:
        print('Você precisa ter um consumo mínimo mensal de:')
        print('Solar : 20 kWh')
        print('Eólica : 40 kWh')
        print('Biomassa : 30 kWh')
        return None
    else:
        total_pacote = consumo * precos_energia[tipo_energia]['preco_kwh']
        return total_pacote

#Função para fazer consultas de preços de pacotes de energia
def consultar_pacote():
    tipo_energia = input('Escolha qual energia deseja ver:\nSolar, Eólica ou Biomassa ').lower()
    while not tipo_energia in ['solar', 'eólica', 'biomassa']:
        print('Escolha inválida. Digite Solar, Eólica ou Biomassa. ')
        tipo_energia = input('Escolha qual energia deseja ver:\nSolar, Eólica ou Biomassa ').lower()
    consumo = input('Digite o consumo mensal de energia em kWh\nex: 20.0: ')
    consumo = num_inteiro(consumo)
    total_pacote = calcular_pacote(tipo_energia, consumo)

    if total_pacote is None:
        print("O consumo informado não atinge o consumo mínimo necessário para este pacote.")
        return

    print('Resumo do Pacote de Energia Solicitado:')
    print(f'Tipo de Energia: {tipo_energia}')
    print(f'Consumo Mensal: {consumo} kWh')
    print(f'Custo total do pacote: R${total_pacote:.2f}')

#Função para simular o consumo de energia mensal
def simular_consumo():
    tipo_energia = input('Escolha qual energia deseja ver:\nSolar, Eólica ou Biomassa ').lower()
    while not tipo_energia in ['solar', 'eólica', 'biomassa']:
        print('Escolha inválida. Digite Solar, Eólica ou Biomassa. ')
        tipo_energia = input('Escolha qual energia deseja ver:\nSolar, Eólica ou Biomassa ').lower()
    uso_energia = float(input("Digite o uso médio diário de energia em kWh \nex: 15.0): "))
    dias = 30
    for dia in range(dias):
        data = datetime.datetime.now() + datetime.timedelta(days=dia)
        emissao_carbono = calcular_emissao(uso_energia, tipo_energia)

    print(f'Seu consumo mensal será: {uso_energia * dias:.2f} kWh')
    print(f'Você evitará {emissao_carbono:.2f} kg C02')

#Calculando o total de emissão de carbono evitada
def calcular_emissao(consumo, tipo_energia):
    emissao_carbono = consumo * fatores_emissao[tipo_energia]
    return emissao_carbono
    
#Função para fazer o registro diário do consumo, para registro no histórico
def registrar_dados_usuario():
    print("\n--- Registrar dados de energia ---")
    consumo = input("Digite o consumo de energia do dia (kWh): ")
    consumo = num_inteiro(consumo)
    print("Escolha o tipo de energia:")
    print("Solar")
    print("Eólica")
    print("Biomassa")
    tipo_energia = input('').lower()
    while not tipo_energia in ['solar', 'eólica', 'biomassa']:
        print('Escolha inválida. Digite Solar, Eólica ou Biomassa. ')
        tipo_energia = input('Qual a energia? \nSolar, Eólica ou Biomassa ').lower()
    emissao_carbono = calcular_emissao(consumo, tipo_energia)
    data = datetime.datetime.now()
    registro = {
    "data": data.strftime("%Y-%m-%d"),
    "consumo": consumo,
    "emissao_carbono": emissao_carbono
    }
    historico.append(registro)
    print("Dados registrados com sucesso!\n")

#Função para gerar um relatório mensal do consumo e emissão de carbono evitada com base no histórico
def gerar_relatorio():
    if not historico:
        print("Nenhum dado registrado ainda para gerar o relatório.")
        return
    consumo_total = 0
    emissao_total = 0
    for registro in historico:
        consumo_total += registro['consumo']
    for registro in historico:
        emissao_total += registro['emissao_carbono']

    print('Relatório Mensal Energy Green')
    print(f'Consumo Total: {consumo_total:.2f}')
    print(f'Emissão de carbono evitada: {emissao_total:.2f} kg CO2')

#Função Principal
def main():
    cadastrar_usuario()
    while True:
        print('Menu Energy Green (EaaS)')
        print('1 - Consultar Pacote de Energia')
        print('2 - Simulação de Consumo')
        print('3 - Criar Relatório de Consumo e Emissão de Carbono')
        print('4 - Relatório de Emissões de Carbono e Consumo')
        print('5 - Gráfico de Consumo')
        print('0 - Sair')

        opcao = input("Escolha o que deseja visualizar: ")

        if opcao == "1":
            consultar_pacote()
        elif opcao == "2":
            simular_consumo()
        elif opcao == "3":
            registrar_dados_usuario()
        elif opcao == "4":
            gerar_relatorio()
        elif opcao == '5':
            graficos_consumo()
        elif opcao == "0":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("OPÇÃO INVÁLIDA. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
