Sobre o Projeto

Este projeto é um sistema de CRUD (Create, Read, Update, Delete) desenvolvido utilizando o framework Django e o banco de dados PostgreSQL. Seu objetivo é gerenciar informações de pessoas de forma simples e eficiente, permitindo a criação, leitura, atualização e exclusão de registros.

Funcionalidades Principais:

	•	Cadastro de Pessoas: Inclui campos como nome, e-mail, telefone e data de nascimento.
	•	Listagem de Pessoas: Exibe uma tabela com os registros cadastrados, permitindo filtragem e ordenação.
	•	Atualização de Registros: Permite a edição de dados existentes de forma intuitiva.
	•	Exclusão de Registros: Facilita a remoção de registros de pessoas do sistema com confirmação de segurança.

Tecnologias Utilizadas:

	•	Django: Framework web robusto e escalável, utilizado para desenvolvimento rápido e seguro.
	•	PostgreSQL: Sistema de gerenciamento de banco de dados relacional, conhecido por sua confiabilidade e desempenho.
	•	HTML/CSS/JavaScript: Para a interface do usuário e funcionalidades interativas.

python -m venv venv
source venv/bin/activate
(venv) pip install django 
or 
(venv) pip install xxxxxx
(venv) django-admin startproject app .
cd app 
(venv) python manage.py runserver (abrir o localhost)

obs: se abrir na url /admin vai aparecer um formulario 
obs2: django esta rodando na porta 8000

(venv) python manage.py migrate (ele ja cria um banco pra mim com uma estrutura basica, com tabelas para controle de sessão, de login, de usuarios)
(venv) python manage.py createsuper user 
name: admin 
email: (optional)
password: XXXXXXXXX
pronto 
na url /admin, entre com seu superuser e administre seu sistema 

python manage.py startapp core (esse comando cria mini aplicações dentro do seu sistema, no caso do "app")

python manage.py makemigrations - cria como o banco de dados deve ser criado la no arquivo migrations/0001_initial.py 

python manage.py migrate  - efetivamente cria o core.0001_initial na aplicação


