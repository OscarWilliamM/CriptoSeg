#gera as chaves publica e privada no modelo openssl
from Crypto.PublicKey import RSA
import random
import string
import json

usuarios = dict()

def generate_keys():
    nome = input('Cadastre um nome de usuario: ')
    # checa se o nome ja foi cadastrado
    with open('usuarios.json', 'r') as jsonfile:
        usuarios = json.load(jsonfile)
    if nome in usuarios:
        print('Já há um usuario cadastrado com esse nome!\nTente outro nome.')
        generate_keys()
    # gerar um par de chaves RSA
    key = RSA.generate(1024)

    # salva a chave privada em um arquivo
    string_length = 10
    chars = string.ascii_letters + string.digits
    random_string = ''.join(random.sample(chars, string_length))
    f_private = open(f'keys/{random_string}.pem','wb')
    f_private.write(key.export_key('PEM'))
    f_private.close()
    # salva a chave publica em um arquivo
    f_public = open(f'keys/{nome}publickey.pem','wb')
    f_public.write(key.public_key().export_key('PEM'))
    f_public.close()

    save_user(nome, f'keys/{random_string}.pem', f'keys/{nome}publickey.pem')


def save_user(nome, priv_key_path, pub_key_path):
    # carrega os usuarios do json para o dicionario
    with open('usuarios.json', 'r') as jsonfile:
        usuarios = json.load(jsonfile)
    #cadastrar um novo usuario no dicionario
    senha = str(input('Cadastre uma senha: ')).strip()
    usuarios[nome] = {'senha': senha, 'private_key': priv_key_path, 'public_key': pub_key_path}

    #salva o json com o novo usuario
    with open('usuarios.json', 'w') as f:
        json.dump(usuarios, f)

#lista todos os nomes associados as chaves publicas
def list_users():
    with open('usuarios.json', 'r') as jsonfile:
        usuarios = json.load(jsonfile)
    for nome in usuarios:
        print(nome)

#fução que busca e retorna a chave publica de um usuario pesquisando pelo nome
def list_user_pubkey(nome):
    with open('usuarios.json', 'r') as jsonfile:
        usuarios = json.load(jsonfile)

    for user in usuarios:
        if user == nome:
            print(usuarios[user]['public_key'])
            return usuarios[user]['public_key']
    print('usuario não encontrado')
    return None

#funcao pesquisa e retorna a chave privada de um usuario buscando pelo nome (necessario senha)
def list_user_privkey(nome, senha):
    with open('usuarios.json', 'r') as jsonfile:
        usuarios = json.load(jsonfile)

    for user in usuarios:
        if user == nome:
            if usuarios[user]['senha'] == senha:
                print(usuarios[user]['private_key'])
                return usuarios[user]['private_key']
            else:
                print('senha incorreta')
                return None
    print('usuario não encontrado ou não existe')
    return None

def delete_keys(nome, senha):
    with open('usuarios.json', 'r') as jsonfile:
        usuarios = json.load(jsonfile)

    for user in usuarios:
        if user == nome:
            if usuarios[user]['senha'] == senha:
                del usuarios[user]
                with open('usuarios.json', 'w') as f:
                    json.dump(usuarios, f)
                return True
            else:
                print('senha incorreta')
                return False
    print('usuario não encontrado ou não existe')
    return False

if __name__ == '__main__':
    generate_keys()
    list_users()
    list_user_pubkey("joao")
    list_user_privkey("marcelo", "1234")
    delete_keys("oscar", "1234")
    