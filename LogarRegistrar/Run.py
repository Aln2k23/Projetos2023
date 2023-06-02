import PySimpleGUI as sg
import pyodbc
from Janelas import janela_login, janela_registro, janela_autenticacao, janela_recuperacao, janela_nova_senha
from SenhaAutomatica import senha_automatica
from Emails import enviar_email, validar_o_email



# CONEXÃO COM SERVIDOR
dados_conexao = ('Driver={SQL Server};'
                 'Server=AlanPc\SQLALAN;' 
                 'Database=InterfaceGrafica;')

conexao = pyodbc.connect(dados_conexao)
print('Conexão Efetuada!')
cursor = conexao.cursor()




janela_1, janela_2, janela_3, janela_4, janela_5 = janela_login(), None, None, None, None

while True:
    windows, events, values = sg.read_all_windows()
    
    def sem_erro():
        janela_2['-ERRO-'].update('')

    def caracteres_especiais(chave):
        caracteres = '[!@#$%&*]' # Lista de caractere que deve ter
        for i in values[chave]:
            if i in caracteres:
                return True # Tem
        return False # Não tem
    

    def um_numero_obrigatorio(chave):
        numeros = '0123456789' # Lista de número que deve ter
        for i in values[chave]:
            if i in numeros:
                return True # Tem
        return False # Não tem
