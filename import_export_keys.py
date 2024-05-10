#funções de carreagr chaves, alem de import e export e salvamento das chaves
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

def export_keys(public_key, private_key):  #exporta o par de chaves myprivatekey.pem e mypublickey.pem
    with open(private_key, 'wb') as f_private:
        f_private.write(private_key.export_key('PEM'))
    with open(public_key, 'wb') as f_public:
        f_public.write(public_key.export_key('PEM'))

def export_public_key(public_key):  #exporta a chave publica criada 'publickey.pem'
    with open(public_key, 'wb') as f_public:
        f_public.write(public_key.export_key('PEM'))

def import_keys(public_key, private_key):  #importa o par de chaves privatekey.pem e publickey.pem
    with open(private_key, 'rb') as f_private:
        private_key = RSA.import_key(f_private.read())
    with open(public_key, 'rb') as f_public:
        public_key = RSA.import_key(f_public.read())
    return public_key, private_key

def import_public_key(public_key_arq):  #importa a chave publica enviada pelo remetente
    with open(public_key_arq, 'rb') as f_public:
        public_key = RSA.import_key(f_public.read())
    return public_key

if __name__ == '__main__':
    #carrega a chave privada e publica a partir dos arquivos criados, em bytes
    private_key = load_private_key('myprivatekey.pem')
    public_key = load_public_key('mypublickey.pem')

    #testes
    if True:  #exporta o par de chaves
        export_keys('exported_publickey.pem','exported_privatekey.pem')
        print('chaves exportadas')
    '''
    if True:  #exporta só a chave publica
        export_public_key('exported_public.pem')
        print('chave publica exportada')
    '''
    