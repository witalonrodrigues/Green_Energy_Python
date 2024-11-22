# Green Energy Python - Energy as a Service (EaaS)

## Integrantes
Witalon Antonio Rodrigues - 559023 |
Davis Cardoso de Lima Junior - 560723

## Descrição
Energy Green (EaaS) é uma aplicação em Python que fornece uma solução de **Energy as a Service (EaaS)**, facilitando o acesso a energia renovável e o gerenciamento eficiente do consumo. Esta plataforma permite que usuários acompanhem o consumo de energia, simulem pacotes de energia renovável e analisem as emissões de carbono evitadas, promovendo práticas de consumo mais sustentáveis e ajudando empresas a gerenciar seus custos e impacto ambiental.

1. **Requisitos**
A aplicação utiliza a biblioteca `matplotlib` para gerar gráficos de consumo. Para instalar, utilize o seguinte comando:

```bash
pip install matplotlib
```

2. **Executando o Programa**

- Clone este repositório:
```
git clone https://github.com/seu_usuario/green_energy_python.git
```

- Navegue até a pasta do projeto:
```
cd green_energy_python
```

- Execute o script:
```
python app.py
```

O programa irá iniciar com um menu interativo onde você pode:
    - Cadastrar Usuário
    - Consultar pacotes de energia.
    - Simular consumo e geração.
    - Gerar relatórios de consumo e emissão de carbono.
    - Exibir gráficos de consumo

## Funcionalidades

### Consultar Pacote de Energia
O usuário escolhe o tipo de energia (solar, eólica ou biomassa) e o consumo mensal de energia. O sistema calcula o custo do pacote com base na fonte de energia escolhida.

### Simular Consumo e Geração
Simula o consumo diário de energia para um mês, calculando também a geração de energia com base no tipo escolhido e registrando dados de emissão de carbono evitada.

### Relatório de Emissões de Carbono
Exibe um relatório com os totais de consumo, geração e emissão de carbono evitada para o período registrado.

### Gráficos de Consumo
Exibe gráficos diários de consumo de energia, permitindo visualizar o comportamento do consumo e da geração ao longo do mês.

## Estrutura do Código
- `cadastrar_usuario()`: Registra o usuário no sistema.
- `num_inteiro(num)`: Valida se o valor informado é um número inteiro.
- `calcular_pacote(tipo_energia, consumo)`: Calcula o valor total do pacote de energia baseado no tipo e no consumo do usuário.
- `consultar_pacote()`: Consulta as opções de pacotes de energia.
- `simular_consumo()`: Simula o consumo mensal de energia e calcula as emissões de carbono evitadas.
- `calcular_emissao(consumo, tipo_energia)`: Calcula a emissão de carbono evitada com base no tipo de energia e no consumo.
- `registrar_dados_usuario()`: Registra o consumo diário e as emissões de carbono evitadas.
- `gerar_relatorio()`: Gera um relatório mensal com o consumo total e as emissões evitadas.
- `graficos_consumo()`: Gera gráficos do consumo diário de energia.

## Como Usar
1. Ao iniciar o programa, será solicitado o cadastro do usuário.
2. No menu principal, o usuário pode escolher entre as opções disponíveis:
    - Consultar pacotes de energia.
    - Simular consumo e calcular as emissões de carbono evitadas.
    - Registrar o consumo diário de energia.
    - Gerar um relatório mensal de consumo e emissões.
    - Visualizar gráficos de consumo diário.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

