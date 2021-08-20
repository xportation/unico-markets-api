# Unico Markets API
Teste de avaliação de conhecimentos em REST para a empresa Unico.
## Setup
As dependências da aplicação ficam no arquivo `requirements.txt` e as 
dependências de desenvolvimento no arquivo `requirements-dev.txt`. 
Para apenas rodar a aplicação:
```shell
> pip3 install -r requirements.txt
```
Para apenas rodar a aplicação, testes, relatórios:
```shell
> pip3 install -r requirements-dev.txt
```
As dependências de desenvolvimento já instalam todas as dependências 
inclusive para rodar a aplicação (não precisa instalar os dois nesse caso).
## Rodando a aplicação
Por default está utilizando o database como SQLite e salva no arquivo `storage.db`.  
Para alterar o database basta declarar a url na variável de ambiente `DATABASE_URL`  
  
Criar database: `python cli.py create-database`  
  
Basta rodar diretamente o módulo `main.py`:
```shell
> python3 main.py
```
Este modo é aconselhado apenas para rodar localmente.
Para rodar em produção utilizar o `uvicorn`:
```shell
> uvicorn main:app --log-config log.ini
```
O comando `make runserver` pode ser utilizado para desenvolvimento, 
este utiliza o `uvicorn` com **reload** automático quando identificadas 
alterações nos arquivos.  
## Documentação
A documentação é gerada automaticamente e fica no path `<url>/docs`.  
http://127.0.0.1:8000/docs
## Testes e Qualidade de código
Todos os testes rodam com database em memória.  
 
Comandos:
- Tests: `pytest`
- Lint: `flake8`
- Cobertura: `coverage run -m pytest` e `coverage report -m` para o relatório.
  
No arquivo Makefile é possível verificar as demais opções de relatórios de qualidade e cobertura.

Comandos estão disponíveis via Makefile:  
```shell
> make test
> make coverage
> make quality
```