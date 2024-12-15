import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/watch?v=8jAykqxIeqw&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=139')
except:
    print('O site não está acesivel!')
else:
    print('Entrou!')