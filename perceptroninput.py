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

def teste(i):
    somatorio = bias*w[0]+entradas[i][0]*w[1]+entradas[i][1]*w[2]+entradas[i][2]*w[3]+entradas[i][3]*w[4]
    return somatorio

def testeinput(a, b, c, d):
	somatorio = bias*w[0]+a*w[1]+b*w[2]+c*w[3]+d*w[4]
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
        print('\nDigite os dados\n')
        a = input('virus\n')
        b = input('bacteria\n')
        c = input('dor de cabeca\n')
        d = input('corisa\n')
        resultado = int(testeinput(int(a), int(b), int(c), int(d)))
        if(resultado > 0):
        	print('!!!gripe (1)')
        elif(resultado <= 0):
        	print('!!!resfriado(0)')
        time.sleep(1)
