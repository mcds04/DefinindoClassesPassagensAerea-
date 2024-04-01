from passagens import PassagensAereasManager, PassagemAerea
from apresentacao import mostra_menu, menu_compra_passagem, lista_passagens

passagens_aereas_manager = PassagensAereasManager()

while True:
    mostra_menu()
    entrada_do_usuario = int(input())
    
    if entrada_do_usuario == 1:
        origem, destino, preco = menu_compra_passagem()
        passagem = PassagemAerea(origem, destino, preco)
        passagens_aereas_manager.adicionar_passagem(passagem)
        print("==" * 50)
    elif entrada_do_usuario == 2:
        lista_passagens(passagens_aereas_manager.listar_passagens())
        print("==" * 50)
    elif entrada_do_usuario == 3:
        print("Encerrando o programa, volte sempre!")
        break
