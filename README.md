# Empresa_abc

# Empresa_abc
### Este é um aplicativo de processamento de trabalho desenvolvido com Flask, que registra, edita e exclui trabalhadores de um banco de dados Postgresql.


## Dependências:
* flask, render_template, request, redirect, url_for, flash
* psycopg2 # pip install psycopg2 
* HTML
* little bit of JS and Jquery.

## Instalação

Use o package manager [pip](https://pip.pypa.io/en/stable/) para instalar as dependências. ou use o requirements.txt

```bash
pip install psycopg2
pip install flask

# instalando todas as dependências
pip install -r requiremnts.txt
```

## Crie uma tabela no banco de dados Postgresql com pgAdmin.

```python
CREATE TABLE funcionarios (
    id  IDENTITY,
    nome                 VARCHAR(100)     NOT NULL,
    sobre_nome           VARCHAR(100)     NOT NULL,
    sexo                 VARCHAR(9) 	   , 
    matricula             timestamp  NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id)
);

CREATE TABLE tabela_2 (
	id_funcionario 	int      NOT NULL ,
	cargo             VARCHAR(100)     NOT NULL,
	codigo_do_cargo      VARCHAR(100)     NOT NULL,
	senha   VARCHAR(100)   NOT NULL,
	salario      INT          NOT NULL,
	status_do_colaborador  VARCHAR(100),
    PRIMARY KEY (id_funcionario),
	CONSTRAINT fk_id_funcionario FOREIGN KEY (id_funcionario) REFERENCES funcionarios (id) ON DELETE CASCADE
); 

CREATE TABLE lider (
   id_lider serial,
   nome               VARCHAR(100)     NOT NULL,
   sobre_nome         VARCHAR(100)     NOT NULL,
   sexo      			VARCHAR(9) 		 NOT NULL, 
   cargo             VARCHAR(100)     NOT NULL,
   codigo_do_cargo      VARCHAR(100)     NOT NULL,
   senha   			VARCHAR(100)   NOT NULL,
   salario      		INT          NOT NULL,
   status_do_colaborador  VARCHAR(100),
   matricula_do_lider  timestamp 
); 
```
