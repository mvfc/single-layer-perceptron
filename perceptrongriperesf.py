import random
import time

w = [
    0,
    0,
    0,
    0,
    0,
]

bias = random.random()

# Saida 1 = gripe, saida 0 = resfriado

entradas = [
    [1, 0, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 1, 0],
]

def teste(i):
    somatorio = bias*w[0]+entradas[i][0]*w[1]+entradas[i][1]*w[2]+entradas[i][2]*w[3]+entradas[i][3]*w[4]
    return somatorio

def learning(p, erro):
    for y in range (4):
        w[y+1] = w[y+1] + (erro * bias * entradas[p][y])
flag = 0

nrvezes = input('Numero de iteracoes\n')

for x in range (int(nrvezes)):
    for p in range(6):
        tst = teste(p)
        if(tst > 0):
            saida = 1
        elif(tst <= 0):
            saida = 0
        print('virus', entradas[p][0])
        print('bacteria', entradas[p][1])
        print('dor de cabeca', entradas[p][2])
        print('corisa', entradas[p][3])
        if(saida == 1):
            print('###gripe', saida)
        elif(saida == 0):
            print('###resfriado', saida)
        print('saida esperada', entradas[p][2])
        print('######################')
        if(saida != entradas[p][2]):
            learning(p, (entradas[p][2] - saida))
            print('Aprendizado!')
            flag = flag + 1
        time.sleep(1)

print('!!!!!!!!!!!')
print('Aprendizado feito', flag, 'vezes')
