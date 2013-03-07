# FLISOL Openspace


Sistema baseado no projeto [Debate Aberto](https://github.com/pr-snas/debateaberto) usado para integrar os vídeos das atividades
do evento, como também inserir interações via chat ou twitter.

## Instalação

1. Faça o checkout do projeto:

``bash
$ git clone git@github.com:gilsondev/flisol-openspace.git
``

2. Crie o ambiente virtual com o ``virtualenv``:

``bash
$ virtualenv --distribute --unzip-setuptools flisol-openspace
``

3. Faça o checkout do Twitter Bootstrap e instale as dependências:

``bash
$ cd flisol-Openspace
$ git submodule init
$ git submodule update

$ source bin/activate
$ pip install -r requirements.txt
``

5. Crie o banco localmente e rode as migrações:

``bash
$ python manage.py syncdb
$ python manage.py migrate
``

## Dependências

1. [Django 1.4.3](https://djangoproject.com)
2. [South](http://south.aeracode.org)
3. [PostgreSQL](http://www.postgresql.org/)
4. [Pip](https://pypi.python.org/pypi/pip)
5. [Virtualenv](https://pypi.python.org/pypi/virtualenv)

Licença: GPL
