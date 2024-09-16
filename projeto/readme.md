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
