Sistema de Gerenciamento de Biblioteca – CRUD de Livros (Python OOP)

Este projeto é um CRUD de Livros utilizando Programação Orientada a Objetos (POO) em Python.
Ele simula o funcionamento básico de uma biblioteca, permitindo:

📌 Cadastro de livros

📌 Controle de estoque

📌 Remoção de itens

📌 Consulta de quantidade

📌 Estrutura com classes, encapsulamento e responsabilidades bem definidas

🧱 Estrutura do Projeto

O projeto é composto por três partes principais:

1. Classe Livro

Representa um livro individual.

Atributos:

titulo

autor

ano

2. Classe Biblioteca

Representa uma biblioteca e contém um estoque interno.

Métodos principais:

get_estoque() – retorna uma instância do estoque

mostrar_livros() – lista livros cadastrados

3. Classe interna __Estoque

Controla os livros disponíveis.

Responsável por:

add_books() – adicionar itens ao estoque

remove_books() – remover itens

listar_livros() – listar catálogo

verifica_quantidade() – consultar quantidade

▶️ Como usar
Criar livros
livro1 = Livro("Era do gelo", "Sheikspare", 2010)
livro2 = Livro("Era do gelo 2", "Sheikspare", 2011)

Criar bibliotecas
b1 = Biblioteca("Atenas")
b2 = Biblioteca("Sophi")

Acessar o estoque
estoque = b1.get_estoque()

Adicionar livros
estoque.add_books(livro1, 10)
estoque.add_books(livro2, 5)

Listar livros
estoque.listar_livros()

Verificar quantidade
estoque.verifica_quantidade("Era do gelo")

🏗️ Conceitos de POO Aplicados

Este projeto demonstra:

Encapsulamento (uso de atributos privados __)

Classes internas

Responsabilidade única (SRP)
Estoque é isolado da biblioteca.

Abstração
Usuário não interage diretamente com o dicionário interno.

Modularidade
Cada classe tem uma função clara.

🐛 Possíveis Melhorias Futuras

Persistência dos dados (JSON/SQLite)

Interface CLI ou GUI

API REST com Flask ou Django

Testes unitários com pytest

Controle de usuários (administrador/cliente)

Tratamento de erros mais robusto

📄 Licença

Este projeto é livre para uso educacional.
Sinta-se à vontade para modificar e evoluir o sistema.
