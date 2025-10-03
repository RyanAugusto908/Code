"""Desenvolva um algoritmo capaz de imprimir na tela Bom dia (0:00 às 11:00), Boa
tarde (12:00 às 17:00) e Boa noite (18:00 às 23:00)."""

def inicio():
    # Que horas são:
    hora = float(input("Digite a hora atual: "))
    print(f"\nSão {hora} horas.")
    # Abreviação de "if hora_atual >= 0 and hora_atual < 12":
    if 0 <= hora < 12:
        print("Bom dia!")
    elif 12 <= hora < 18:
        print("Boa tarde.")
    else:
        print("Boa noite.")

inicio()