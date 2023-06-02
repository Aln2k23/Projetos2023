import random

def senha_automatica():

    """
    Está função serve para gerar caracteres automático, dentre eles: caracter especial, números
    inteiros, e letras maiúsculas e minúsculas.
    Retorna a string com valores obtidos do gerador de "string".
    """
    string = ''
    for x in range(10):
        gerador = random.choice("6A.-avnaa5@B$.aaAFfIOaapfwte#aVfAZFaftiApllApoSazawJtyuu/9*-C\
c9PIL1.D-0#$/Oçlajafaa1urd*+=+#=@@$aA8a#g[Ee-FAN/F.pHGfBF*NB#G71*gGAFAWAFAFa]f@afaH[X7]/@9\
$AD$9h$2$F-I/zazaffgxacaGSGa@ig$\Jx[jbAFÇh.Kk5-1$[p@/5L0r*-l3F*GLKÇruruF3-1M.$@#5m/n$O.gçl\
#agjapo9#/44o$\ArF[1/.a0XaZ4afapAgdhka$5j@!![PpQqR9!6!5r/S@-*!sT$@t*Uu%AAFA*@4[8-V%/A.v[W]\
#wWlafkBFDADFAA!!po!afjaGA[*K$ÇA-QFZ\A!FG!OxYy![-7-Zz.~çkjknvf!aZFBTRTtfl#h$ja1y1a!F!D!AAR.")
        string += gerador
        continue
    return string