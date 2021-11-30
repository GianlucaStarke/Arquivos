import re
import urllib.request

try:

    f = open('alice.txt')
except:

    print('Arquivo nao existe, baixando...')

    try:

        alice = urllib.request.urlopen('https://www.gutenberg.org/files/11/11-0.txt').read().decode('utf8')

        with open('alice.txt', 'w') as f:
            f.write(alice)
            f.close()
    except:
    
        print('Houve um erro no download.')
        exit()
    else:

        print('Download efetuado com sucesso')
        f = open('alice.txt')
finally:

    alice_so_letras = ''.join(re.findall('[a-zA-Z]', f.read())).lower()
    f.close()
    frequencia_letras = {x:alice_so_letras.count(x) for x in alice_so_letras}
    
    print(frequencia_letras)
