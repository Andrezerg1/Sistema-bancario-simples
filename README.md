# Sistema Bancário Simples em Python 

Este é um projeto prático desenvolvido para consolidar conhecimentos fundamentais em **Python**, utilizando estruturas de dados (dicionários), funções, manipulação de tipos e controle de fluxo.

O sistema simula as operações básicas de um banco, permitindo a gestão de múltiplas contas em um ambiente de execução local.

## Funcionalidades

O sistema oferece as seguintes operações:

* **Criar Conta:** Registra um novo titular com um número de conta exclusivo.
* **Listar Contas:** Exibe todas as contas cadastradas, seus respectivos titulares e saldos.
* **Depositar:** Adiciona saldo a uma conta existente.
* **Sacar:** Remove saldo de uma conta (com verificação de saldo insuficiente).
* **Transferir:** Realiza a transferência de valores entre duas contas cadastradas.
* **Menu Interativo:** Interface via terminal fácil de usar.

## Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Estrutura de Dados:** Dicionários (`dict`) para armazenamento em memória.

## Estrutura do Código

O projeto é estruturado em funções para manter o código limpo e organizado:

- `criarConta()`: Valida se a conta já existe antes de criar.
- `listarContas()`: Itera sobre o dicionário global para exibir os dados.
- `Deposito()` / `sacar()`: Realiza operações aritméticas básicas de atualização de saldo.
- `transferir()`: Gerencia a lógica de saída de uma conta e entrada em outra.
- `menu()`: O coração do programa que gerencia o loop principal.

## Como executar

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Clone este repositório ou copie o código para um arquivo chamado `sistema_bancario.py`.
3. Abra o terminal ou prompt de comando na pasta do arquivo.
4. Execute o comando:
   ```bash
   python sistema_bancario.py
