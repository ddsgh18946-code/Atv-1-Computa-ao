Este sistema simula a compra de periféricos em uma loja. A lógica segue este fluxo:Boas-vindas: O sistema exibe uma mensagem de recepção e solicita o nome do cliente.Exibição do Menu: Apresenta uma lista de produtos disponíveis (ex: Mouse, Teclado, Monitor) com seus respectivos preços.Entrada de Dados: * O usuário escolhe o produto pelo número (ID).O usuário informa a quantidade desejada.Processamento e Validação:O sistema verifica se a opção escolhida é válida.Calcula o valor total (Preço Unitário $\times$ Quantidade).Verifica se o cliente tem direito a um "Desconto VIP" (por exemplo, se o valor total for acima de R$ 500,00 e a quantidade de itens for maior que 2).Saída (Recibo): Exibe um resumo detalhado com o nome do cliente, produto, quantidade, subtotal, desconto aplicado e o valor final a pagar.

# Sistema de Vendas Simples - Python v1.0

## Descrição
Este projeto é um simulador de sistema de vendas para uma loja de tecnologia, desenvolvido como parte da disciplina de Fundamentos de Programação.

## Requisitos Atendidos
- **Tipos de Dados:** `str`, `int`, `float`, `bool`.
- **Entradas:** Dados do usuário (nome, opção, quantidade).
- **Processamento:** 
  - Estrutura `match/case` para seleção de menu.
  - Operadores matemáticos para cálculo de preço.
  - Operadores lógicos (`and`) e condicionais (`if/elif/else`).
- **Saídas:** Recibo detalhado e mensagens de validação.

## Como Executar
1. Instale o Python (versão 3.10 ou superior).
2. Execute o script através do terminal:
   ```bash
   python app.py
   
Exemplo de Funcionalidade (Bônus)
O sistema aplica automaticamente 10% de desconto se o valor da compra ultrapassar R$ 500,00 e o cliente levar mais de uma unidade.
