import smtplib
import email.message
import random


def enviar_email(email_destinatario):
    password = 'flgvyttwsyrnmsbd'  # Senha App gmail gerada automática
    print(email_destinatario)

    senha_autenticacao = ''
    for i in range(6):
        gerador = random.choice('0123456789')
        senha_autenticacao += gerador

    titulo = 'Recuperação de senha - guimera'

    descricao_email = f"""Olá guimerano, esqueceu a senha né.<br>
    Segue abaixo seu código de autenticação de Usuário:
    <h2> {senha_autenticacao} </h2>"""

    msg = email.message.Message()
    msg['Subject'] = titulo  # Título
    msg['From'] = 'guimera.sistem@gmail.com'  # Remetente
    msg['To'] = f'{email_destinatario}'  # destinatário

    msg.add_header('Content-Type', 'text/html')  # Configurações site html
    msg.set_payload(descricao_email)  # Corpo email/descrição

    s = smtplib.SMTP('smtp.gmail.com: 587')  # Servidor e porta de acesso ao Gmail
    s.starttls()  # Executação da porta e servidor
    # Login Credentials for sending the mail
    s.login(msg['From'], password)  # Login da conta: email, e a senha
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))  # Envio da mensagem
    print('Email enviado')
    return senha_autenticacao




def validar_o_email(email_digitado):
    def validar_arroba():
        if '@' in email_digitado:
            return True
        return False

    if '.br' in email_digitado:
        if '.com' in email_digitado:
            existe_ou_nao = validar_arroba()
            return existe_ou_nao

    elif '.com' in email_digitado:
        existe_ou_nao = validar_arroba()
        return existe_ou_nao

    else:
        return False
