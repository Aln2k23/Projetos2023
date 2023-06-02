from ConnectionServers import ConnectionServers
from time import sleep

ConnectionServers.Ping_LocalHost()

# Sites

fusp, ip = ConnectionServers.Ping_Hosts('fusp.org.br')
ConnectionServers.Validate_Datas(fusp, ip)

managerweb, ip = ConnectionServers.Ping_Hosts('managerweb.fusp.org.br')
ConnectionServers.Validate_Datas(managerweb, ip)


# Servidores FUSP/USP

srvprint, ip = ConnectionServers.Ping_Hosts('srvprint02')
ConnectionServers.Validate_Datas(srvprint, ip)

srvscfp, ip = ConnectionServers.Ping_Hosts('srvscfp')
ConnectionServers.Validate_Datas(srvscfp, ip)

srvsql2017, ip = ConnectionServers.Ping_Hosts('srvsql2017')
ConnectionServers.Validate_Datas(srvsql2017, ip)

srvsql2014, ip = ConnectionServers.Ping_Hosts('srvsql2014')
ConnectionServers.Validate_Datas(srvsql2014, ip)

srvapptrc, ip = ConnectionServers.Ping_Hosts('srvapptrc')
ConnectionServers.Validate_Datas(srvapptrc, ip)

srvfile, ip = ConnectionServers.Ping_Hosts('srvfile')
ConnectionServers.Validate_Datas(srvfile, ip)

srvdc02, ip = ConnectionServers.Ping_Hosts('srvdc02')
ConnectionServers.Validate_Datas(srvdc02, ip)

srvapp, ip = ConnectionServers.Ping_Hosts('srvapp')
ConnectionServers.Validate_Datas(srvapp, ip)

srvweb02, ip = ConnectionServers.Ping_Hosts('srvweb02')
ConnectionServers.Validate_Datas(srvweb02, ip)

srvmanager02, ip = ConnectionServers.Ping_Hosts('srvmanager02')
ConnectionServers.Validate_Datas(srvmanager02, ip)

srvtaf, ip = ConnectionServers.Ping_Hosts('srvtaf')
ConnectionServers.Validate_Datas(srvtaf, ip)

print('\nFim do monitoramento, será efetuado novamente daqui a 1 hora.')
sleep(5)
