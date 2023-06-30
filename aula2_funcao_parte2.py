# Continuação da aula01 - funções

# # Argumento com Valor Default
# def minha_quinta_funcao(arg="Batatinha frita"):
#     if type(arg) == int:
#         return arg * 1
#     elif type(arg) == str:
#         return arg.upper()
#     elif type(arg) == tuple:
#         return "é uma tupla."
#     elif type(arg) == bool:
#         return "Argumento Boleano."
#     else:
#         return "Tipo não identificado."
#
# #print(minha_quinta_funcao())
# resultado = minha_quinta_funcao()
# print(resultado)
# exit()










# # Multiplos Argumentos
# def minha_sexta_funcao(arg1,  arg3, arg2="--"):
#     print(arg1, arg2, arg3)
#     return "Deu tudo certo!"
#
# print(minha_sexta_funcao(22, 11, arg2="Tio Ivo" ))
# exit()
#

# # *args
# def minha_setima_funcao(*args):
#     print(type(args))
#     print(args[0][-3:].upper())
#     args[2][0] = "blablabla"
#     print(args)
#     for elemento in args:
#         print(f" >>{elemento}")
#
# minha_setima_funcao("Tio Ivo", "Tia Ana", [1,2,3,4])
# exit()




# # Misturando tudo
# def minha_oitava_funcao(arg1, *args, arg2, arg3, arg4):
#     print(arg1, arg2, arg3, arg4, args)
#
#
# minha_oitava_funcao("Obrigatório", [1, 2, 3, 4, 5], arg4=11, arg2=22, arg3=33)
#


# # **kwargs
# def minha_nona_funcao(**kwargs):
#     print(kwargs)
#     for chave in kwargs.values():
#         print(chave)
#
# minha_nona_funcao(k1=[1,2,3], k2=2, k3=3, k4=4)






# # Recursao
# def minha_decima_funcao(num, qt=0):
#     if num % 2 == 0:
#         num -= 2
#         qt += 1
#         if num == 0:
#             return qt
#         return minha_decima_funcao(num, qt)
#
#
# print(minha_decima_funcao(10))
#
# exit()












"""
Crie uma função que leia o nome de uma pessoa e mostre a mensagem:
' Um bom Ano Novo para nós <nome_da_pessoa>!'
"""

def cumprimento(nome):
    print(f' Um bom Ano Novo para nós {nome}!')
    print(f' Um bom Ano Novo para nós {input("Nome: ")}!')

cumprimento(input("Nome:: "))
exit()
