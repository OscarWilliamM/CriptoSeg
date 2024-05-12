from Crypto.PublicKey import RSA
from import_export_keys import import_public_key
from Crypto.Cipher import PKCS1_OAEP
import json
import os

usuarios = dict()
mensagens = dict()

def cifragem(nome):
    usuarios = retorna_usuarios()
    if nome not in usuarios:
        print('Usuario não encontrado!')
        return
    pub_key = usuarios[nome]['public_key']
    #carrega o conteudo do arq com o texto claro
    arquivo = str(input('Digite o nome do arquivo (sem extensao) com a mensagem a ser cifrada: '))
    try:
        with open(f'{arquivo}.txt', 'rb') as file:
            mensagem = file.read()
    except FileNotFoundError:
        print('Arquivo não encontrado!')
        return
    mensagem = mensagem.decode('utf-8').encode('utf-8')

    #importa a chave publica do destinatario
    chave_importada = RSA.import_key(open(pub_key).read())

    #criptografa a mensagem com a chave public do destinatario
    cipher = PKCS1_OAEP.new(chave_importada)
    mensagem_cifrada = cipher.encrypt(mensagem)
    #jogando a mensagem cifrada em um novo arq
    if not os.path.exists('mensagens_cifradas'): #cria a pasta keys se ela nao existir
        os.makedirs('mensagens_cifradas')
    with open(f'mensagens_cifradas/{arquivo}_cifrada.txt', 'wb') as file:
        file.write(mensagem_cifrada)
    if not os.path.exists('mensagens.json'): #cria o arquivo json se ele não existir
            with open('mensagens.json', 'w') as jsonfile:
                jsonfile.write('{}')
    with open('mensagens.json', 'r') as jsonfile:
        mensagens = json.load(jsonfile)
        if arquivo not in mensagens:
            mensagens[arquivo] = {'destinatario': f'{nome}', 'identificador': f'{arquivo}_cifrada.txt'}
    with open('mensagens.json', 'w') as jsonfile:
        json.dump(mensagens, jsonfile)

def decifragem(nome):
    usuarios = retorna_usuarios()
    if nome not in usuarios:
        print('Usuario não encontrado!')
        return
    mensagens = retorna_mensagens()
    minhas_mensagens = []
    for key in mensagens:
        if mensagens[key]['destinatario'] == nome:
            minhas_mensagens.append(key)

    senha_digitada = str(input('Digite a senha para ter acesso a chave privada: '))
    if senha_digitada != usuarios[nome]['senha']:
        print('Senha incorreta!')
        return
    priv_key = usuarios[nome]['private_key']
    #importa a chave privada do destinatario
    chave_importada = RSA.import_key(open(f'{priv_key}').read())
    #carrega as mensagens decifrando-as e mostrando na tela
    arquivo = str(input('Digite o nome do arquivo cifrado (sem extensão) com a mensagem a ser decifrada: '))
    try:
        with open(f'mensagens_cifradas/{arquivo}.txt', 'rb') as file:
            mensagem_cifrada = file.read()
            cipher = PKCS1_OAEP.new(chave_importada)
            mensagem = cipher.decrypt(mensagem_cifrada)
            print(mensagem.decode('utf-8'))
    except:
        print('Arquivo não encontrado ou de acesso não autorizado')


def enviar_mensagem(texto, chave_publica, nome):
    usuarios = retorna_usuarios()
    if nome not in usuarios:
        print('Usuario não encontrado!')
        return
    cifragem(texto, chave_publica, nome)

def retorna_usuarios():
    if not os.path.exists('keys'): #cria a pasta keys se ela nao existir
        os.makedirs('keys')
    if not os.path.exists('usuarios.json'): #cria o arquivo json se ele não existir
            with open('usuarios.json', 'w') as jsonfile:
                jsonfile.write('{}')

    with open('usuarios.json', 'r') as jsonfile:
        usuarios = json.load(jsonfile)
    return usuarios

def retorna_mensagens():
    if not os.path.exists('mensagens.json'): #cria o arquivo json se ele não existir
            with open('mensagens.json', 'w') as jsonfile:
                jsonfile.write('{}')

    with open('mensagens.json', 'r') as jsonfile:
        mensagens = json.load(jsonfile)
    return mensagens


if __name__ == '__main__':
    # simulando enviar mensagem para alguém
    nome = str(input('Digite o nome do destinatario: '))
    cifragem(nome) # aqui vai o nome do donoda chave publica

    # simulando receber mensagem de alguém
    outro_nome = str(input('Digite seu nome para decriptar suas mensagens: '))
    decifragem(outro_nome) # aqui vai o nome do dono da chave privada