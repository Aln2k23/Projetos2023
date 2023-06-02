import pyodbc


dados_conexao = ('Driver={SQL Server};'
                 'Server=AlanPc\SQLALAN;' 
                 'Database=NewMetals;')

conexao = pyodbc.connect(dados_conexao)
print('Conexão Efetuada!')
cursor = conexao.cursor()


def last_id():
    lines = query_consult('id','EstoqueNM')
    size_lines = len(lines)
    for roam in lines:
        id = roam[0]

    if size_lines == 0:
        id = 0
        return id
    return id



def query_consult(colunm, table):
    comand_consult_table_sql = f"""
    SELECT {colunm} FROM {table}
    """

    cursor.execute(comand_consult_table_sql)
    row_table = cursor.fetchall()
    return row_table



def query_delet(product, id):
    query = f"""
    delete from EstoqueNM where produto = '{product}' OR id = {id};
    """
    cursor.execute(query)
    cursor.commit()



def query_add(pro, brand, price, qtd, date):
    id = last_id()
    id += 1
    query = f"""INSERT INTO EstoqueNM (id, produto, marca, preco, quantidade, data_compra)
    values ({id},'{pro}','{brand}',{price},{qtd},'{date}');
    """
    print(query)
    cursor.execute(query)

    cursor.commit()



def query_qtd(qtd):
    query = f"""
    select * from EstoqueNM where quantidade = {qtd}
    """
    cursor.execute(query)
    row_table = cursor.fetchall()
    return row_table

