import os
from SendEmail import UrgentSendEmail

class ConnectionServers:

    @staticmethod
    def Ping_LocalHost():
        cmd = 'ping ' + '127.0.0.1' # Ip loopback
        comand = os.popen(cmd)
        statistic = comand.read()
        print('----------------------------------------------')
        print(statistic)
        print('----------------------------------------------')
        return statistic # Retorna valores lidos, da conexão básica LOOPBACK


    @staticmethod
    def Ping_Hosts(ip_insert):
        try:
            cmd = 'ping ' + ip_insert
            comand = os.popen(cmd)
            statistic = comand.read()
            print('----------------------------------------------')
            print(statistic)
            print('----------------------------------------------')
            return statistic, ip_insert
        except TypeError:
            print('Coloque um valor em <String>, você inseriu outro!')


    def Validate_Datas(self:str, ip):
        with open('reading-ping.txt', 'w', encoding='utf-8') as file:
            file.write(self) # Escrever em arquivo txt para analisar

        with open('reading-ping.txt', 'r', encoding='utf-8') as analysis_file:
            list_statistic = analysis_file.readlines() # Transforma em lista


        servidor_encontrado = 0  # Se for zero, enviar um email que ocorreu um erro ao conectar com o servidor desejado.
        porcentagem_ms = 0
        for i in list_statistic:
            if 'Disparando' in i:
                servidor_encontrado += 1

            if 'Resposta' in i:
                porcentagem_ms += 1


        values = UrgentSendEmail(ip,servidor_encontrado,porcentagem_ms)
        UrgentSendEmail.Sending(values)