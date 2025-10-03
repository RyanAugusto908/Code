# Myke
#Não precisa ter login.
def inicio():
    
    #Mostrar a minha localização.
    latitude = int(input("\nDigite a sua latitude de 0 a 100: "))
    longitude = int(input("Digite sua longitude de 0 a 100: "))

    #sistema tem que ter horario previsto.
    hora_onibus = [
        "06.00", "07.00", "08.00", "09.00",
        "10.00", "11.00", "12.00", "13.00",
        "14.00", "15.00", "16.00", "17.00",
        "18.00", "19.00", "20.00"
    ]

    # Lista de linhas de ônibus
    linha_onibus = [
        100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
        110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120
    ]

    # Um dicionário onde cada chave é um número de linha de ônibus e o valor é a lista de horários.
    onibus = {linha: hora_onibus for linha in linha_onibus}

    # Solicitar ao usuário o número da linha de ônibus
    linha_desejada = int(input("\nDigite o número da linha de ônibus de 100 até 120: "))
    
    #localização do onibus.
    onibus_local = "\nEstação Diamante"
    print(f"\nO local do onibus é: {onibus_local}")

    # Verificar se a linha existe no dicionário
    if linha_desejada in onibus:
        print(f"\nHorários da linha {linha_desejada}: {onibus[linha_desejada]}")
    else:
        print(f"\nLinha {linha_desejada} não encontrada.")


        #sistema tem que ter horario previsto.
        if latitude + longitude < 50:
            distancia = 30
            print(f"\nO horário de chegada previsto na latitude: {latitude} e longitude: {longitude} é de aproximadamente {distancia} minutos.")
        elif latitude + longitude > 50 and latitude+longitude < 100:
            distancia = 60
            print(f"\nO horário de chegada previsto na latitude: {latitude} e longitude: {longitude} é de aproximadamente {distancia} minutos.")
        else:
            print("\nDistancia muito longa, podera ter atrasos de 10 minutos.\n")
        
inicio()
    
    

