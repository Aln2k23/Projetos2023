import PySimpleGUI as sg
from Janelas import win_login, win_stock, win_table_standard, win_table_prod_id
from Querys import query_consult, query_add, query_delet

# Chave de entrada = m0use99



def control_price(choice_price):
    try:
        choice_price = choice_price.replace(',','.')
        choice_price = float(choice_price)
        return choice_price
    except:
        return False



def control_qtd(qtd):
    try:
        qtd = int(qtd)
        return qtd
    except:
        return False


def alert_vazio():
    janela_2['-ALERT_EST-'].update('')


def alert_error(reply):
    janela_2['-ALERT_EST-'].update(reply)



try: # Tenta rodar o programa, qualquer erro ira ativar uma mensgem
    janela_1, janela_2, janela_stan, janela_produ = win_login(), None, None, None
    while True:
        windows, events, values = sg.read_all_windows() # Looping, leitura das janelas



        # ABRIR E FECHAR Janela--===---===---===---===

        if windows == janela_1 and events == 'Fechar' or windows == janela_1 and events == sg.WIN_CLOSED: # LOGIN
            break

        if windows == janela_2 and events == 'Fechar' or windows == janela_2 and events == sg.WIN_CLOSED: # SISTEMA TABELA
            break
        
        if windows == janela_stan and events == sg.WIN_CLOSED: # TABELA
            janela_stan.hide()
            
        if windows == janela_produ and events == sg.WIN_CLOSED:
            janela_produ.hide()


        if windows == janela_1 and events == 'Esqueci a chave':
            sg.popup_ok('E-mail para suporte: guimera.sistem@gmail.com')


        # ENTRANDO NA JANELA ESTOQUE--===---===---===---===

        if windows == janela_1 and events == 'Entrar':
            key_digit = values['-KEY-'] # Chave digitada pelo usuário
            line_key = query_consult('*', 'SenhaADM') # Senha de Ativação do Banco de Dados

            for palavraKey in line_key:
                for letraKey in palavraKey:
                    letraKey = letraKey # Chave de Ativação buscada do Banco de Dados

            if key_digit == letraKey:
                janela_1['-ALERT_KEY-'].update('')
                janela_2 = win_stock() # Abrir Janela do Estoque
                janela_1.hide() # Esconder Janela_1
            else:
                janela_1['-ALERT_KEY-'].update('A senha está errada!')
        



    # DADOS DE VALIDAÇÕES--===---===---===---===

        if windows == janela_2 and events == 'Validar':
            actions_user = values['-ACTIONS-'] # Caixa de COMBO
            len_actions_user = len(actions_user)


            # Usuário Digitou   
            id_choice = values['-ID_USER-']
            product_choice = values['-PROD_DIGIT-']
            product_choice = product_choice.lower()
            brand_choice = values['-BRAND_DIGIT-']
            price_choice = values['-PRICE_DIGIT-']
            qtd_choice = values['-QTD_DIGIT-']
            date_choice = values['-DATE_DIGIT-']
            len_id = len(id_choice)
            if len_id == 0:
                        id_choice = 0


            if len_actions_user == 0:
                alert_error('Escolha uma opção')



            # Ver todos itens disponiveis (sem ordem)--===---===---===---===

            elif actions_user == 'Todos Itens':
                alert_vazio()
                janela_stan = win_table_standard() 



            # Consultar Produto por NOME ou ID--===---===---===---===

            elif actions_user == 'Consultar':
                if product_choice or id_choice:
                    alert_vazio()
                    janela_produ = win_table_prod_id(product_choice,id_choice)
                    
                else:
                    alert_error('Escolha o Produto pelo nome ou ID')

           
            # Adicionar ITEM--===---===---===---===

            elif actions_user == 'Adicionar':
                if id_choice == 0:
                    if product_choice:
                        if len(product_choice) <= 20:
                            if brand_choice:
                                if len(brand_choice) <= 20:

                                    if price_choice:
                                        price_choice = control_price(price_choice)

                                        if price_choice != False:
                                            if qtd_choice:
                                                qtd_choice = control_qtd(qtd_choice)

                                                if qtd_choice != False:
                                                    if date_choice:
                                                        if len(date_choice) == 10:
                                                            try:
                                                                alert_vazio()
                                                                print(product_choice,brand_choice,price_choice,qtd_choice,date_choice)
                                                                query_add(product_choice,brand_choice,price_choice,qtd_choice,date_choice)
                                                                sg.popup_timed('Produto Inserido!')
                                                            except:
                                                                alert_error('HOUVE UM ERRO! Formato correto: aaaa-mm-dd')
                                                        else:
                                                            alert_error('Caracteres indesejados, atente-se ao valor correto. Formato: aaaa/mm/dd')
                                                    else:
                                                        alert_error('Formato inválido. Formato válido: aaaa/mm/dd')
                                                else:
                                                    alert_error('Houve um erro. Digite apenas número inteiros')
                                            else:
                                                alert_error('Você não digitou a QUANTIDADE')
                                        else:
                                            alert_error('Você digitou letras, atente-se ao valor correto!')           
                                    else:
                                        alert_error('Você não digitou o PREÇO')
                                else:
                                    alert_error('Número de caracteres máximo atingidos (20)')
                            else:
                                alert_error('Você não digitou a MARCA')
                        else:
                            alert_error('Número de caracteres máximo atingidos (20)')
                    else:
                        alert_error('Você não digitou o PRODUTO')
                else:
                    alert_error('NÃO é necessário o ID, retire para prosseguir')



            # Verificação se digitou "EXCLUIR"--===---===---===---===
            elif actions_user == 'Excluir':
                if id_choice:
                    if product_choice: 
                            alert_vazio()                       
                            query_delet(product_choice, id_choice)
                            sg.popup_timed('Produto excluído!')                          
                    else:
                        alert_error('Você não digitou o produto')
                else:
                    alert_error('Você não digitou o ID e o nome do PRODUTO')


except:
    sg.popup_ok('Houve um erro inesperado no Programa\nFale com o suporte: guimera.sistem@gmail.com')

    # ...............FIM da leituras das janelas