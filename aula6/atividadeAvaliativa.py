
class Produto:
    def __init__(self, codigo, nome, descricao, preco, quantidadeEstoque):
        self.codigo = int(codigo)
        self.nome = nome
        self.descricao = descricao
        self.preco = float(preco)
        self.quantidadeEstoque = int(quantidadeEstoque)

    def getCodigo(self):
        return self.codigo

    def getNome(self):
        return self.nome

    def getCategoria(self):
        return self.descricao
    
    def getPreco(self):
        return self.preco

    def getQuantidadeEstoque(self):
        return self.quantidadeEstoque
    
    def setPreco(self, novoPreco):
        self.preco = novoPreco

    def vender(self, quantidadeVendida):
        while True:
            if self.quantidadeEstoque > 0 and quantidadeVendida <= self.quantidadeEstoque:
                self.quantidadeEstoque -= quantidadeVendida
                totalVenda = quantidadeVendida * self.preco
                break
            else:
                print("O produto não está mais disponível ou não tem a quantidade que deseja")

        print(f"\nProduto: {self.nome}")
        print(f"Categoria: {self.descricao}")
        print(f"Quantidade: {quantidadeVendida}")
        print(f"Preço: {self.preco}")
        print(f"Valor total: {totalVenda}")


    def comprar(self, quantidadeComprada):
        self.quantidadeEstoque += quantidadeComprada



produto = Produto(12, "camiseta", "vestuário", 19.90, 7)

produto.getCodigo()
produto.getNome()
produto.getCategoria()
produto.getPreco()
produto.getQuantidadeEstoque()
produto.setPreco(44.50)
produto.vender(5)
produto.comprar(6)
print(produto.quantidadeEstoque)