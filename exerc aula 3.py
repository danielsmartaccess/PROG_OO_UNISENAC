lista_nomes   = ['Pedro',
                 'Ana',
                 'Guilherme',
                 'Carla',
                 'Julia',
                 'Maria',
                 'Valentina',
                 'Mariana',
                 'Debora',
                 'Augusta',
                 'Rosangela',
                 'Rafaela',
                 'Helena',
                 'Marco',
                 'Mauricio',
                 'Matheus']

lista_bebidas = ['CocaCola',
                 'Guarana',
                 'CocaCola',
                 'Pepsi',
                 'Sprite',
                 'Soda Limonada',
                 'Guarana',
                 'CocaCola',
                 'Fanta Laranja',
                 'Soda Limonada',
                 'Guarana',
                 'Pepsi',
                 'Soda Limonada',
                 'Guarana',
                 'Fanta Laranja',
                 'Pepsi']


'''
#exercício 1

def pessoas_que_gostam_da_bebida(bebida):
    if bebida in lista_bebidas:
        for i in range(len(lista_nomes)):
            if lista_bebidas[i] == bebida:
                print(lista_nomes[i])
    else:
        print('Bebida não encontrada')
    

bebida = 'Guarana' #parâmetro passado na mão
pessoas_que_gostam_da_bebida(bebida)


#exercício 2

def adicionar_pessoa_e_bebida(nome, bebida):
    lista_nomes.append(nome)
    lista_bebidas.append(bebida)
    
adicionar_pessoa_e_bebida('Pedro', 'Guarana')
adicionar_pessoa_e_bebida('Ana', 'Guarana')
adicionar_pessoa_e_bebida('Guilherme', 'Guarana')

print (lista_nomes, lista_bebidas)


#exercício 3

def bebida_mais_preferida():
    bebidas_contagem = ()
    for bebida in lista_bebidas:
        if bebida not in bebidas_contagem:
            bebidas_contagem[bebida] = 1
        else:
            bebidas_contagem[bebida] += 1
            bebida_mais_preferida = max(bebidas_contagem, key=bebidas_contagem.get)
            return bebida_mais_preferida
        '''

def bebida_mais_preferida():
    bebidas_contagem = []
    for bebida in lista_bebidas:
        encontrou = False
        for i in range(len(bebidas_contagem)):
            if bebidas_contagem[i][0] == bebida:
                bebidas_contagem[i] = (bebida, bebidas_contagem[i][1] + 1)
                encontrou = True
                break
        if not encontrou:
            bebidas_contagem.append((bebida, 1))
    bebidas_contagem.sort(key=lambda x: x[1], reverse=True)
    return bebidas_contagem[0][0]

print(bebida_mais_preferida())