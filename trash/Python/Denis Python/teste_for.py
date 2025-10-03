def encher_caixa():
    # Lista de mensagens para cada nível da caixa d'água.
    
    nivel = 0
    mensagens = [
        "Começando a encher... ",
        "Nível baixo, continue enchendo.",
        "Quase na metade...",
        "Metade da caixa atingida!",
        "Falta pouco para encher...",
        "Caixa cheia! Parando de encher."
    ]
    #loop que simula o enchimento da caixa d'água, do nível 0 ao nível 5
    for nivel in range(6):
        # Exibe o nível atual da água e a mensagem correspondente
        print(f"Nível da água: {nivel} - {mensagens[nivel]}")
        
encher_caixa()