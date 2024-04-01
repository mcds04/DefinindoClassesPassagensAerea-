class PassagemAerea:
    def __init__(self, origem, destino, preco):
        self.origem = origem
        self.destino = destino
        self.preco = preco

class PassagensAereasManager:
    def __init__(self):
        self.passagens_compradas = []

    def adicionar_passagem(self, passagem):
        self.passagens_compradas.append(passagem)

    def listar_passagens(self):
        for passagem in self.passagens_compradas:
            print(f"Origem: {passagem.origem}, Destino: {passagem.destino}, Preço: {passagem.preco}")
            print("==" * 50)
