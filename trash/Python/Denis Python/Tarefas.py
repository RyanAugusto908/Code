def notas():
    # Tarefa fora do loop para não reinicializar:
    tarefas = []
    
    while True:
        # Adicionar tarefas:
        menu = "\n|1-Adicionar Tarefa|\n|2-Selecionar Tarefa|\n|3-Visualizar Tarefas|\n"
        print(menu)
        entrada = int(input("Selecione: "))
        
        # Adicionar tarefa:
        if entrada == 1:
            # Loop para adicionar várias tarefas.
            while True:
                tarefa = input("Digite uma tarefa ou [Sair] para finalizar: ")
                
                # Saida do loop:
                if tarefa.lower() == "sair":
                    break
                
                # Adiciona tarefa à lista "tarefas":
                tarefas.append(tarefa)

            # Exibir tarefas:   
            print("\nAs tarefas são:")
            for l, c in enumerate(tarefas, start=1):
                print(f"{l}. {c}") 
        
        # Selecionar tarefa:
        elif entrada == 2:
            if not tarefas:
                print("---------------\nNão há tarefas.\n---------------")
            else:
                # Solicita ao usuário que selecione uma tarefa
                while True:
                    try:
                        numero_tarefa = int(input("\nDigite o número da tarefa que deseja selecionar (ou 0 para sair): "))
                        
                        # Verifica se o usuário deseja sair
                        if numero_tarefa == 0:
                            break
                        
                        # Verifica se o número da tarefa está dentro do intervalo válido
                        if 1 <= numero_tarefa <= len(tarefas):
                            tarefa_selecionada = tarefas[numero_tarefa - 1]  # -1 porque a lista começa em 0
                            print(f"Tarefa selecionada: {tarefa_selecionada}")
                            menu2 = int(input("\n|1-Marcar Concluida| |2-Excluir Tarefa|: "))
                            
                            # Marcar concluida:
                            if menu2 == 1:
                                tarefas[numero_tarefa - 1] += " ✅ - Concluída."
                                print(f"Tarefa marcada como concluída: {tarefas[numero_tarefa - 1]}\n")
                            
                            # Remover:
                            elif menu2 == 2:
                                tarefas.remove(tarefa_selecionada)
                                print("Tarefa removida.")
                                print(tarefas)
                            else:
                                print("Tarefa não excluída.")
                        else:
                            print("Número da tarefa inválido. Tente novamente.")
                    except ValueError:
                        print("Por favor, insira um número válido.")
        
        # Visualizar tarefas:
        elif entrada == 3:
            if not tarefas:
                print("---------------\nNão há tarefas.\n---------------")
            else:
                print("\nAs tarefas são:")
                for l, c in enumerate(tarefas, start=1):
                    print(f"{l}. {c}")
        
        # Sair do programa:
        elif entrada == 4:
            print("Saindo do programa.")
            break
        
        #Entrava inválida:
        else:
            print("Opção inválida. Tente novamente.")

notas()