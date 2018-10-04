# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 23:41:29 2018

@author: VICTOR HABIB
"""

import json
with open("arquivo_ep.json" , "r") as entrada:
    dicionario_tudo = json.loads(entrada.read())
    
#cardapio = {"Sanduíche":12.00, "Suco":6.20, "Nescau":4.50, "Açaí":11.90, "Bib":2.00}
#comanda = {}
#dicdecomandas = {}

print("Bem-vindo ao Programa Lipib")
print("Aqui é possível organizar o seu trabalho, de modo a facilitar o mesmo.")
print("\n")

print("Menu Inicial")
print("0 - Sair do Menu Inicial")
print("1 - Acessar Comandas Eletrônicas")
print("2 - Imprimir Cardápio")
print("3 - Adicionar item ao Cardápio")
print("4 - Remover item do Cardápio")
print("5 - Alterar item do Cardápio")
x = int(input("Faça sua escolha:"))

while x != 0:
    if x == 1:
        print("Menu de Comandas")
        print("0 - Sair do Menu de Comandas")
        print("1 - Adicionar Comanda")
        print("2 - Remover Comanda")
        print("3 - Acessar Comanda")
        print("4 - Ver comandas já adicionadas")
        z = int(input("Faça sua escolha:"))
                        
        while z != 0:
            
            if z == 1:
                print("Você selecionou a opção: Adicionar Comanda")
                numcomanda = input("Qual o número da mesa?")
                print("\n")
                if numcomanda not in dicionario_tudo["dicdecomandas"]:
                    dicionario_tudo["dicdecomandas"][numcomanda] = {}
                    print("Comanda Adicionada.")
                else:
                    print("Mesa {0} já se encontra cadastrada no sistema".format(numcomanda))
                print("Você voltou para o Menu de Comandas")
                print("\n")
                print("Menu de Comandas")
                print("0 - Sair do Menu de Comandas")
                print("1 - Adicionar Comanda")
                print("2 - Remover Comanda")
                print("3 - Acessar Comanda")
                print("4 - Ver comandas já adicionadas")
                z = int(input("Faça sua escolha:"))
                
            elif z == 2:
                print("Você selecionou a opção: Remover Comanda")
                print("Mesas cadastradas:")
                for e in dicionario_tudo["dicdecomandas"]:
                    print(e)
                numcomanda = input("Qual o número da mesa?")
                if numcomanda not in dicionario_tudo["dicdecomandas"]:
                    print("Mesa não encontrada")
                else:
                    del dicionario_tudo["dicdecomandas"][numcomanda]
                    print("Mesa {0} deletada".format(numcomanda))
                    print("Comanda Removida.")
                print("\n")
                print("Você voltou para o Menu de Comandas")
                print("\n")
                print("Menu de Comandas")
                print("0 - Sair do Menu de Comandas")
                print("1 - Adicionar Comanda")
                print("2 - Remover Comanda")
                print("3 - Acessar Comanda")
                print("4 - Ver comandas já adicionadas")
                z = int(input("Faça sua escolha:"))
                
            elif z == 3:
                print("Você selecionou a opção: Acessar Comanda")
                print("Mesas cadastradas:")
                for e in dicionario_tudo["dicdecomandas"]:
                    print(e)
                numcomanda = input("Qual o número da mesa a ser acessada?")
                
                if numcomanda not in dicionario_tudo["dicdecomandas"]:
                    print("A mesa não está no sistema.")
                    print("\n")
                    print("Menu de Comandas")
                    print("0 - Sair do Menu de Comandas")
                    print("1 - Adicionar Comanda")
                    print("2 - Remover Comanda")
                    print("3 - Acessar Comanda")
                    print("4 - Ver comandas já adicionadas")
                    z = int(input("Faça sua escolha:"))
                    
                else:
                    print("Você acessou a comanda da mesa de número: {}".format(numcomanda))
                    print("\n")
                    
                    print("Comanda Eletrônica")
                    print("0 - Sair da Comanda Eletrônica")
                    print("1 - Imprimir Cardápio")
                    print("2 - Adicionar Item à Comanda")
                    print("3 - Remover Item da Comanda")
                    print("4 - Imprimir Comanda")
                    e = int(input("Faça sua escolha:"))
                    print("\n")
                
                    while e != 0:
                        if e == 1:
                            print("O cardápio possui os seguintes itens:")
                            for h in dicionario_tudo["cardapio"]:
                                print("{0} (R${1:.2f})".format(h, dicionario_tudo["cardapio"][h]))
                            print("\n")
                            print("Comanda Eletrônica")
                            print("0 - Sair da Comanda Eletrônica")
                            print("1 - Imprimir Cardápio")
                            print("2 - Adicionar Item à Comanda")
                            print("3 - Remover Item da Comanda")
                            print("4 - Imprimir Comanda")
                            e = int(input("Faça sua escolha:"))
                            
                        elif e == 2:
                            print("Você selecionou a opção Adicionar Item.")
                            produto = input("Qual o nome do item a ser adicionado?")
                            if produto not in dicionario_tudo["cardapio"]:
                                print("O produto requisitado não pode ser adquirido nesse comércio.")
                                print("\n")
                                print("Comanda Eletrônica")
                                print("0 - Sair da Comanda Eletrônica")
                                print("1 - Imprimir Cardápio")
                                print("2 - Adicionar Item à Comanda")
                                print("3 - Remover Item da Comanda")
                                print("4 - Imprimir Comanda")
                                e = int(input("Faça sua escolha:"))
                            elif produto in dicionario_tudo["cardapio"] and produto not in dicionario_tudo["dicdecomandas"][numcomanda]:
                                quantidade = float(input("Qual a quantidade pedida?"))
                                dicionario_tudo["dicdecomandas"][numcomanda][produto] = quantidade
                                print("\n")
                                print("Comanda Eletrônica")
                                print("0 - Sair da Comanda Eletrônica")
                                print("1 - Imprimir Cardápio")
                                print("2 - Adicionar Item à Comanda")
                                print("3 - Remover Item da Comanda")
                                print("4 - Imprimir Comanda")
                                e = int(input("Faça sua escolha:"))
                            else:
                                quantidade = float(input("Qual a quantidade pedida?"))
                                dicionario_tudo["dicdecomandas"][numcomanda][produto] += quantidade
                                print("\n")
                                print("Comanda Eletrônica")
                                print("0 - Sair da Comanda Eletrônica")
                                print("1 - Imprimir Cardápio")
                                print("2 - Adicionar Item à Comanda")
                                print("3 - Remover Item da Comanda")
                                print("4 - Imprimir Comanda")
                                e = int(input("Faça sua escolha:"))
                                
                        elif e == 3:
                            print("Você selecionou a opção Remover Item.")
                            produto2 = input("Qual o nome do item a ser removido?")
                            if produto2 not in dicionario_tudo["dicdecomandas"][numcomanda]:
                                print("Produto não encontrado nesta comanda")
                            else:
                                quantidade2 = int(input("Qual a quantidade a ser removida?"))
                                while quantidade2 < 0 or quantidade2 > dicionario_tudo["dicdecomandas"][numcomanda][produto]:
                                    if quantidade2 > dicionario_tudo["dicdecomandas"][numcomanda][produto2]:
                                        print("Não é possível remover quantidade maior do que a quantidade presente na comanda.")
                                        print("O máximo a ser removido: {}".format(dicionario_tudo["dicdecomandas"][numcomanda][produto]))
                                    
                                    else:
                                        print("Não é possível remover quantidade negativa.")
                                    quantidade2 = int(input("Qual a quantidade a ser removida?"))
                                
                                dicionario_tudo["dicdecomandas"][numcomanda][produto2] -= quantidade2
                            print("\n")
                            print("Comanda Eletrônica")
                            print("0 - Sair da Comanda Eletrônica")
                            print("1 - Imprimir Cardápio")
                            print("2 - Adicionar Item à Comanda")
                            print("3 - Remover Item da Comanda")
                            print("4 - Imprimir Comanda")
                            e = int(input("Faça sua escolha:"))
                            
                        elif e == 4:
                            if len(dicionario_tudo["dicdecomandas"][numcomanda]) == 0:
                                print("Não há produtos na comanda.")
                            else:
                                print("A comanda possui os seguintes itens:")
                                print("\n")
                                precototalcomanda = 0
                                for h in dicionario_tudo["dicdecomandas"][numcomanda]:
                                    precosomaprod = dicionario_tudo["cardapio"][h] * dicionario_tudo["dicdecomandas"][numcomanda][h]
                                    precototalcomanda += precosomaprod
                                    print("{0}:".format(h))
                                    print("\tQuantidade: {0}".format(dicionario_tudo["dicdecomandas"][numcomanda][h]))
                                    print("\tPreço unitário: {0:.2f}".format(dicionario_tudo["cardapio"][h]))
                                    print("\tPreço total dos produtos: {0:.2f} reais".format(precosomaprod))
                                    print("\n")
                                print("Preço total da comanda: {0:.2f} reais".format(precototalcomanda))
                                print("Preço total da comanda (c/ 10%): {0:.2f} reais".format(precototalcomanda*1.1))
                                
                            print("\n")
                            print("Comanda Eletrônica")
                            print("0 - Sair da Comanda Eletrônica")
                            print("1 - Imprimir Cardápio")
                            print("2 - Adicionar Item à Comanda")
                            print("3 - Remover Item da Comanda")
                            print("4 - Imprimir Comanda")
                            e = int(input("Faça sua escolha:"))
                    
                    if e == 0:
                        print("Menu de Comandas")
                        print("0 - Sair do Menu de Comandas")
                        print("1 - Adicionar Comanda")
                        print("2 - Remover Comanda")
                        print("3 - Acessar Comanda")
                        print("4 - Ver comandas já adicionadas")
                        z = int(input("Faça sua escolha:"))
                    
            elif z == 4:
                print("Você selecionou a opção: imprimir o número das mesas já adicionadas")
                if dicionario_tudo["dicdecomandas"] == {}:
                    print("Não há comandas adicionadas.")
                    print("\n")
                    print("Menu de Comandas")
                    print("0 - Sair do Menu de Comandas")
                    print("1 - Adicionar Comanda")
                    print("2 - Remover Comanda")
                    print("3 - Acessar Comanda")
                    print("4 - Ver comandas já adicionadas")
                    z = int(input("Faça sua escolha:"))
                else:
                    print("Comandas já adicionadas:")
                    for a in dicionario_tudo["dicdecomandas"]:
                        print("Mesa de número: {}".format(a))
                    print("\n")
                    print("Menu de Comandas")
                    print("0 - Sair do Menu de Comandas")
                    print("1 - Adicionar Comanda")
                    print("2 - Remover Comanda")
                    print("3 - Acessar Comanda")
                    print("4 - Ver comandas já adicionadas")
                    z = int(input("Faça sua escolha:"))
                
        if z == 0:
            print("Você saiu do Menu de Comandas:")
            print("\n")
            print("Menu Inicial")
            print("0 - Sair do Menu Inicial")
            print("1 - Acessar Comandas Eletrônicas")
            print("2 - Imprimir Cardápio")
            print("3 - Adicionar item ao Cardápio")
            print("4 - Remover item do Cardápio")
            print("5 - Alterar item do Cardápio")
            x = int(input("Faça sua escolha:"))
    

    elif x == 2:
        print("O cardápio possui os seguintes itens:")
        for h in dicionario_tudo["cardapio"]:
            print("{0} (R${1:.2f})".format(h, dicionario_tudo["cardapio"][h]))
        print("\n")
        print("Menu Inicial")
        print("0 - Sair do Menu Principal")
        print("1 - Acessar Comanda Eletrônica")
        print("2 - Imprimir Cardápio")
        print("3 - Adicionar item ao Cardápio")
        print("4 - Remover item do Cardápio")
        print("5 - Alterar item do Cardápio")
        x = int(input("Faça sua escolha:"))
        
    elif x == 3:
        print("Você escolheu a opção 3: Adicionar Item ao Cardápio")
        item1 = input('Qual o item a ser adicionado no cardápio?')
        
        
        if item1 not in dicionario_tudo["cardapio"]:
            item1preco = float(input('Qual o preço unitário do item?'))
            while item1preco <=0:
                print("Valor precisa ser positivo")
                item1preco = float(input('Qual o preço unitário do item?'))                            
            dicionario_tudo["cardapio"][item1] = item1preco
            print("\n")
            print("Menu Inicial")
            print("0 - Sair do Menu Principal")
            print("1 - Acessar Comanda Eletrônica")
            print("2 - Imprimir Cardápio")
            print("3 - Adicionar item ao Cardápio")
            print("4 - Remover item do Cardápio")
            print("5 - Alterar item do Cardápio")
            x = int(input("Faça sua escolha:"))
            
        else:
            print('O produto já está no cardápio.')
            print("0 - Voltar para o Menu Inicial.")
            print("1 - Alterar preço do produto.")
            alterar = int(input("Faça sua escolha:"))
            
            if alterar == 1:
                item1preconovo = float(input('Qual o novo preço unitário do item?'))
                dicionario_tudo["cardapio"][item1] = item1preconovo
                print("\n")
                print("Menu Inicial")
                print("0 - Sair do Menu Principal")
                print("1 - Acessar Comanda Eletrônica")
                print("2 - Imprimir Cardápio")
                print("3 - Adicionar item ao Cardápio")
                print("4 - Remover item do Cardápio")
                print("5 - Alterar item do Cardápio")
                x = int(input("Faça sua escolha:"))
                
            else:
                print("\n")
                print("Menu Inicial")
                print("0 - Sair do Menu Principal")
                print("1 - Acessar Comanda Eletrônica")
                print("2 - Imprimir Cardápio")
                print("3 - Adicionar item ao Cardápio")
                print("4 - Remover item do Cardápio")
                print("5 - Alterar item do Cardápio")
                x = int(input("Faça sua escolha:"))

    elif x == 4:
        print("Você escolheu a opção 4: Remover Item do Cardápio")
        item1 = input('Qual o item a ser removido do cardápio?')
        if item1 not in dicionario_tudo["cardapio"]:
            print("Produto não se encontra no cardápio")
        else:
            del dicionario_tudo["cardapio"][item1]
            print("{0} não se encontra mais no cardápio".format(item1))
        print("\n")
        print("Menu Inicial")
        print("0 - Sair do Menu Principal")
        print("1 - Acessar Comanda Eletrônica")
        print("2 - Imprimir Cardápio")
        print("3 - Adicionar item ao Cardápio")
        print("4 - Remover item do Cardápio")
        print("5 - Alterar item do Cardápio")
        x = int(input("Faça sua escolha:"))
        
    elif x == 5:
        print("Você escolheu a opção 5: Alterar preço de item do cardápio")
        item1 = input('Qual o item a ser alterado?')
        if item1 not in dicionario_tudo["cardapio"]:
            print("Produto não se encontra no cardápio")
        else:
            item1preconovo = float(input('Qual o novo preço unitário do item?'))
            dicionario_tudo["cardapio"][item1] = item1preconovo
            print("Novo preço de {0}: {1:.2f}".format(item1, item1preconovo))
        print("\n")
        print("Menu Inicial")
        print("0 - Sair do Menu Principal")
        print("1 - Acessar Comanda Eletrônica")
        print("2 - Imprimir Cardápio")
        print("3 - Adicionar item ao Cardápio")
        print("4 - Remover item do Cardápio")
        print("5 - Alterar item do Cardápio")
        x = int(input("Faça sua escolha:"))
        
print("Você saiu do Menu Inicial.")
print("Até mais.")

ble_json = json.dumps(dicionario_tudo, sort_keys = True , indent=4)
with open("arquivo_ep.json" , "w") as saida:
    saida.write(ble_json)

with open("arquivo_ep.json", "w") as entrada:
    entrada.write(json.dumps(dicionario_tudo, sort_keys=True, indent=4)) 
