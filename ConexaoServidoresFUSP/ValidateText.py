def Text_Validate(host, host_found, connection_ms):

    def rate_packages(connection_ms):
        if connection_ms == 0:
            return '0%'  # Vermelho Fraco
        elif connection_ms == 1:
            return '25%'  # Vermelho Forte
        elif connection_ms == 2:
            return '50%'  # Amarelo Fraco
        elif connection_ms == 3:
            return '75%'  # Verde Fraco
        elif connection_ms == 4:
            return '100%'  # Verde Forte

    print(host, host_found, connection_ms)
    if host_found == 0:
        return True, f'O host {host}: Não foi encontrado\nPacotes entregues: {rate_packages(connection_ms)}'


    elif host_found == 1:
        if connection_ms == 0:
            return True, f'O host {host}: Foi encontrado. Pacotes entregues: {rate_packages(connection_ms)}'
        elif connection_ms == 1:
            return True, f'O host {host}: Foi encontrado. Pacotes entregues: {rate_packages(connection_ms)}'
        elif connection_ms == 2:
            return True, f'O host {host}: Foi encontrado. Pacotes entregues: {rate_packages(connection_ms)}'
        elif connection_ms == 3:
            return False, f'O host {host}: Foi encontrado. Pacotes entregues: {rate_packages(connection_ms)}'
        elif connection_ms == 4:
            return False, f'O host {host}: Foi encontrado. Pacotes entregues: {rate_packages(connection_ms)}'
    else:
        print('Houve algum problema')
