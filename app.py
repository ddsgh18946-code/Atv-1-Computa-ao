# --- VARIÁVEIS E TIPOS DE DADOS ---
nome_loja = "Python Tech Store"  # str
desconto_fidelidade = 0.10      # float
limite_para_desconto = 500      # int
compra_concluida = False        # bool

# --- ENTRADAS EXTERNAS (USUÁRIO) ---
print(f"--- Bem-vindo à {nome_loja} ---")
cliente = input("Por favor, digite seu nome: ")

# --- MENU INTERATIVO ---
print("\n--- MENU DE PRODUTOS ---")
print("1. Monitor Gamer - R$ 1200.00")
print("2. Teclado Mecânico - R$ 350.00")
print("3. Mouse Wireless - R$ 150.00")
print("4. Sair")

opcao = input("\nSelecione o código do produto: ")

# --- PROCESSAMENTO (SWITCH / MATCH CASE) ---
preco_unitario = 0.0
produto_nome = ""

match opcao:
    case "1":
        produto_nome = "Monitor Gamer"
        preco_unitario = 1200.00
    case "2":
        produto_nome = "Teclado Mecânico"
        preco_unitario = 350.00
    case "3":
        produto_nome = "Mouse Wireless"
        preco_unitario = 150.00
    case "4":
        print("Saindo do sistema... Obrigado!")
    case _:
        print("Opção inválida! Reinicie o programa.")

# --- ESTRUTURAS CONDICIONAIS E OPERADORES ---
if preco_unitario > 0:
    quantidade = int(input(f"Quantas unidades de '{produto_nome}' você deseja? "))
    
    # Operadores Matemáticos
    subtotal = preco_unitario * quantidade
    
    # Operadores Lógicos e Condicionais
    if subtotal >= limite_para_desconto and quantidade > 1:
        print(f"Parabéns {cliente}! Você recebeu 10% de desconto.")
        total_final = subtotal * (1 - desconto_fidelidade)
    elif subtotal > 0:
        total_final = subtotal
    else:
        total_final = 0
        
    compra_concluida = True

    # --- SAÍDA DE DADOS ---
    if compra_concluida:
        print("\n" + "="*30)
        print(f"RECIBO PARA: {cliente.upper()}")
        print(f"PRODUTO: {produto_nome}")
        print(f"TOTAL: R$ {total_final:.2f}")
        print("="*30)
        print("Obrigado pela preferência!")
