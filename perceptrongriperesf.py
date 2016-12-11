import random
import time

start = time.clock()

w = [
    0,
    0,
    0,
    0,
    0,
]

bias = 1

# Saida 1 = gripe, saida 0 = resfriado

entradas = [
    [1, 0, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 1, 0],
]

entradasreal = [[random.randint(0, 1) for x in range(5)] for y in range(100)]

def teste(i):
    somatorio = bias*w[0]+entradas[i][0]*w[1]+entradas[i][1]*w[2]+entradas[i][2]*w[3]+entradas[i][3]*w[4]
    return somatorio

def testereal(i):
    somatorio = bias*w[0]+entradasreal[i][0]*w[1]+entradasreal[i][1]*w[2]+entradasreal[i][2]*w[3]+entradasreal[i][3]*w[4]
    return somatorio

def learning(p, erro):
    for y in range (4):
        w[y+1] = w[y+1] + (erro * bias * entradas[p][y])
flag = 0

for p in range (500):
    if(flag < 2):
        for p in range(6):
            print('####### Aprendizado ######\n')
            tst = teste(p)
            if(tst > 0):
                saida = 1
            elif(tst <= 0):
                saida = 0
            print('virus', entradas[p][0], 'peso 1 ', w[1])
            print('bacteria', entradas[p][1], 'peso 2 ', w[2])
            print('dor de cabeca', entradas[p][2], 'peso 3 ', w[3])
            print('corisa', entradas[p][3], 'peso 4 ', w[4])
            if(saida == 1):
                print('###gripe### ', saida)
            elif(saida == 0):
                print('###resfriado### ', saida)
            print('saida esperada', entradas[p][4])
            print('####### Aprendizado ######\n')
            if(saida != entradas[p][4]):
                learning(p, (entradas[p][4] - saida))
                print('Aprendizado!\n')
                flag = flag + 1
            now = time.clock()
            print('Rodando por ', int(now - start), 'segundos')
            print('Aprendizado feito', flag, 'vezes')
            #time.sleep(0.5)
    else:
        for p in range(100):
            print('########## Fase 2 ############\n')
            tst = testereal(p)
            if (tst > 0):
                saida = 1
            elif (tst <= 0):
                saida = 0
            print('virus', entradasreal[p][0], 'peso 1 ', w[1])
            print('bacteria', entradasreal[p][1], 'peso 2 ', w[2])
            print('dor de cabeca', entradasreal[p][2], 'peso 3 ', w[3])
            print('corisa', entradasreal[p][3], 'peso 4 ', w[4])
            if (saida == 1):
                print('%%gripe%% ', saida)
            elif (saida == 0):
                print('%%resfriado%% ', saida)
            entradasreal[p][4] = saida
            print('########## Fase 2 ############\n')
            now = time.clock()
            print('Rodando por ', int(now - start), 'segundos')
            #time.sleep(0.5)
