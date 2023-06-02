import PySimpleGUI as sg
caminho = r'imagens\avatar100-removebg-preview.png'

def janela_login():
    sg.theme('Reddit')
    estrutura_janela_login = [
        [sg.Image(caminho)],
        [sg.Push(), sg.Text('E-mail ou Usuário'), sg.Input(key='-LOGIN_ACESS-'), sg.Push()],
        [sg.Push(), sg.Text('        Senha        '), sg.Input(key='-LOGIN_PASS-', password_char='*'), sg.Push()],
        [sg.Push(), sg.Text('', key='-ERROLOG-'), sg.Push()],
        [sg.Text('         '), sg.Button('Logar'), sg.Text('    '), sg.Button('Não sou registrado'),
         sg.Button('Esqueci a senha'), sg.Push(), ]
    ]

    return sg.Window('Tela de login', estrutura_janela_login, size=(500, 245), element_justification='c', finalize=True)




def janela_registro():
    sg.theme('Reddit')
    estrutura_janela_registro = [
        [sg.Push(), sg.Image('avatar100-removebg-preview.png'), sg.Push()],
        [sg.Text('      Nome'), sg.Push(), sg.Input(key='-NOME-', size=(50)), sg.Push()],
        [sg.Text('   Usuário'), sg.Push(), sg.Input(key='-USUARIO-', size=(50)), sg.Push()],
        [sg.Text('     Senha'), sg.Push(), sg.Input(key='-SENHA-', size=(50)), sg.Push()],
        [sg.Text(' Confirmar'), sg.Push(), sg.Input(key='-CONFIRMAR-', size=(50)), sg.Push()],
        [sg.Text('     E-mail'), sg.Push(), sg.Input(key='-EMAIL-', size=(50)), sg.Push()],
        [sg.Push(), sg.Text('', key='-ERRO-'), sg.Push()],
        # BOTÕES
        [sg.Push(), sg.Button('Registrar'), sg.Button('Voltar'), sg.Button('Gerar senha forte'), sg.Push()]
    ]

    return sg.Window('Tela de registro', estrutura_janela_registro, size=(550, 320), finalize=True)




def janela_autenticacao():
    sg.theme('Reddit')
    layout = [[sg.T('Digite o código de autenticação')],
              [sg.I(size=(6),key='-USUARIO_CODIGO-')],
              [sg.T('',key='-AUTENTICAR_ERRO-')],
              [sg.Button('Autenticar')]]

    return sg.Window('Autenticação', layout=layout,element_justification='c',finalize=True)




def janela_recuperacao():
    sg.theme('Reddit')
    estrutura = [[sg.Text('Digite seu E-mail abaixo')], # 1
                 [sg.Input(key='-EMAIL_RECUPERACAO-')], # 2
                 [sg.Text('',key='-EMAIL_ERROR-')], # 3
                 [sg.Button('Enviar'),sg.Button('Retornar')], # 4
                 ]
    return sg.Window('Recuperação', layout=estrutura,size=(250,117), element_justification='c', finalize=True)




def janela_nova_senha():
    sg.theme('Reddit')
    layout = [[sg.Push(),sg.T('Nova Senha'),sg.I(key='-NOVA_SENHA-')],
              [sg.Push(),sg.T(' Confirmar '),sg.I(key='-CONFIRMAR_NOVA_SENHA-')],
              [sg.Push(),sg.T('', key='-SENHA_INCORRETAS-'),sg.Push()],
              [sg.Push(),sg.Button('Confirmar'),sg.Push()]]

    return sg.Window('Nova Senha', layout=layout, finalize=True)
