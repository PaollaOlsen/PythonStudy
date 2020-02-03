a = 10

b = 3

print(a + b)  # adição
print(a - b)  # subtação
print(a ** b)  # potencia
print(a * b)  # multiplicação
print(a / b)  # divisão
print(a // b)  # divisão
print(a % b)  # retorna o resto da divisão

print(a > b)  # maior que
print(a < b)  # menor que
print(a == b)  # igual
print(a != b)  # diferente
print(a >= b)  # maior ou igual
print(a <= b)  # menor ou igual

print(a and b)  # pode usar &
print(a or b)  # pode usar |
print(not a)  # pode usar ~
print(a ^ b)  # equilave ao XOR - um ou outro mas não ambos

x = a + b
a += b  # a = a + b
a -= b  # a = a - b
a *= b  # a = a * b
a /= b  # a = a / b
a //= b  # a = a // b
a %= b  # a = a % b
a **= b  # a = a ** b
# a &= b  # a = a & b - a tem que ser boleano
# a |= b  # a = a | b - a tem que ser boleano

print(a is not b)  # não é
print(a is b)  # é
# print(a in b)  # está em - a precisa ser uma lista
# print(a not in b)  # não está - a precisa ser uma lista

if(a > b):
    print('a maior que b')
elif (a < b):
    print('b menor que a')
else:
    print('b = a')

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = range(0, 20, 2)

for i in lista:
    print(i)

for i in lista2:
    print(i)

length = len(lista)
i = 0

while i < length:
    print(lista[i])
    i += 1
