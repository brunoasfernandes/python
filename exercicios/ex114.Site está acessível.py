import urllib
import urllib.request

try:    # tente fazer isso
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:     # se não conseguir
    print('O site não está disponível.')
else:
    print('O site está funcionando.')
