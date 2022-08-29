import numpy
import numpy as np

# Criar matriz e retorna a mesma para a main
def criaMatriz(inst):
    path = 'Matriz/datasets/' + inst + '.txt'
    data = np.loadtxt(path)
    return data

# obter dimenção da matriz
#e salva em um arquivo os resultados
def obtemDimen(insta, matriz):
    rows, columns = np.shape(matriz)
    print("instancia= ", insta)
    print('Linhas= ', rows)
    print('Colunas= ', columns)
    resultado = str(insta) + '\n' + 'Linhas= ' + str(rows) + '\n' + 'Colunas= ' + str(columns)
    salvaResultado(resultado)

#salva os resultados obtidos em arquivo
def salvaResultado(resultado):
    arquivo = open('Matriz/resultado/resultados', 'a+')
    arquivo.writelines('nome do arquivo: ' + resultado + '\n\n')
    arquivo.close()


