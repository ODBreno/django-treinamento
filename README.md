# EVENTEX

Sistema de Eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env.
6. Execute os testes.

```console
git clone git@github.com:ODBreno/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage,py test
```


## Como fazer o deploy?

1. Crie uma instância nop heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura.
4. Defina DEBUG=False.
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heorku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# Configuro o email
git push heroku master --force
 ```