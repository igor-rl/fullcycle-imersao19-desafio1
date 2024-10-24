![header-igor-projetos](https://github.com/igor-rl/assets/blob/main/img/github-projetcs-header.jpg)

![header-igor-projetos](https://events-fullcycle.s3.amazonaws.com/events-fullcycle/media/images/a06b6a97db354487b1ee6bee9ef9f123.svg)

# DESAFIO 1 - DJANGO

### Criando um pequeno blog com Django

Neste desafio, você deverá criar uma aplicação Django que simule um pequeno blog.
Teremos uma listagem de blogs em nosso blog.

Você deverá criar um app do Django com o nome core e os seguintes models:
- Post
  
  Dados: title, content, created_at, tags (um post tem uma ou várias tags e uma tag pode ter um ou vários posts)


- Tag

  Dados: name

Estes 2 models devem estar plugados no admin do Django.

Crie uma página com o path /blog e liste todos os posts e tags da aplicação.

Faça tudo com SQLite3 e acrescente no controle de versão com Git.

Precisa já ter cadastrado um usuário no admin com as seguintes credenciais: admin para o username, admin para a senha.

Envie a URL do seu repositório.

Bons estudos!

# Comandos para Inicializar a aplicação
Instale as dependências:
```bash
pipenv install
```

Acessar o ambiente virtual do Pipenv:
```bash
pipenv shell
```

Inicialize a aplicação:
```bash
python manage.py runserver
```

Agora é só acessar a aplicação em [localhost:8000](http://127.0.0.1:8000).

Link para acessar a listagem dos Posts e tags: [localhost:8000](http://127.0.0.1:8000/blog)

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-Igor_Lage-blue?style=social&logo=github)](https://github.com/igor-rl) 

![Static Badge](https://img.shields.io/badge/24--10--2024-black)


</div>