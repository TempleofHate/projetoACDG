import array
x = []
x.append(int(input('Digite um valor: ')))
x.append(int(input('Digite um valor: ')))
x.append(int(input('Digite um valor: ')))
x.append(int(input('Digite um valor: ')))
print(x)
y = []
y.append(int(input('Digite um valor: ')))
y.append(int(input('Digite outro valor: ')))
y.append(int(input('Digite outro valor: ')))
y.append(int(input('Digite outro valor: ')))
print(y)

sum = sum(x,y)
print(sum)
sum = sum(x+y)
print(sum)



