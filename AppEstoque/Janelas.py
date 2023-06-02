import PySimpleGUI as sg
from Querys import cursor, query_consult

def table_columns():
    headding = ['ID', 'Produto', 'Marca', 'Preço', 'Qtd', 'Data_Compra']
    return headding


def win_login():
    sg.theme('DarkTeal6') # LightBrown1
    layout_left = [[sg.Push(),sg.Image(filename='imagens\logotipologin.png')]]

    layout_right = [[sg.Text('Chave de entrada',key='teste')],
                    [sg.Input(key='-KEY-', password_char=' ')],
                    [sg.Text('', key='-ALERT_KEY-')],
                    [sg.Button('Entrar'), sg.Button('Fechar'),sg.Button('Esqueci a chave')]]

    layout = [[sg.Column(layout_left),
                    sg.VSeparator(),
                    sg.Column(layout_right)]]

    return sg.Window('Janela de entrada', layout, size=(450,128),element_justification='c', finalize=True)



def win_stock():
    name_columns = 'Todos Itens', 'Consultar', 'Adicionar', 'Excluir'
    sg.theme('DarkTeal6')

    layout = [[sg.Text('Escolha uma opção')],
              [sg.Combo(values=name_columns, s=(15, 22), enable_events=True, key='-ACTIONS-')],
              [sg.Text('       ID       '), sg.Input('', key='-ID_USER-')],
              [sg.Text('   Produto   '), sg.Input('', key='-PROD_DIGIT-')],
              [sg.Text('   Marca    '), sg.Input('', key='-BRAND_DIGIT-')],
              [sg.Text('    Preço    '), sg.Input('', key='-PRICE_DIGIT-')],
              [sg.Text('Quantidade'), sg.Input('', key='-QTD_DIGIT-')],
              [sg.Text('     Data    '), sg.Input('', key='-DATE_DIGIT-')],
              [sg.Text('', key='-ALERT_EST-')],
              [sg.Button('Validar')],
              ]

    return sg.Window('EstoqueNM', layout=layout, element_justification='c', finalize=True)




# Janela da Tabela
def win_table_standard():
    sg.theme('DarkTeal6')

    query = query_consult('*', 'EstoqueNM')
    itens = []

    for item in query:  # Tirar da Lista = Sobrando Tuplas
        linha = [f'{item[0]}'], [f'{item[1]}'], [f'{item[2]}'], [f'{item[3]}'], [f'{item[4]}'], [
            f'{item[5]}']  # Formatando Item
        itens.append(linha)  # Adicionando a formatação em diferentes listas = Linhas

    layout = [[sg.Table(itens, table_columns(), size=(30, 30), enable_click_events=True, col_widths=[3, 12, 12, 7, 5],auto_size_columns=False, )]]

    return sg.Window('Consulta de Estoque New Metals', layout=layout, size=(500, 500), finalize=True)




def win_table_prod_id(prod, id):
    comand = f"""SELECT * FROM EstoqueNM
    WHERE '{prod}' = produto OR id = {id}"""
    cursor.execute(comand)

    row_table = cursor.fetchall()

    itens = []
    for item in row_table:  # Tirar da Lista = Sobrando Tuplas
        linha = [f'{item[0]}'], [f'{item[1]}'], [f'{item[2]}'], [f'{item[3]}'], [f'{item[4]}'], [
            f'{item[5]}']  # Formatando Item
        itens.append(linha)  # Adicionando a formatação em diferentes listas = Linhas

    layout = [[sg.Table(itens, table_columns(), size=(30, 30), enable_click_events=True, col_widths=[3, 12, 12, 7, 5], auto_size_columns=False)]]

    return sg.Window('Estoque New Metals', layout=layout, size=(500, 500), finalize=True)