# ----------------------------------------------------------------------------------


    if windows == janela_1 and events == sg.WIN_CLOSED: 
        break

    elif windows == janela_2 and events == sg.WIN_CLOSED:
        break 

    elif windows == janela_3 and events == sg.WIN_CLOSED:
        break

    elif windows == janela_4 and events == sg.WIN_CLOSED:
        break

    elif windows == janela_5 and events == sg.WIN_CLOSED:
        break


    if windows == janela_1 and events == 'Logar': # Evento Logar

        ver_senha = janela_1['-ERROLOG-']
        print(ver_senha)
        acess = values['-LOGIN_ACESS-']
        password_login = values['-LOGIN_PASS-']

        # Query
        consultar_tabela = f"""
        select user_acess, email_user, password_user from UsuariosCadastrados
        """
        cursor.execute(consultar_tabela) # Executa a consulta
        linhas_sql = cursor.fetchall() # Consulta todas as linhas
        

        for cada_linha in linhas_sql: # Looping em todas as linhas
            if cada_linha[0] == acess or cada_linha[1] == acess: # verificação de conta
                senha_correta = cada_linha[2] == password_login

                if senha_correta == True:
                    sg.popup_ok('Iniciando...')
                    # Fazer uma função que entre 
                else:
                    janela_1['-ERROLOG-'].update('Senha incorreta')         

        janela_1['-ERROLOG-'].update('Usuário ou E-mail não registrados')



    if windows == janela_2 and events == 'Registrar': # Registrar
        # VALIDAR CADASTRO, E COLOCAR NO BANCO DE DADOS
        def dados_validados():
            if len(values['-NOME-']) >= 1:
                sem_erro()

                if values['-USUARIO-']:
                    tamanho_usuario = len(values['-USUARIO-'])
                    if tamanho_usuario >= 3:
                        sem_erro()

                        if  len(values['-SENHA-']) >= 4 and len(values['-SENHA-']) <= 20:
                            sim_nao_number = um_numero_obrigatorio('-SENHA-')

                            if sim_nao_number == True:
                                sim_nao_especial = caracteres_especiais('-SENHA-')

                                if sim_nao_especial == True:

                                    if values['-SENHA-'] == values['-CONFIRMAR-']:

                                        if values['-EMAIL-']:
                                            sem_erro()
                                            resultado_email = validar_o_email(values['-EMAIL-'])

                                            if resultado_email == True:
                                                sem_erro()
                                                return True

                                            else:
                                                janela_2['-ERRO-'].update('E-mail Incorreto')

                                        else:
                                            janela_2['-ERRO-'].update('Você não digitou seu E-mail')

                                    else:
                                        janela_2['-ERRO-'].update('As senhas não coincidem')

                                else:
                                    janela_2['-ERRO-'].update('É necessário pelo menos um carácter especial [!@#$%&*]')

                            else:
                                janela_2['-ERRO-'].update('É necessário pelo menos um número')

                        else:
                            janela_2['-ERRO-'].update('Deve ter no minímo 4 caracteres, e no máximo 20 caracteres na Senha')

                    else:
                        janela_2['-ERRO-'].update('Deve ter 3 ou mais caracteres no Usuário')

                else:
                    janela_2['-ERRO-'].update('Você não escreveu o Usuário')

            else:
                janela_2['-ERRO-'].update('Você não escreveu seu Nome')
        dados_validos_sim_nao = dados_validados()


        # Inserir dados da pessoas cadastrada dentro do banco de dados
        if dados_validos_sim_nao == True:
            name_user = values['-NOME-']
            user_acess = values['-USUARIO-']
            email_user = values['-EMAIL-']
            password_user = values['-SENHA-']

            # Comando para registrar no banco de dados
            command_register = f""" 
            INSERT INTO UsuariosCadastrados (name_user, user_acess, email_user, password_user)
            VALUES ('{name_user}', '{user_acess}', '{email_user}','{password_user}')
            """

            # Execução do Comando
            cursor.execute(command_register)
            cursor.commit()
            sg.popup_timed('Usuário Registrado')
            janela_2.hide()
            janela_1.un_hide()



    if windows == janela_1 and events == 'Não sou registrado': # Abrir janela de registro
        janela_2 = janela_registro()
        janela_1.hide()

           

    if windows == janela_1 and events == 'Esqueci a senha':
        janela_3 = janela_recuperacao()
        janela_1.hide()



    if windows == janela_3 and events == 'Enviar':
        email_digitado = values['-EMAIL_RECUPERACAO-']
        
        comand_consult = f"""
        select email_user from UsuariosCadastrados
        where '{email_digitado}' = email_user
        """
        cursor.execute(comand_consult) # Executa a consulta
        busca = cursor.fetchall() # Consulta todas as linhas
        
        tamanho = len(busca)
        if tamanho == 1:
            senha_autenticacao = enviar_email(email_digitado)
            sg.popup_timed('Código enviado para o E-mail.')
            janela_4 = janela_autenticacao()
            janela_3.hide()

        else:
            janela_3['-EMAIL_ERROR-'].update('Este email não está registrado')




    if windows == janela_4 and events == 'Autenticar':
        Usuario_codigo_autentic = values['-USUARIO_CODIGO-']
        if Usuario_codigo_autentic == senha_autenticacao:
            janela_5 = janela_nova_senha()
            janela_4.hide()
        else:
            janela_4['-AUTENTICAR_ERRO-'].update('Código está incorreto')



    if windows == janela_2 and events == 'Voltar': # Voltar a tela de login
        janela_2.hide()
        janela_1.un_hide()



    if windows == janela_3 and events == 'Retornar':
        janela_3.hide()
        janela_1.un_hide()



    if windows == janela_2 and events == 'Gerar senha forte':  # Gera uma senha automática forte
        senha_gerada = senha_automatica()
        janela_2['-SENHA-'].update(senha_gerada)
        janela_2['-CONFIRMAR-'].update(senha_gerada)



    if windows == janela_5 and events == 'Confirmar':
        nova_senha = values['-NOVA_SENHA-']
        confir_senha = values['-CONFIRMAR_NOVA_SENHA-']
    
        print(nova_senha, confir_senha)
        query_password_antiga = f"""
        select email_user, password_user from UsuariosCadastrados
        where '{email_digitado}' = email_user
        """
        cursor.execute(query_password_antiga)
        line_corret = cursor.fetchall()
        email_colum = line_corret[0][0]
        passw_colum =line_corret[0][1]
        tamanho_senhas = len(nova_senha)

        if tamanho_senhas >= 4 and tamanho_senhas <= 20:
            sim_nao_number2 = um_numero_obrigatorio('-NOVA_SENHA-')

            if sim_nao_number2 == True:
                sim_nao_especial2 = caracteres_especiais('-NOVA_SENHA-')

                if sim_nao_especial2 == True:

                    if nova_senha == confir_senha:

                        if passw_colum != nova_senha:
                            query_update_passw = f"""
                            update UsuariosCadastrados
                            set password_user = '{nova_senha}'
                            where password_user = '{passw_colum}'
                            """

                            cursor.execute(query_update_passw)
                            cursor.commit()
                            sg.popup_timed('Recuperação bem sucedida!')
                            janela_5.hide()
                            janela_1.un_hide()

                        else:
                            janela_5['-SENHA_INCORRETAS-'].update('Não pode ser a mesma senha anterior')

                    else:
                        janela_5['-SENHA_INCORRETAS-'].update('As senhas não coincidem')

                else:
                    janela_5['-SENHA_INCORRETAS-'].update('É necessário pelo menos um carácter especial [!@#$%&*]')

            else:
                janela_5['-SENHA_INCORRETAS-'].update('É necessário pelo menos um número')

        else:
            janela_5['-SENHA_INCORRETAS-'].update('Deve ter no minímo 4 caracteres, e no máximo 20 caracteres na Senha')