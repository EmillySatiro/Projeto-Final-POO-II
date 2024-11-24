import json

class Produto:
    def __init__(self, nome: str = None, preco: float = None, data: float = None, hora: float = None,quantidade: int = None) -> None:
        self.nome = nome
        self.preco = preco
        self.data = data
        self.hora = hora
        self.quantidade = quantidade 
        
    def dump(self):
        return json.dumps({
            "nome": self.nome,
            "preco": self.preco,
            "data": self.data,
            "hora": self.hora,
            "quantidade": self.quantidade,
        })
    
    def load(self, data: dict):
        self.nome = data["nome"]
        self.preco = data["preco"]
        self.hora = data["hora"]
        self.data = data["data"]
        self.quantidade = data["quantidade"]

    def __str__(self) -> str:
        return f"{self.nome} - R${self.preco:.2f}"
    
class GerenciarProdutos:
    
    def __init__(self):
        self.produtos = {}
        
    def add_produto(self, produto: Produto, data: float, hora: float, quantidade: int):
        self.produtos[produto.nome] = produto
        self.produtos[produto.data] = data
        self.produtos[produto.hora] = hora
        self.produtos[produto.quantidade] = quantidade
        return True
        
    def listar_produtos(self):
        return [produto for produto in self.produtos.values()]
    
    def comprar_produto(self, nome: str, qtd: int, data: float, hora: float) -> float:
        produto = self.produtos[nome]
        quantidade = self.produtos[quantidade]
        data = self.produtos[data]
        hora = self.produtos[hora]
        return produto.preco * qtd
        
    def dump(self):
        data = {}
        for key, value in self.produtos.items():
            data[key] = value.dump()
        return json.dumps(data)
    
    def load(self, data: dict):
        for key, value in data.items():
            produto = Produto()
            produto.load(json.loads(value))
            self.produtos[key] = produto
            
    def procurar_produto(self, nome: str) -> Produto:
        return nome in self.produtos
  
produtos = {
  1: Produto("Coca-Cola", 5.00),
  2: Produto("Pepsi", 4.00),
  3: Produto("Guaraná", 3.00),
  4: Produto("Fanta", 2.00),
  5: Produto("Sprite", 1.00),
}