# Empresa_abc

### Este é um aplicativo de processamento de dados dos funcionários desenvolvido com Python e Flask, que registra, edita e exclui funcionários de um banco de dados Postgresql de empressa_abc.

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

```

## Screenshots
### Adicionando um funcionario
![mick](https://user-images.githubusercontent.com/64991182/137638660-fa96a0aa-cf0e-48fe-a98b-d6c893f135bf.jpeg)

### funcionario adicionando
![success](https://user-images.githubusercontent.com/64991182/137638665-b8e96fe1-671f-4bd6-bdae-eeafe4e3706b.jpeg)

### Adicionando um Lider
![lider](https://user-images.githubusercontent.com/64991182/137638959-776c8557-420f-4f5a-8e2c-b04f9f0dc15a.jpeg)


### Lider adicionado
![lider_success](https://user-images.githubusercontent.com/64991182/137642287-e27f0b51-9fd3-4d08-8960-8b586c8af835.jpeg)

### Editando a senha do funcionario
![editar_func](https://user-images.githubusercontent.com/64991182/137642605-130b20ff-9959-46d2-a229-6186ef4c3231.jpeg)

### senha do funcionario editado
![func_editado](https://user-images.githubusercontent.com/64991182/137642598-f34ee8dd-33a2-4c4d-800e-f4601419987b.jpeg)

### Excluir funcionario
![delete_func](https://user-images.githubusercontent.com/64991182/137642846-906ab10c-c21e-4824-8e4b-bdd18de55ac6.jpeg)

### Funcionario excluido
![deletado](https://user-images.githubusercontent.com/64991182/137642848-5dc2eee4-f6e3-4bbe-b0f6-e75353dd4de7.jpeg)

## Database
![db_data](https://user-images.githubusercontent.com/64991182/137644029-547c41ea-2b97-4644-ac22-50627cb56c3f.jpeg)






