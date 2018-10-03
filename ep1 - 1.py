# -*- coding: utf-8 -*-
"""
Spyder Editor

EP 1 - Felipe Machado e Victor Habib

@author: VICTOR HABIB
"""

#cardapio={'produto': valor}
cardapio={'bibzinho': 100, 'lipe': 50}
#comanda={'produto': quantidade}
comanda={'lipe': 5}

comanda_eletronica=['\nComanda eletrônica', '0 - sair', '1 - imprimir cardápio', '2 - adicionar item', '3 - remover item', '4 - imprimir comanda']

for c_e in comanda_eletronica:
    print(c_e)
escolha=int(input('O que deseja fazer? '))


while escolha!=0:
    
    
#imprimir o cardápio  
    
    

    if escolha==1:
        #imprimir cardapio
        print('\nCARDÁPIO')
        for i in cardapio:
            print('{0}: R${1:.2f}'.format(i, cardapio[i]))
        for c_e in comanda_eletronica:
            print(c_e)
        escolha=int(input('O que deseja fazer? '))
    
    
#adicionar item na comanda 
    
    
    elif escolha==2:
        #adicionar item
        produto=input('Produto que deseja adicionar na comanda: ')
        if produto not in cardapio:
            print('O item {0} não está no cardápio'.format(produto))
        else:
            if produto not in comanda:
                print('{0} foi adicionado na comanda.'.format(produto))
                quantidade=int(input('Quantidade de {0} que deseja adicionar: '.format(produto)))
                while quantidade<0:
                    print('Não é possível adicionar quantidade negativa.')
                    quantidade=int(input('Quantidade de {0} que deseja adicionar: '.format(produto)))
                comanda[produto]=quantidade
                print('Quantidade atual de {0} na comanda: {1}'.format(produto, quantidade))
            else:
                quantidade=int(input('Quantidade de {0} que deseja adicionar a mais: '.format(produto)))
                comanda[produto]+=quantidade
                print('Quantidade atual de {0} na comanda: {1}'.format(produto, comanda[produto]))
        for c_e in comanda_eletronica:
            print(c_e)
        escolha=int(input('O que deseja fazer? '))
        
                

#remover item da comanda
        

      
    elif escolha==3:
        #remover item
        produto=input('Nome do produto: ')
        if produto not in comanda:
            print('{0} não foi encontrado na comanda.'.format(produto))
        else:
            quantidade=int(input('Quantidade de {0} que deseja remover da comanda: '.format(produto)))
            while quantidade<=0 or quantidade>comanda[produto]:
                if quantidade<=0:
                    print('Não é possível remover quantidade não positiva.')
                elif quantidade>comanda[produto]:
                    print('Não é possível remover quantidade maior do que a quantidade presente na comanda.')
                    print('Máximo a ser removido: {0}'.format(comanda[produto]))
                quantidade=int(input('Quantidade de {0} que deseja remover da comanda: '.format(produto)))
            comanda[produto]-=quantidade
            print('Quantidade atual de {0}: {1}'.format(produto, comanda[produto]))
        for c_e in comanda_eletronica:
            print(c_e)
        escolha=int(input('O que deseja fazer? '))
        
        
#imprimir comanda
        
        
    elif escolha==4:
        #imprimir comanda
        for i in comanda:
            print('{0}: {1}'.format(i, comanda[i]))
        for c_e in comanda_eletronica:
            print(c_e)
        escolha=int(input('O que deseja fazer? '))

        
    else:
        print('Esta opção não existe')
        for c_e in comanda_eletronica:
            print(c_e)
        escolha=int(input('O que deseja fazer? '))

print('Até mais')


    
