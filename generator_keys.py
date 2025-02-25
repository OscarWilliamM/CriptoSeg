#gera as chaves publica e privada no modelo openssl
from Crypto.PublicKey import RSA
import random
import string
import json
import os

usuarios = dict()

def generate_keys(nome, senha):
    if not os.path.exists('keys'): #cria a pasta keys se ela nao existir
        os.makedirs('keys')
    if not os.path.exists('usuarios.json'): #cria o arquivo json se ele não existir
            with open('usuarios.json', 'w') as jsonfile:
                jsonfile.write('{}')

    with open('usuarios.json', 'r') as jsonfile:
        usuarios = json.load(jsonfile)
    # checa se o nome ja foi cadastrado
    if nome in usuarios:
        print('Já há um usuario cadastrado com esse nome!\nTente outro nome.')
        generate_keys()
    # gerar um par de chaves RSA
    key = RSA.generate(1024)

    # salva a chave privada em um arquivo
    string_length = 12
    chars = string.ascii_letters + string.digits
    random_string = ''.join(random.sample(chars, string_length))
    f_private = open(f'keys/{random_string}.pem','wb')
    f_private.write(key.export_key('PEM'))
    f_private.close()
    # salva a chave publica em um arquivo
    f_public = open(f'keys/{nome}publickey.pem','wb')
    f_public.write(key.public_key().export_key('PEM'))
    f_public.close()

    save_user(nome, f'keys/{random_string}.pem', f'keys/{nome}publickey.pem', senha)


def save_user(nome, priv_key_path, pub_key_path, senha):
    # carrega os usuarios do json para o dicionario
    with open('usuarios.json', 'r') as jsonfile:
        usuarios = json.load(jsonfile)
    senha = senha.strip()
    usuarios[nome] = {'senha': senha, 'private_key': priv_key_path, 'public_key': pub_key_path}

    #salva o json com o novo usuario
    with open('usuarios.json', 'w') as f:
        json.dump(usuarios, f)

#lista todos os nomes associados as chaves publicas
def list_users():
    usuarios_list = []
    with open('usuarios.json', 'r') as jsonfile:
        usuarios = json.load(jsonfile)
    for nome in usuarios:
        usuarios_list.append(nome)

    return usuarios_list

#fução que busca e retorna a chave publica de um usuario pesquisando pelo nome
def search_pubkey(nome):
    if os.path.exists('usuarios.json') == False or os.path.getsize('usuarios.json') != 0:
        with open('usuarios.json', 'r') as jsonfile:
            usuarios = json.load(jsonfile)

        for user in usuarios:
            if user == nome:
                endereco = usuarios[user]['public_key']
                print(endereco)
                with open(endereco, 'rb') as f:
                    conteudo = f.read()
                return f'Chave pública: {usuarios[user]['public_key']}\n\n{conteudo.decode("utf-8")}'
        print('usuario não encontrado')
        return 'o nome do usuario não foi encontrado'
    else:
        print('não há usuarios cadastrados')
        return 'o nome do usuario não foi encontrado'

#funcao pesquisa e retorna a chave privada de um usuario buscando pelo nome (necessario senha)
def search_privkey(nome, senha):
    if os.path.exists('usuarios.json') == False or os.path.getsize('usuarios.json') != 0:
        with open('usuarios.json', 'r') as jsonfile:
            usuarios = json.load(jsonfile)

        for user in usuarios:
            if user == nome:
                if usuarios[user]['senha'] == senha:
                    endereco = usuarios[user]['private_key']
                    print(endereco)
                    with open(endereco, 'rb') as f:
                        conteudo = f.read()
                    return f'{usuarios[user]['private_key']}\n\n{conteudo.decode("utf-8")}'
                else:
                    print('senha incorreta')
                    return 'senha incorreta'

        print('usuario não encontrado ou não existe')
        return 'usuario nao encontrado ou nao existe'
    else:
        print('não há usuarios cadastrados')
        return 'não há usuarios cadastrados'

def delete_keys(nome, senha):
    if os.path.exists('usuarios.json') == False or os.path.getsize('usuarios.json') != 0:
        with open('usuarios.json', 'r') as jsonfile:
            usuarios = json.load(jsonfile)

        for user in usuarios:
            if user == nome:
                if usuarios[user]['senha'] == senha:
                    os.remove(usuarios[user]['private_key'])    #deleta a chave privada do usuario de 'keys'
                    os.remove(usuarios[user]['public_key'])  #deleta a chave publica do usuario de 'keys'
                    del usuarios[user]    #deleta o usuario de usuarios.json
                    with open('usuarios.json', 'w') as f:
                        json.dump(usuarios, f)
                    return True
                else:
                    print('senha incorreta')

        print('usuario não encontrado ou não existe')
    else:
        print('não há usuarios cadastrados')

if __name__ == '__main__':
    generate_keys()
    #list_users()
    #search_pubkey("joao")
    #search_privkey("marcelo", "1234")
    #delete_keys("paulo mota", "12345")
