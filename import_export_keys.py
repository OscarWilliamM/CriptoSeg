#funções de carreagr chaves, além de import e export e salvamento das chaves 
from Crypto.PublicKey import RSA
from generator_keys import generate_keys

def load_private_key(arq): #carrega a chave privada a partir de um arquivo porem codificada em bytes
    with open(arq, 'rb') as f:
        key_data = f.read()
        private_key = RSA.import_key(key_data)
    return private_key

def load_public_key(arq):  #carrega a chave pública a partir de um arquivo porem codificada em bytes
    with open(arq, 'rb') as f:
        key_data = f.read()
        public_key = RSA.import_key(key_data)
    return public_key

def export_keys(public_key_arq, private_key_arq):  #exporta o par de chaves privatekey.pem e publickey.pem
    with open(private_key_arq, 'wb') as f_private:
        f_private.write(private_key.export_key('PEM'))
    with open(public_key_arq, 'wb') as f_public:
        f_public.write(public_key.export_key('PEM'))
        
def export_public_key(public_key_arq):  #exporta a chave publica criada 'publickey.pem'
    with open(public_key_arq, 'wb') as f_public:
        f_public.write(public_key.export_key('PEM'))
        
def import_keys(public_key_arq, private_key_arq):  #importa o par de chaves privatekey.pem e publickey.pem
    with open(private_key_arq, 'rb') as f_private:
        private_key = RSA.import_key(f_private.read())
    with open(public_key_arq, 'rb') as f_public:
        public_key = RSA.import_key(f_public.read())
    return public_key, private_key

def import_public_key(public_key_arq):  #importa a chave publica exportada 'exported_publickey.pem'
    with open(public_key_arq, 'rb') as f_public:
        public_key = RSA.import_key(f_public.read())
    return public_key
    
if __name__ == '__main__':
    #gera as chaves publica e privada
    generate_keys()
    #carrega a chave privada e publica a partir dos arquivos criados, em bytes
    private_key = load_private_key('privatekey.pem')
    public_key = load_public_key('publickey.pem')
    #print(private_key.export_key('PEM')) #imprime a chave privada decodificada
    
    if True:  #exporta o par de chaves
        export_keys('exported_public.pem','exported_private.pem')
        print('chaves exportadas')
    
    if True:  #exporta só a chave publica
        export_public_key('exported_public.pem')
        print('chave publica exportada')
   
    if True: #importa o par de chaves
        public_key, private_key = import_keys('exported_public.pem','exported_private.pem')
        print('chaves importadas')
    
    if True:  #importa só a chave publica
        public_key = import_public_key('exported_public.pem')
        print('chave publica importada')

    