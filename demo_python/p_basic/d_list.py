#!/usr/bin/python

lista = [10,20,30,40]

print lista
del(lista[0])
print lista
lista.remove(40)
print lista

#find if 20 in lista
x = 20 in lista
print x

list_struct = []
# could not be like this
#list_struct.append(10,1)
print list_struct

lista.append(-4)
lista.append(-5)
lista.append(-6)
print lista
