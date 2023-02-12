# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
print('-------- TABUADA --------')

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if num <= 0:
        break
    for cont in range (1, 11):
        print(f'{num} x {cont} = {num * cont}')
        cont += 1
    print('-' * 30)
print('Tabuada Encerrada!')
