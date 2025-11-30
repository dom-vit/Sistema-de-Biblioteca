📚 CRUD de Biblioteca em Python

Este projeto é um CRUD simples de gerenciamento de livros usando Programação Orientada a Objetos (POO) em Python. Ele simula o funcionamento de uma biblioteca, com classes para Livro, Biblioteca e um controlador interno de estoque.

🚀 Funcionalidades

Adicionar livros ao estoque

Remover livros do estoque

Listar livros disponíveis

Consultar quantidade de um título específico

Criar múltiplas bibliotecas com estoques independentes

🧱 Estrutura do Projeto

O projeto utiliza três classes principais:

📘 Livro

Representa um livro com título, autor e ano.

🏛 Biblioteca

Representa uma biblioteca. Cada instância pode criar e acessar seu próprio estoque.

📦 Estoque (classe interna)

Controla o estoque de livros, armazenando quantidades, listando e permitindo alterações.

A classe __Estoque é privada dentro da classe Biblioteca, reforçando encapsulamento.

🛠 Tecnologias usadas

Python 3

Programação Orientada a Objetos (POO)

🧩 Melhorias Futuras

Persistência de dados (JSON, SQLite ou CSV)

Interface de linha de comando (CLI)

Interface gráfica simples (Tkinter)

API com Flask ou FastAPI
