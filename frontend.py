import requests

rodando = True
modo = 1
url = "http://26.47.22.246:8000/"
#url = "https://localhost:8000/"

while rodando and modo != 0:
    try:
        if modo == 1:
            print("====INTERFACE FARMACIA====")
            print('1) Clientes\n2) Clientes preferenciais\n3) Sair\n\nEscolha uma opcao: ')
            x = input()
            if x == '1': modo = 2
            if x == '2': modo = 7
            if x == '3': rodando = False
        if modo == 2:
            print('1) Ver clientes\n2) Adicionar cliente\n3) Remover cliente\n4) Atualizar cliente\n5) Cancelar\n\nEscolha uma opcao: ')
            x = input()
            if x == '1': modo = 3
            if x == '2': modo = 4
            if x == '3': modo = 5
            if x == '4': modo = 6
            if x == '5': modo = 1
        if modo == 3:
            resposta = requests.get(url + "clientes")
            resposta = resposta.json()
            for i in resposta["data"]:
                print("======")
                print("Cliente " + str(i["id"]) + ":\nNome: " + i["nome"] + "\nEmail: " + i["email"] + "\nFixo: " + i["fixo"] + "\nCelular: " + i["celular"] + "\nCpf: " + i["cpf"])
                print("======")
            modo = 1
        if modo == 4:
            infos = {
            'nome' : '',
            'email': '',
            'fixo' : '',
            'celular' : '',
            'cpf' : ''
            }
            print('Nome do cliente')
            infos["nome"] = input()
            print('Email do cliente')
            infos['email'] = input()
            print('Fixo do cliente')
            infos['fixo'] = input()
            print('Celular do cliente')
            infos['celular'] = input()
            print('CPF do cliente')
            infos['cpf'] = input()
            resposta = requests.post(url + "clientes", json = infos)
            if resposta.status_code == 200: print("Envio bem sucedido!")
            else: print("Algo ocorreu, por favor tente novamente.")
            modo = 1
        if modo == 5:
            print('Digite o ID do cliente que deseja excluir:')
            uid = input()
            url_id = url + "clientes/" + uid
            resposta = requests.delete(url_id)
            if resposta.status_code == 200: print("Envio bem sucedido!")
            else: print("Algo ocorreu, por favor tente novamente.")
            modo = 1
        if modo == 6:
            print("ID do usuario para atualizar: ")
            uid = input()
            infos = {
            'nome' : '',
            'email': '',
            'fixo' : '',
            'celular' : '',
            'cpf' : ''
            }
            print('Nome do cliente')
            infos["nome"] = input()
            print('Email do cliente')
            infos['email'] = input()
            print('Fixo do cliente')
            infos['fixo'] = input()
            print('Celular do cliente')
            infos['celular'] = input()
            print('CPF do cliente')
            infos['cpf'] = input()
            resposta = requests.put(url + "clientes/" + uid, json = infos)
            if resposta.status_code == 200: print("Envio bem sucedido!")
            else: print("Algo ocorreu, por favor tente novamente.")
            print(resposta)
            modo = 1
        
        if modo == 7:
            print('1) Ver Clientes preferenciais\n2) Adicionar cliente preferencial\n3) Remover cliente preferencial\n4) Atualizar cliente preferencial\n5) Cancelar\n\nEscolha uma opcao: ')
            x = input()
            if x == '1': modo = 8
            if x == '2': modo = 9
            if x == '3': modo = 10
            if x == '4': modo = 11
            if x == '5': modo = 1
        if modo == 8:
            resposta = requests.get(url + "clientespreferenciais")
            resposta = resposta.json()
            for i in resposta["data"]:
                print("======")
                print("Cliente preferencial " + str(i["id"]) + ":\nNome: " + i["nome"] + "\nEmail: " + i["email"] + "\nFixo: " + i["fixo"] + "\nCelular: " + i["celular"] + "\nCpf: " + i["cpf"] + "\nDesconto: " + str(i["desconto"]))
                print("======")
            modo = 1
        if modo == 9:
            infos = {
            'nome' : '',
            'email': '',
            'fixo' : '',
            'celular' : '',
            'cpf' : '',
            'desconto' : ''
            }
            print('Nome do cliente preferencial')
            infos["nome"] = input()
            print('Email do cliente preferencial')
            infos['email'] = input()
            print('Fixo do cliente preferencial')
            infos['fixo'] = input()
            print('Celular do cliente preferencial')
            infos['celular'] = input()
            print('CPF do cliente preferencial')
            infos['cpf'] = input()
            print('Desconto do cliente preferencial')
            infos['desconto'] = input()
            resposta = requests.post(url + "clientespreferenciais", json = infos)
            if resposta.status_code == 200: print("Envio bem sucedido!")
            else: print("Algo ocorreu, por favor tente novamente.")
            print(resposta)
            modo = 1
        if modo == 10:
            print('Digite o ID do cliente preferencial que deseja excluir:')
            uid = input()
            url_id = url + "clientespreferenciais/" + uid
            resposta = requests.delete(url_id)
            if resposta.status_code == 200: print("Envio bem sucedido!")
            else: print("Algo ocorreu, por favor tente novamente.")
            modo = 1
        if modo == 11:
            print("ID do cliente preferencial para atualizar: ")
            uid = input()
            infos = {
            'nome' : '',
            'email': '',
            'fixo' : '',
            'celular' : '',
            'cpf' : '',
            'desconto' : ''
            }
            print('Nome do cliente')
            infos["nome"] = input()
            print('Email do cliente')
            infos['email'] = input()
            print('Fixo do cliente')
            infos['fixo'] = input()
            print('Celular do cliente')
            infos['celular'] = input()
            print('CPF do cliente')
            infos['cpf'] = input()
            print('Desconto do cliente preferencial')
            infos['desconto'] = input()
            resposta = requests.put(url + "clientespreferenciais/" + uid, json = infos)
            if resposta.status_code == 200: print("Envio bem sucedido!")
            else: print("Algo ocorreu, por favor tente novamente.")
            print(resposta)
            modo = 1
    except:
        print("Algo ocorreu de errado, retornando ao menu.")
        modo = 1