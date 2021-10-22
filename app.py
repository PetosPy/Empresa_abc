from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2 
import psycopg2.extras
from datetime import datetime
 

app = Flask(__name__)

app.secret_key = "ghwtsgshbj2s2h2bdsweghd"
 
HOST = "localhost"
DATABASE = "empresa_abc"
USER = "postgres"
PASSWORD = "tempo290"


# Conectando-se ao banco de dados
connection = psycopg2.connect(dbname=DATABASE, user=USER, password=PASSWORD, host=HOST)


@app.route('/')
def Index():

    # criando o cursor
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
 
    # Selecione todos os dados das duas tabelas usando INNER_JOIN e exiba-os na página.
    user = """SELECT funcionarios.id, funcionarios.nome, funcionarios.sobre_nome, funcionarios.sexo, funcionarios.matricula, 
            tabela_2.senha, tabela_2.salario, tabela_2.cargo, tabela_2.codigo_do_cargo, tabela_2.status_do_colaborador
            FROM funcionarios INNER JOIN tabela_2 ON funcionarios.id = tabela_2.id_funcionario;
            """
    cursor.execute(user) # Execute the SQL
    list_users = cursor.fetchall()

    return render_template('index.html', list_users = list_users)
   

 
@app.route('/add_employee', methods=['POST'])
def add_employee():
    # Adicionar o funcionario

    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        if  len(request.form['nome']) != 0 and len(request.form['sobre_nome']) != 0 and len(request.form['sexo']) != 0 and len(request.form['salario']) != 0:
            if request.form.get("funcionario"):

                # Tabela dos funcionarios
                nome = request.form['nome']
                sobre_nome = request.form['sobre_nome']
                sexo = request.form['sexo']

                #Tabela_2
                senha = request.form['senha']
                salario = request.form['salario']
                cargo = request.form['cargo']
                codigo_do_cargo = request.form['codigo_do_cargo']
                status_do_colaborador = request.form['status_do_colaborador']
                
                # Insira dados na tabela dos funcionarios
                cursor.execute("INSERT INTO funcionarios (nome, sobre_nome, sexo) VALUES (%s,%s,%s) RETURNING id", (nome, sobre_nome, sexo))
                id_funcionario = cursor.fetchone()[0]

                # Insira dados na tabela_2 baseado no "id" dos funcionarios
                cursor.execute("INSERT INTO tabela_2 (id_funcionario, senha, salario, cargo, codigo_do_cargo, status_do_colaborador) VALUES (%s, %s, %s, %s, %s, %s)", (id_funcionario, senha, salario, cargo, codigo_do_cargo, status_do_colaborador))
                connection.commit()
                
                flash('Funcionário adicionado com sucesso')

                return redirect(url_for('Index'))

            else:
                if  len(request.form['nome']) != 0 and len(request.form['sobre_nome']) != 0 and len(request.form['sexo']) != 0 and len(request.form['salario']) != 0:
                    
                    # Dados do Lider
                    if request.form.get("lider"):

                        # Tabela dos funcionarios
                        nome = request.form['nome']
                        sobre_nome = request.form['sobre_nome']
                        sexo = request.form['sexo']

                        #Tabela_2
                        senha = request.form['senha']
                        salario = request.form['salario']
                        cargo = request.form['cargo']
                        codigo_do_cargo = request.form['codigo_do_cargo']
                        status_do_colaborador = request.form['status_do_colaborador']

                        # Insira dados na tabela_2 baseado no "id" dos funcionarios   
                        cursor.execute("INSERT INTO funcionarios (nome, sobre_nome, sexo) VALUES (%s,%s,%s) RETURNING id", (f"{nome} (Lider-{cargo})", sobre_nome, sexo))
                        id_funcionario = cursor.fetchone()[0]
                        cursor.execute("INSERT INTO tabela_2 (id_funcionario, senha, salario, cargo, codigo_do_cargo, status_do_colaborador) VALUES (%s, %s, %s, %s, %s, %s)", (id_funcionario, senha, salario, cargo, codigo_do_cargo, status_do_colaborador))
                        connection.commit()

                        flash(f'Lider: {nome} {sobre_nome} adicionado com sucesso')

                        return redirect(url_for('Index'))
        else:
            flash("Por favor insira informações completas")

            return redirect(url_for('Index'))


 
@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_employee(id):
    # Editar os dados do funcionario

    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    sql = "SELECT funcionarios.id, funcionarios.nome, funcionarios.sobre_nome, funcionarios.sexo, tabela_2.senha, tabela_2.cargo, tabela_2.codigo_do_cargo, tabela_2.status_do_colaborador FROM funcionarios INNER JOIN tabela_2 ON funcionarios.id = tabela_2.id_funcionario"
    cursor.execute(f'{sql} WHERE id = {("%s")}', (id))
    data = cursor.fetchall()
    cursor.close()
    # print(data[0])

    return render_template('edit.html', funcionario = data[0])
 

@app.route('/update/<id>', methods=['POST'])
def update_employee(id):

    # Dados atualizados do funcionario
    if request.method == 'POST':
        nome = request.form['nome']
        sobre_nome = request.form['sobre_nome']
        sexo = request.form['sexo']
        senha = request.form['senha']
        cargo = request.form['cargo']
        codigo_do_cargo = request.form['codigo_do_cargo']
        status_do_colaborador = request.form['status_do_colaborador']
         
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("""
            UPDATE funcionarios 
            SET nome = %s,
                sobre_nome = %s,
                sexo = %s
            WHERE id = %s """,
            (nome, sobre_nome, sexo, id))

        cursor.execute("""
            UPDATE tabela_2 
            SET senha = %s,
                cargo = %s,
                codigo_do_cargo = %s,
                status_do_colaborador = %s
            WHERE tabela_2.id_funcionario = %s """, 
            (senha, cargo, codigo_do_cargo, status_do_colaborador, id))

        flash('Dados do funcionário atualizados com sucesso')
        connection.commit()

        return redirect(url_for('Index'))

 
@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_employee(id):
    # Deletar funcionario

    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(f'DELETE FROM funcionarios WHERE id = {id}')
    connection.commit()
    flash('Funcionário removido com sucesso')
    return redirect(url_for('Index'))


@app.route('/about')
def about():

    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)




####### Extra code ########

# def reset_id(cursor):
#     cursor.execute("ALTER SEQUENCE funcionarios_id_seq RESTART WITH 1")
#     print("Id reset complete")
 
# SELECT * FROM funcionarios 
# INNER JOIN tabela_2 
# ON funcionarios.id = tabela_2.id_funcionario


# Delete FROM funcionarios
# ALTER SEQUENCE funcionarios_id_seq RESTART WITH 1

# SELECT * FROM funcionarios