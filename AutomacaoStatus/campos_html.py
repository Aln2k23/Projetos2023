from datetime import date
import pyautogui as auto
import time


# Acessos
user = 'user'
passw = 'passw'


# Data
data_atual = date.today() # Pegando data atual
data_formatado = data_atual.strftime('%d/%m/%Y') # Data formatada


# Função de temporizador
def spp(temp):
    time.sleep(temp)


# Campo personalizado que vai ser adicionado
texto_novo = f""" <p><strong>{data_formatado}</strong></p> 


  <p>Sem incidentes anteriores.</p>

  
  <hr width="“1”" size="“10”">"""


# Automatização = AÇÃO DE COLAR
auto.click(x=169, y=742) # CHROME ABERTO!!!
spp(1.2)
auto.hotkey('ctrl','t') # Abrir nova guia
spp(1.5)
auto.write('https://fusp.org.br/admin-fusp') # link do site
auto.press('enter') # Entrar nele
spp(5.5)
auto.click(x=622, y=282) # Campo do email
spp(0.3)
auto.write(user) # Escrever email
spp(1.2)
auto.click(x=589, y=352) # Campo senha
spp(0.3)
auto.write(passw) # Escrever senha
auto.click(x=672, y=419) # Campo ENTRAR
spp(3.5)
auto.click(x=64, y=234) # Acessa PÁGINAS
spp(1.8)
auto.click(x=307, y=209) # Buscar a página STATUS
spp(0.5)
auto.write('status')
spp(1.2)
auto.click(x=368, y=526) # Entrando na página status
spp(2)
auto.click(x=1349, y=322) # Abrir engrenagem
spp(0.3)
auto.click(x=1256, y=325) # Acessando código fonte
spp(0.3)
auto.click(x=626, y=382) # Clicando no campo de código
spp(1.2)
auto.hotkey('ctrl','a') # Selecionando todo o código
spp(1.2)
auto.hotkey('ctrl','c') # Copiado o código
spp(1.2)
auto.click(x=1364, y=742) # Área de trabalho
spp(1.2)
auto.click(x=1161, y=135, clicks=2) # Acessando a Pasta autoStatus
spp(1.2)
auto.click(x=348, y=343, clicks=2) # Selecionando o texto desejado
spp(1.2)
auto.click(x=638, y=392) # Selecionando o campo do txt
spp(1.2)


auto.hotkey('ctrl','a') # Selecionando todo o texto
spp(1.2)
auto.hotkey('ctrl','v') # Colando
spp(1.2)
auto.hotkey('ctrl','s') # Salvando
spp(1.2)
auto.hotkey('alt','f4') # Fechado bloco de notas
spp(1.2)

with open('texto_antigo.txt','r', encoding='utf-8') as leitura: # Fazendo leitura do arquivo e adicionado para uma lista
    texto_puro = leitura.readlines()


# Apagando último bloco de texto
for apagando_linha in range(5):
    del texto_puro[71]
    

# Criando uma nova lista com o campo personalizado adicionado
lista = [] 
for indice in texto_puro:
    if indice == '<div>\n':
        lista.append(indice)
        lista.append(texto_novo)
    lista.append(indice)


# Transformando em string para ser adicionado ao um novo texto
novo_texto = '' 
for linha in lista:
    novo_texto += linha


# Adicionando um texto com string nova
with open('texto_novo.txt', 'w',encoding='utf-8') as adicionar:
    adicionar.writelines(novo_texto)

auto.click(x=325, y=357, clicks=2) # Abri texto novo
spp(0.5)
auto.click(x=670, y=404) # Selecionar ele
spp(1.2)
auto.hotkey('ctrl','a') # Selecionar tudo
spp(1.2)
auto.hotkey('ctrl','c') # Copiar
spp(1.2)
auto.hotkey('alt','f4') # Fechar texto
spp(1.2)
auto.hotkey('alt','f4') # Fechar explorer
spp(1.2)
auto.click(x=169, y=742) # CHROME ABERTO!!!
spp(1)
auto.click(x=670, y=404) # Selecionar ele
spp(1.2)
auto.hotkey('ctrl','a') # Selecionar tudo
spp(1.2)
auto.hotkey('ctrl','v') # Colar
spp(1.2)
auto.click(x=849, y=665) # Salvando
spp(1.2)
auto.click(x=1299, y=621) # Três barras
spp(0.5)
auto.click(x=1240, y=623) # Salvando a página
spp(6)
auto.click(x=1291, y=196) # Visualizando