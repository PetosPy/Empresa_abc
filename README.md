# Empresa_abc

### Este é um aplicativo de processamento de trabalho desenvolvido com Flask, que registra, edita e exclui trabalhadores de um banco de dados Postgresql.
![empresa_abc](https://user-images.githubusercontent.com/64991182/137638345-f45098d9-9c78-42de-8e72-2afa85e60be4.jpeg)



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

## Screenshots
### Adding a worker 
![mick](https://user-images.githubusercontent.com/64991182/137638660-fa96a0aa-cf0e-48fe-a98b-d6c893f135bf.jpeg)

### Worker added
![success](https://user-images.githubusercontent.com/64991182/137638665-b8e96fe1-671f-4bd6-bdae-eeafe4e3706b.jpeg)

### Adding a Lider
![lider](https://user-images.githubusercontent.com/64991182/137638959-776c8557-420f-4f5a-8e2c-b04f9f0dc15a.jpeg)


### Lider added
![lider_success](https://user-images.githubusercontent.com/64991182/137638964-07b349be-9d5c-4628-a9c2-3bdd641946d5.jpeg)
