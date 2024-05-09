#gera as chaves publica e privada no modelo openssl
from Crypto.PublicKey import RSA 

def generate_keys():
    # gerar um par de chaves RSA
    key = RSA.generate(1024)
    
    # salva a chave privada em um arquivo
    f_private = open('myprivatekey.pem','wb')
    f_private.write(key.export_key('PEM'))
    f_private.close()
    # salva a chave publica em um arquivo
    f_public = open('mypublickey.pem','wb')
    f_public.write(key.public_key().export_key('PEM'))
    f_public.close()

if __name__ == '__main__':
    generate_keys()
    

 

