#Aluno = Lucas Dias Rosa - 2017020835
#Professor: Rafael Frinhani
#Data: 29/08/2022

#importações
from Matriz import Matriz as ma

if __name__ == '__main__':
    #para outros aquivos, mudar exemplo para o nome do arquivo desejado, os arquivos se encontram na pasta dataset
    #Arquivos: ponte, exemplo e zachary, basta substituir entre as apas simples
    inst = 'zacharyS'
    #cria a matriz a partir do arquivo
    matriz = ma.criaMatriz(inst)
    #salva em arquivo o nome, linhas e coluna da matriz no arquivo colocado e imprime na tela o numero de colunas e linhas
    resultado = ma.obtemDimen(inst, matriz)
  #  ma.salvaResultado(resultado)


