# Serialização de Dados 
# 
#  Objeto Python      pickle    
#     [] (Lista)    --------->  (ARQUIVO)
#                     dump   (serialização)
#
#    [] (Lista)     <---------   (ARQUIVO)
#                     load   (desserialização)

import pickle

lista = ["Ana", "joao", "maria"]
arquivo = open("dados.dat", "wb")
pickle.dump(lista, arquivo)
arquivo.close()