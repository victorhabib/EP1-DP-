# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 20:53:22 2018

@author: 2000
"""
cardapio = {"Sanduíche":12.00, "Suco":6.20, "Nescau":4.50, "Açaí":11.90}
comanda = {}

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
            print("{0} (R${1})".format(h, cardapio[h]))
        print("\n")
        print("Comanda Eletrônica")
        print("0 - Sair")
        print("1 - Imprimir Cardápio")
        print("2 - Adicionar Item")
        print("3 - Remover Item")
        print("4 - Imprimir Comanda")
        e = int(input("Faça sua escolha:"))
        
    elif e == 2:
        print("Você selecionou a opção Adicionar Item.")
        produto = input("Qual o nome do item a ser adicionado?")
        quantidade = float(input("Qual a quantidade pedida?"))
        if produto not in cardapio:
            print("O produto requisitado não pode ser adquirido nesse comércio.")
        elif produto in cardapio and produto not in comanda:
            comanda[produto] = quantidade
            print("\n")
            print("Comanda Eletrônica")
            print("0 - Sair")
            print("1 - Imprimir Cardápio")
            print("2 - Adicionar Item")
            print("3 - Remover Item")
            print("4 - Imprimir Comanda")
            e = int(input("Faça sua escolha:"))
        else:
            comanda[produto] += quantidade
            print("\n")
            print("Comanda Eletrônica")
            print("0 - Sair")
            print("1 - Imprimir Cardápio")
            print("2 - Adicionar Item")
            print("3 - Remover Item")
            print("4 - Imprimir Comanda")
            e = int(input("Faça sua escolha:"))
            
    elif e == 3:
        print("Você selecionou a opção Remover Item.")
        produto2 = input("Qual o nome do item a ser removido?")
        quantidade2 = int(input("Qual a quantidade a ser removida?"))
        if quantidade >= comanda:
            del comanda[produto2]
        else:
            comanda[produto2] -= quantidade2
        
    elif e == 4:
        if len(comanda) == 0:
            print("Não há produtos na comanda.")
        else:
            print("A comanda possui os seguintes itens:")
            for h in comanda:
                print("{0}, quantidade: {1}".format(h, comanda[h]))
        print("\n")
        print("Comanda Eletrônica")
        print("0 - Sair")
        print("1 - Imprimir Cardápio")
        print("2 - Adicionar Item")
        print("3 - Remover Item")
        print("4 - Imprimir Comanda")
        e = int(input("Faça sua escolha:"))

print("Até mais.")