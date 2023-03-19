#### Listas
lista_enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
iterador = iter(lista_enteros)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
# lista_numeros = [0.1, 0.2, 0.3]
# lista_strings = ['Diego', 'Fernando']
# lista_booleanos = [True, False, False]
# lista = ['Diego', 34, True]
# lista = ['Fernando', 21, False]


# print(lista_enteros.index(7))
# print(lista_enteros[len(lista_enteros)-1])
# print(lista_enteros[-1])

# lista = [3, 'Hola', True] 
# lista[0] = 7
# # # lista.append(3)
# # # lista.append(4)
# print(lista)

# lista = [6, 4, 1, 9, 7, 0, 5]
# elemento = lista.pop(3)
# print(elemento)
# print(lista)


# lista.insert(2, 'Adiós')
# print(lista.index('Hola'))

# for elemento in lista:
#   if type(elemento) == str:
#     print(f'Nombre: {elemento}')
#   elif type(elemento) == int:
#     print(f'Edad: {elemento}') 
#   elif elemento == True:
#     print('Soltero')   
#   else:
#     print('Casado')  
    



# # No es una buena practica
# print(lista_enteros[0]*2)
# print(lista_enteros[1]*2)
# print(lista_enteros[2]*2)
# print(lista_enteros[3]*2)
# print(lista_enteros[4]*2)

# print(type(lista[0]) == str)
# print(type(lista[1]) == int)
# print(type(lista[2]) == bool)

# Operaciones con listas
# Ciclos repetitivos (For, While)
# # For
# for elemento in lista_enteros:
#   print(elemento)

# for i in range(1, 11):
#   print(f"\nTabla de multiplicar del {i}")
#   for j in range(1, 21):
#     print(f"{i} x {j} = {i * j}")

# # While
# n = 0
# while n < len(lista_enteros):
#   print(lista_enteros[n])
#   n += 1


# primer_elemento = lista_enteros[0]
# print(f'El primer elemento de la lista es: {lista_enteros[0]}')
# print(f'El numero de elementos en la lista es: {len(lista_enteros)}')
# print(f'El último elemento de la lista es: {lista_enteros[len(lista_enteros)-1]}')

# print(f'El primer elemento de la lista de numeros es: {lista_numeros[0]}');
# print(f'El ultimo elemento de la lista de numeros es: {lista_numeros[len(lista_numeros)-1]}');

# ### Tuplas
# generos = 'masculino', 'femenino'
# provincias = 'azuay', 'guayas', 'loja'
# print(generos)


### Diccionarios
# cliente = {
#   'Nombre': 'Diego',
#   'Apellido': 'Carrera',
#   'Edad': 34,
#   'Estado civil': 'S',
#   'cedula': 99999999999
# }

# print(sorted(cliente))

# for clave in cliente.keys():
#   for valor in cliente.values():
#     print(f'{clave} {valor}')





# for clave in cliente.keys():
#   print(clave)

# for valor in cliente.values():
#   print(valor)  

# print(cliente.keys())
# print(cliente.values())

# for clave in cliente.keys():

# print(cliente['cedula'])

### Conjuntos
# lista_enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 3, 2, 5, 7, 9]
# conjunto = set(lista_enteros)
# print(conjunto)

# conjunto1 = {1, 2, 3, 2, 1}
# print(1 in conjunto1)
# print(f'Conjunto 1: {conjunto1}')
# conjunto2 = {3, 4, 5}
# print(f'Conjunto 2: {conjunto2}')
# # print(conjunto1.union(conjunto2))
# print(f'Conjunto 1 union Conjunto 2: {conjunto1.union(conjunto2)}')
# print(f'Conjunto 1 interseccion Conjunto 2: {conjunto1.intersection(conjunto2)}')
# print(f'Conjunto 1 - Conjunto 2: {conjunto1.difference(conjunto2)}')
# print(f'Conjunto 2 - Conjunto 1: {conjunto2.difference(conjunto1)}')


### Condicionales

# print("Ingresa tu edad: ")
# numero = int(input())
# if (numero >= 18):
#   print("Adulto")
# else:
#   print("Menor de edad")  


# print("Escribe un número de 1 a 10")
# number = int(input())
# if (number > 5):
#   print("¡Soy mayor que 5!")
# elif (number == 5):
#   print("Soy el número 5")
# else:
#   print("Soy menor o igual que 5")




