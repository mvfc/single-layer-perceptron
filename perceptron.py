import random

w = [
    0,
    0,
    0,
]

bias = 1

entradas = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 1],
    [1, 1, 1],
]

def teste(i):
    somatorio = bias*w[0]+entradas[i][0]*w[1]+entradas[i][1]*w[2]
    return somatorio

def learning(p, erro):
    for y in range (2):
        w[y+1] = w[y+1] + (erro * bias * entradas[p][y])

for x in range(500):
    for p in range(4):
        tst = teste(p)
        if(tst > 0):
            saida = 1
        elif(tst <= 0):
            saida = 0
        print('n1', entradas[p][0])
        print('n2', entradas[p][1])
        print('saida', saida)
        print('saida esperada', entradas[p][2])
        print('bias', bias)
        print('pesob', w[0])
        print('peso1', w[1])
        print('peso2', w[2])
        print('######################')
        if(saida != entradas[p][2]):
            learning(p, (entradas[p][2] - saida))
