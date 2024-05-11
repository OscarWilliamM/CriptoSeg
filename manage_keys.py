#gerenciamento das chaves através da interface
from generator_keys import *
from cript_and_descript_text import *
from import_export_keys import *
import PySimpleGUI as sg
sg.theme('DarkAmber')

#tamanho da janela
sg.SetOptions(element_padding=(50, 50))
#botoes da janela principal
layout = [[sg.Text('Bem vindo ao gerenciador de chaves!')],
        [sg.Button('Gerar chaves'), sg.Button('Criptografar e Decifragem'), 
        sg.Button('Pesquisar chaves'), sg.Button('Sair')]]

window = sg.Window('Gerenciador de chaves', layout)

#loop de eventos
while True: 
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if event == 'Gerar chaves':
        gerar_layout = [[sg.Text('Digite o nome e a senha para a geração das chaves')],
            [sg.Text('Nome:'), sg.InputText()],
            [sg.Text('Senha:'), sg.InputText()],
            [sg.Button('Gerar'), sg.Button('Voltar')]]

        gerar_window = sg.Window('Gerar chaves', gerar_layout)

        while True:
            gerar_event, gerar_value = gerar_window.read()
            if gerar_event == sg.WIN_CLOSED or gerar_event == 'Voltar':
                break
            if gerar_event == 'Gerar':
                nome = gerar_value[0]
                senha = gerar_value[1]
                generate_keys(nome, senha)
                sg.Popup('Chaves geradas com sucesso!')
                gerar_window.close()
                window = sg.Window('Gerenciador de chaves', layout)
                break
        
window.close()

                
    