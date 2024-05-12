#gerenciamento das chaves através da interface
from generator_keys import *
from cript_and_descript_text import *
from import_export_keys import *
import PySimpleGUI as sg

sg.theme('DarkAmber')

#tamanho da janela
sg.SetOptions(element_padding=(60, 20))
#botoes da janela principal
layout = [[sg.Text('Bem vindo ao gerenciador de chaves!')],
        [sg.Button('Gerar chaves'), sg.Button('Criptografia e Descriptografia'),
        sg.Button('Gerenciar Chaves'), sg.Button('Sair')]]

window = sg.Window('Gerenciador de chaves', layout)

#loop de eventos na interface
while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        window.close()
        break
    if event == 'Gerar chaves':
        gerar_layout = [[sg.Text('Digite o nome e a senha para a geração das chaves')],
            [sg.Text('Nome:'), sg.InputText()], [sg.Text('Senha:'), sg.InputText()],
            [sg.Button('Gerar'), sg.Button('Voltar')]]

        gerar_window = sg.Window('Gerar chaves', gerar_layout)
        while True:
            gerar_event, gerar_value = gerar_window.read()
            if gerar_event == sg.WIN_CLOSED or gerar_event == 'Voltar':
                gerar_window.close()
                break

            if gerar_event == 'Gerar':
                nome = gerar_value[0]
                senha = gerar_value[1]
                generate_keys(nome, senha)
                sg.Popup('Chave gerada com sucesso!')
                gerar_window.close()
                break

    if event == 'Gerenciar Chaves':
        gerenciar_layout = [[sg.Text('Escolha uma opção')],
            [sg.Button('listar users'), sg.Button('Pesquisar Chave Publica'), sg.Button('Visualizar chave privada'),
            sg.Button('deletar chave'), sg.Button('Voltar')]]

        gerenciar_window = sg.Window('Gerenciar chaves', gerenciar_layout)
        while True:
            gerenciar_event, gerenciar_value = gerenciar_window.read()
            if gerenciar_event == sg.WIN_CLOSED or gerenciar_event == 'Voltar':
                gerenciar_window.close()
                break

            if gerenciar_event == 'listar users':
                list_layout = [[sg.Text('Lista de usuarios cadastrados')],
                    [sg.Multiline(list_users(), size=(28, 10))],
                    [sg.Button('Voltar')]]

                list_window = sg.Window('Lista de usuarios', list_layout)
                while True:
                    list_event, list_value = list_window.read()
                    if list_event == sg.WIN_CLOSED or list_event == 'Voltar':
                        list_window.close()
                        break
                    list_window.close()
                    break

            if gerenciar_event == 'Pesquisar Chave Publica':
                pesquisar_layout = [[sg.Text('Digite o nome do usuario')],
                    [sg.InputText()],
                    [sg.Button('Pesquisar'), sg.Button('Voltar')]]

                pesquisar_window = sg.Window('Pesquisar chave publica', pesquisar_layout)
                while True:
                    pesquisar_event, pesquisar_value = pesquisar_window.read()
                    if pesquisar_event == sg.WIN_CLOSED or pesquisar_event == 'Voltar':
                        pesquisar_window.close()
                        break

                    if pesquisar_event == 'Pesquisar':
                        nome = pesquisar_value[0]
                        pubkey = search_pubkey(nome)
                        sg.popup('Chave publica:', pubkey)
                        pesquisar_window.close()
                        break

            if gerenciar_event == 'Visualizar chave privada':
                visualizar_layout = [[sg.Text('Digite o nome do usuario')],
                    [sg.InputText()], [sg.Text('Digite sua senha:')], [sg.InputText()],
                    [sg.Button('Visualizar'), sg.Button('Voltar')]]

                visualizar_window = sg.Window('Visualizar chave privada', visualizar_layout)
                while True:
                    visualizar_event, visualizar_value = visualizar_window.read()
                    if visualizar_event == sg.WIN_CLOSED or visualizar_event == 'Voltar':
                        visualizar_window.close()
                        break

                    if visualizar_event == 'Visualizar':
                        nome = visualizar_value[0]
                        senha = visualizar_value[1]
                        privkey = search_privkey(nome, senha)
                        sg.popup('Chave privada:', privkey)
                        visualizar_window.close()
                        break

            if gerenciar_event == 'deletar chave':
                deletar_layout = [[sg.Text('Digite o nome do usuario que deseja deletar:')],
                    [sg.InputText()], [sg.Text('Digite a senha:')],
                    [sg.InputText()], [sg.Button('Deletar'), sg.Button('Voltar')]]

                deletar_window = sg.Window('Deletar chave', deletar_layout)
                while True:
                    deletar_event, deletar_value = deletar_window.read()
                    if deletar_event == sg.WIN_CLOSED or deletar_event == 'Voltar':
                        deletar_window.close()
                        break

                    if deletar_event == 'Deletar':
                        nome = deletar_value[0]
                        senha = deletar_value[1]
                        delete_keys(nome, senha)
                        sg.popup('Chave deletada com sucesso!')
                        deletar_window.close()
                        break

window.close()
