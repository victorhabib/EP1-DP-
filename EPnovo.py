# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 16:06:46 2018

@author: Lipe e Bib
"""

cardapio = {"Sanduíche":12.00, "Suco":6.20, "Nescau":4.50, "Açaí":11.90, "Bib":2.00}
comanda = {}
dicdecomandas = {}

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
                        
        while z != 0:

            if z == 1:
                print("Você selecionou a opção: Adicionar Comanda")
                numcomanda = int(input("Qual o número da mesa?"))
                print("\n")
                dicdecomandas[numcomanda] = comanda
                
                print("Comanda Adicionada.")
                print("Você voltou para o Menu de Comandas")
                print("\n")
                print("Menu de Comandas")
                print("0 - Sair do Menu de Comandas")
                print("1 - Adicionar Comanda")
                print("2 - Remover Comanda")
                print("3 - Acessar Comanda")
                print("4 - Ver comandas já adicionadas")
                z = int(input("Faça sua escolha:"))
                
            if z == 2:
                print("Você selecionou a opção: Remover Comanda")
                for e in dicdecomandas:
                    print(e)
                numcomanda = int(input("Qual o número da mesa?"))
                print("\n")
                del dicdecomandas[numcomanda]
                
                print("Comanda Removida.")
                print("Você voltou para o Menu de Comandas")
                print("\n")
                print("Menu de Comandas")
                print("0 - Sair do Menu de Comandas")
                print("1 - Adicionar Comanda")
                print("2 - Remover Comanda")
                print("3 - Acessar Comanda")
                print("4 - Ver comandas já adicionadas")
                z = int(input("Faça sua escolha:"))
                
            if z == 3:
                print("Você selecionou a opção: Acessar Comanda")
                numcomanda = int(input("Qual o número da mesa a ser acessada?"))
                
                if numcomanda not in dicdecomandas:
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
                            for h in cardapio:
                                print("{0} (R${1:.2f})".format(h, cardapio[h]))
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
                            quantidade = float(input("Qual a quantidade pedida?"))
                            if produto not in cardapio:
                                print("O produto requisitado não pode ser adquirido nesse comércio.")
                                print("\n")
                                print("Comanda Eletrônica")
                                print("0 - Sair da Comanda Eletrônica")
                                print("1 - Imprimir Cardápio")
                                print("2 - Adicionar Item à Comanda")
                                print("3 - Remover Item da Comanda")
                                print("4 - Imprimir Comanda")
                                e = int(input("Faça sua escolha:"))
                            elif produto in cardapio and produto not in comanda:
                                comanda[produto] = quantidade
                                print("\n")
                                print("Comanda Eletrônica")
                                print("0 - Sair da Comanda Eletrônica")
                                print("1 - Imprimir Cardápio")
                                print("2 - Adicionar Item à Comanda")
                                print("3 - Remover Item da Comanda")
                                print("4 - Imprimir Comanda")
                                e = int(input("Faça sua escolha:"))
                            else:
                                comanda[produto] += quantidade
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
                            quantidade2 = int(input("Qual a quantidade a ser removida?"))
                            
                            while quantidade2 < 0 or quantidade2 > comanda[produto]:
                                if quantidade2 > comanda[produto2]:
                                    print("Não é possível remover quantidade maior do que a quantidade presente na comanda.")
                                    print("O máximo a ser removido: {}".format(comanda[produto]))
                                    
                                else:
                                    print("Não é possível remover quantidade negativa.")
                                quantidade2 = int(input("Qual a quantidade a ser removida?"))
                                
                            comanda[produto2] -= quantidade2
                            print("\n")
                            print("Comanda Eletrônica")
                            print("0 - Sair da Comanda Eletrônica")
                            print("1 - Imprimir Cardápio")
                            print("2 - Adicionar Item à Comanda")
                            print("3 - Remover Item da Comanda")
                            print("4 - Imprimir Comanda")
                            e = int(input("Faça sua escolha:"))
                            
                        elif e == 4:
                            if len(comanda) == 0:
                                print("Não há produtos na comanda.")
                            else:
                                print("A comanda possui os seguintes itens:")
                                print("\n")
                                precototalcomanda = 0
                                for h in comanda:
                                    precosomaprod = cardapio[h] * comanda[h]
                                    precototalcomanda += precosomaprod
                                    print("{0}, quantidade: {1}".format(h, comanda[h]))
                                    print("Preço unitário: {0:.2f}".format(cardapio[h]))
                                    print("Preço total dos produtos: {1:.2f} reais".format(h, precosomaprod))
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
                    
            if z == 4:
                print("Você selecionou a opção: imprimir o número das mesas já adicionadas")
                if dicdecomandas == {}:
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
                    for a in dicdecomandas:
                        print("Mesa de número: {}".format(a))
                    print("\n")
                    print("Menu de Comandas")
                    print("0 - Sair do Menu de Comandas")
                    print("1 - Adicionar Comanda")
                    print("2 - Remover Comanda")
                    print("3 - Acessar Comanda")
                    print("4 - Ver comandas já adicionadas")
                    z = int(input("Faça sua escolha:"))
                
    

    elif x == 2:
        print("O cardápio possui os seguintes itens:")
        for h in cardapio:
            print("{0} (R${1:.2f})".format(h, cardapio[h]))
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
        item1preco = float(input('Qual o preço unitário do item?'))
        
        if item1 not in cardapio:
            cardapio[item1] = item1preco
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
                cardapio[item1] = item1preconovo
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
        del cardapio[item1]
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
        item1preconovo = float(input('Qual o novo preço unitário do item?'))
        cardapio[item1] = item1preconovo
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















