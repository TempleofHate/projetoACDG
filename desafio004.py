import sys
n1 = float(input('Digite sua nota :'))
n2 = float(input('Digite sua outra nota :'))
soma = (n1 + n2)/2
if soma >= 8:
    print('Parabéns! Você passou de ano')
    sys.exit(0)
elif soma < 4:
    print('Você foi reprovado!')
    sys.exit(0)
else:
    print('Você vai precisar da prova final')
n3 = float(input('Digite a nota da sua prova final :'))
final = ((n1 + n2) + n3)/3
if final >=5:
    print('Parabéns, você foi aprovado')
else:
    print('Você foi reprovado!')
