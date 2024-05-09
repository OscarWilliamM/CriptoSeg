from Crypto.PublicKey import RSA
from import_export_keys import import_public_key
from Crypto.Cipher import PKCS1_OAEP

def cifragem(text_claro, chave_publica, nome):
    #carrega o conteudo do arq com o texto claro
    with open('text_claro.txt', 'r') as file:
        mensagem = file.read().encode('utf-8')

    #importa a chave publica do destinatario
    chave_importada = RSA.import_key(open('keys/mypublickey.pem').read())

    #criptografa a mensagem com a chave public do destinatario
    cipher = PKCS1_OAEP.new(chave_importada)
    mensagem_cifrada = cipher.encrypt(mensagem)

    #jogando a mensagem cifrada em um novo arq
    with open('mensagem_cifrada.txt', 'wb') as file:
        file.write(mensagem_cifrada)

def decifragem(text_cifrado, chave_privada, nome):
    #carrega o conteudo do arq com o texto cifrado
    with open('mensagem_cifrada.txt', 'rb') as file:
        mensagem_cifrada = file.read()

    #importa a chave privada do destinatario
    chave_importada = RSA.import_key(open('keys/myprivatekey.pem').read())

    #descriptografa a mensagem com a chave privada do destinatario
    cipher = PKCS1_OAEP.new(chave_importada)
    mensagem = cipher.decrypt(mensagem_cifrada)

    #jogando a mensagem decifrada em um novo arq
    with open('mensagem_decifrada.txt', 'wb') as file:
        file.write(mensagem)

if __name__ == '__main__':
    chave_publica = import_public_key('mypublickey.pem')
    chave_privada = import_public_key('myprivatekey.pem')
    cifragem('text_claro.txt', chave_publica)
    decifragem('mensagem_cifrada.txt', chave_privada)




