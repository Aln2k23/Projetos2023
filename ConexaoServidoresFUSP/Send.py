import smtplib
import email.message

def send(email_destinatario, message):
    password = 'flgvyttwsyrnmsbd'  # Senha App gmail gerada automática


    msg = email.message.Message()
    msg['From'] = 'guimera.sistem@gmail.com'  # Remetente
    msg['To'] = f'{email_destinatario}'  # destinatário
    msg['Subject'] = 'Houve um problema com o servidor' # Título
    descricao_email = f"""{message}"""


    msg.add_header('Content-Type', 'text/html') # Configurações site html
    msg.set_payload(descricao_email) # Corpo email/descrição


    s = smtplib.SMTP('smtp.gmail.com: 587') # Servidor e porta de acesso ao Gmail
    s.starttls() # Executação da porta e servidor

    # Login Credentials for sending the mail
    s.login(msg['From'], password) # Login da conta: email, e a senha
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8')) # Envio da mensagem
    return None
