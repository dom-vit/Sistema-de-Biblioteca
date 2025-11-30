class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.__estoque = self.__Estoque()  # único estoque da biblioteca

    def get_estoque(self):
        return self.__estoque
        
    def mostrar_livros(self):
        self.__estoque.listar_livros()

    class __Estoque:
        def __init__(self):
            self.__estoque = {}

        def listar_livros(self):
            if self.__estoque:
                for titulo, qtd in self.__estoque.items():
                    print(f'Título: {titulo} - {qtd} unidades')
            else:
                print('Nenhum livro no estoque da biblioteca')
            
        def add_books(self, obj, quantidade):
            if isinstance(obj, Livro):
                self.__estoque[obj.titulo] = self.__estoque.get(obj.titulo, 0) + quantidade
            else:
                print("Erro: adicione somente livros cadastrados!")
        
        def remove_books(self, nome, valor):
            if nome not in self.__estoque:
                print(f'Erro: livro com titulo {nome} não encontrado!')
                return
            
            quantidade = self.__estoque[nome]
            if quantidade < valor:
                print(f'Há somente {quantidade} unidades.')
                return
            
            self.__estoque[nome] -= valor
            if self.__estoque[nome] == 0:
                del self.__estoque[nome]
                print(f'Todos os livros "{nome}" foram removidos.')
            else:
                print(f'{nome} removido. {self.__estoque[nome]} restantes.')
        
        def verifica_quantidade(self, pesquisa):
            if pesquisa in self.__estoque:
                print(f'{pesquisa}: {self.__estoque[pesquisa]} unidades')
            else:
                print("Livro não está em estoque")

livro1 = Livro("Era do gelo", "Sheikspare", 2010)
livro3 = Livro("Era do gelo 3", "Sheikspare", 2010)

b1 = Biblioteca('Atenas')

estoque1 = b1.get_estoque()
estoque1.add_books(livro1, 20)
estoque1.add_books(livro3, 20)

estoque1.verifica_quantidade('Era do gelo 3')
