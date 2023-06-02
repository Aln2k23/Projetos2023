from Send import send
from time import sleep
from ValidateText import Text_Validate

class UrgentSendEmail:

    def __init__(self, host:str, host_found:int, connection_ms:int):
        self.host = host
        self.host_found = host_found
        self.connection_ms = connection_ms

    def Sending(self):
        true_or_false, message = Text_Validate(self.host, self.host_found, self.connection_ms)
        if true_or_false == True:
            send('ala.pereiradocavalcante@gmail.com', message)
            print('Servidor Error! Email de monitoramento enviado!\n\n')
            sleep(4)
        else:
            print('Servidor Ok\n\n')