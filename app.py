def cadastrar_usuario():
    print("\nCadastro de Usuário")
    usuario['nome'] = input("Digite seu nome: ").strip()
    usuario['email'] = input("Digite seu email: ").strip()
    usuario['telefone'] = input("Digite seu telefone: ").strip()
    print(f"Usuário {usuario['nome']} cadastrado com sucesso!")

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
