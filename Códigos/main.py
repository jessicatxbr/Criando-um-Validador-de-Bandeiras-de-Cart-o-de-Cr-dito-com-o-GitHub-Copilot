from card_validator import identificar_bandeira

if __name__ == "__main__":
    numero = input("Digite o número do cartão: ")
    bandeira = identificar_bandeira(numero)
    print(f"Bandeira detectada: {bandeira}")
