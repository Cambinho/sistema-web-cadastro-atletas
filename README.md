🏅 Sistema de Cadastro de Atletas

Este projeto é um sistema web de cadastro e gerenciamento de atletas desenvolvido em Python com Flask, utilizando arquitetura baseada em MVC (Model-View-Controller), integração com banco de dados PostgreSQL e API REST.

O sistema permite o cadastro de atletas com upload de imagens, autenticação de administrador e gerenciamento dos registros através de uma interface web.

🚀 Funcionalidades

Login de administrador
Cadastro de atletas
Upload de imagem do atleta
Listagem de atletas
Exclusão de atletas
API REST para consulta e cadastro
Interface web com HTML, CSS e JavaScript
Integração com banco de dados PostgreSQL

🛠️ Tecnologias utilizadas

Python
Flask
Flask-SQLAlchemy
PostgreSQL
HTML
CSS
JavaScript
Programação Orientada a Objetos (POO)
Arquitetura MVC
Git e GitHub

📂 Estrutura do projeto

projeto_guiado/
│
├── app.py
├── data/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
└── requirements.txt

O projeto segue uma arquitetura baseada em MVC:

Models → Estrutura dos dados e integração com o banco (SQLAlchemy)
Views → Páginas HTML (interface do usuário)
Controllers → Rotas Flask e regras de negócio
Static → Arquivos CSS, JavaScript e imagens

▶️ Como executar o projeto

1. Instalar o Python 3
2. Clonar este repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
3. Acessar a pasta do projeto
cd seu-repositorio
4. Instalar as dependências
pip install -r requirements.txt
5. Criar o banco de dados PostgreSQL

No PostgreSQL, execute:

CREATE DATABASE olimpiadas;
6. Configurar a conexão com o banco no arquivo app.py
postgresql://postgres:SUA_SENHA@localhost:5432/olimpiadas
7. Executar o sistema
python app.py
8. Acessar no navegador
http://127.0.0.1:5000

🔐 Acesso ao sistema

Usuário	Senha
admin	123

📌 API Endpoints

Método	Rota	Descrição
GET	/api/atletas	Lista atletas
POST	/api/atletas	Cadastra atleta
DELETE	/api/atletas/	Remove atleta

👨‍💻 Autor

Carlos Alberto Martins Baltazar
Estudante de Ciência de Dados | Desenvolvedor Python

📌 Observações

Este projeto foi desenvolvido para fins de estudo e prática de desenvolvimento web, banco de dados, API REST e arquitetura de software utilizando Flask.
