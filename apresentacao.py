def mostra_menu():
    print("Escolha uma da opções abaixo:")
    print("Digite 1 para comprar passagens")
    print("Digite 2 para listar passagens")
    print("Digite 3 para sair do programa")
    print("==" * 50)

def menu_compra_passagem():
    print("Você escolheu comprar de passagens")
    origem = input("Qual é a origem? ")
    destino = input("Qual é o destino? ")
    preco = float(input("Qual é o preço? "))
    return origem, destino, preco

def lista_passagens(passagens_compradas):
    for indice, passagem in enumerate(passagens_compradas):
        print(f"{indice+1}) {passagem}")
        print("==" * 50)
