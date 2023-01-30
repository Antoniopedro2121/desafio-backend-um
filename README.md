# desafio-backend-um

# descrição

Essa e uma aplicação que ira ler os arquivos canab cadastrar no banco a loja e as transações efetuada nessa loja

# Para rodar o projeto

- Basta istalar as dependencias no ambiente virtual
- exemplo pip install -r requirements.txt
- rodar as migração do banco de dados
- python manage.py migrate
- e por ultimo rodar a api
- python manage.py runserver

# end points da api

base url e o localhost/8000

# nessa rota sera possivel cadastrar os arquivos CANAB

- POST baseUrl/lojas/transacao/

```
canab_arquivo : o arquivo canab
```

- com isso sera cadastrado os dados no bancos de dados da loja e das trasaçoes da loja

# nessa rota sera possivel pegar todas as transações

- get baseUrl/lojas/transacao/

```
sem requisito do body
```

# Para pegar os dados de todas as lojas basta usar a seguinte rota

- GET baseUrl/lojas/

```
sem requisito do body
```

# Para pegar os dados de uma loja basta usar a seguinte rota

- GET baseUrl/lojas/id_da_loja/

```
sem requisito do body
```
