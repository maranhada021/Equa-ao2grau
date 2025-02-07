
import math

print("Bem vindo,veja a resolução da sua equação de 2 grau")
while True:

    while True:
        a = input('digite A: ')

        try:
            a = int(a)
            break

        except:
            print('digite um numero inteiro!')
            continue

    if a == 0:

        num1 = False
        print("isto não é uma equação do 2 grau, tente novamente.")

        continue

    while True:

        b = input('digite B: ')

        try:
            b = int(b)
            break

        except:
            print('digite um numero inteiro!')
            continue

    while True:

        c = input('digite C: ')

        try:
            c = int(c)
            break

        except:
            print('digite um numero inteiro!')
            continue


    delta = (b**2) - (4 * a * c)

    print(f'Delta é raiz de {delta}.')

    if delta < 0:
        print("Não existem raízes reais para este numero")
        break

    if delta == 0:
            x1 = -b / (2 * a)
            print(f'x1 = {x1}')
            break
    else:
         delta = math.sqrt(delta)
         x1 = (-b + delta) / (2 * a)
         x2 = (-b - delta) / (2 * a)
         print (f'x1 = {x1:.4f}')
         print (f'x2 = {x2:.4f}')
         break 
       
