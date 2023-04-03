import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.linalg import solve
lista = [i for i in range(1, 1000+1)]
x = np.array(lista)
y = []

for i in x:
  y.append(i**2+5)
  
print(f'x: {x}')  
print(f'x: {y}')

  

plt.plot(x, y, linewidth=3)
plt.show()
plt.savefig('grafica.png')

# valores = np.random.randn(10000)
# plt.hist(valores)
# plt.show()



# datos = pd.read_csv('datos.csv', names=['Telefono', 'Mensaje'])
# print(pd.DataFrame(datos) )

# diccionario = {'id_archivo': pd.Series([576, 577, 578], index =  [1, 2, 3]), 'id_detalle': pd.Series([279, 27, 266], index = [1, 2, 3] ), 'path': pd.Series(['c99bca69ab35d11ba7843c200.png', 'c99bca69ab35d11ba7843c201.png', 'c99bca69ab35d11ba7843c202.png'], index = [1, 2, 3]) }
# dataframe = pd.DataFrame(diccionario) 
# print(dataframe)
# print(dataframe.sort_values(by='id_detalle'))


# # Vector
# a = np.array([1, 2, 3, 4])
# b = np.array([7, 2, 5, 3])

# print('Maximo comun divisor')
# print(np.lcm(a, b))

# # Matriz rectangular
# R = np.array([[1, -1, -1], [2, -1, 1]]) # Matriz de 2 filas y 3 col.
# print('La matriz R: \n')
# print(R);    # Se visualiza la matriz R en la consola
# print('\n')  # Nueva línea

# # Vector columna
# print('El vector b: \n')
# print(b);    # Se visualiza el vector b en la consola
# b = np.array([[1], [2], [3]]) # Vector columna de 3 filas 
# print('\n')  # Nueva línea

# print('El producto Rb: \n')
# print(R@b)   # Se visualiza el producto de la matriz A por el vecto b en consola
# print('\n')  # Nueva línea

# # Matriz cuadrada
# A = np.array([[1, -1, -1], [2, -1, 1], [7, 9, 5]]) # Matriz de 3 filas y 3 col.
# print('La matriz A: \n')
# print(A);    # Se visualiza la matriz A en la consola
# print('\n')  # Nueva línea

# # Solución de un sistema de ecuaciones Ax = b
# print('El vector de incógnitas x del sistema Ax = b es igual a: \n')
# print(solve(A, b))
# print('\n')  # Nueva línea

# A = np.array([[1, 2], [2, 1]])
# B = np.array([[1, 2], [7, 19]])
# b = np.array([[5], [3]])
# x = solve(A, b)

# print(f'La matriz A:')
# print(A)
# print(f'El vector b:')
# print(b)
# print(f'El vector de incognitas:')
# print(x)

# print('Matriz A + B')
# print(A+B)

# # Matriz Inversa
# print('La inversa de la matriz A: \n')
# print(np.linalg.inv(A));
# print('\n')  # Nueva línea

# print('La inversa de la matriz B: \n')
# print(np.linalg.inv(B));
# print('\n')  # Nueva línea




# lista = [2, 3, 4]
# print(lista)
# print(type(lista))
# arreglo = np.array(lista)
# print(arreglo)
# print(type(arreglo))

# Matriz rectangular
# A = np.array([[1, 2, -3], [4, 0, -2]]) 
# # print('Matriz A: ')
# # print(A)
# # print(A[1, 1])
# B = np.array([[3, 1], [2, 4], [-1, 5]])
# print('Matriz B: ')
# print(B)
# print('\n C es igual a ')
# print(A@B)
# print('\n D es igual a ')
# print(B@A)
# # texto = 'Hola mundo'
# # numero = 7
# # print(texto + numero)

# lista = range(1,1000+1)
# arreglo = np.array(lista)

# print(arreglo)


# lista = [2, 3, 4]
# try:
#   print(lista[2])
# except:
#   print("No existe esa posición")
# else:
#   print("Está perfecto")

# lista = [2, 3, 4, 5]
# try:
#   print(lista[4])
# except:
#   print("No existe esa posición")
# else:
#   print("Está perfecto")
# finally:
#   print("Hemos terminado el bloque try-except")

# lista = [i for i in range(1, 1000+1) if i % 2 == 0]
# lista = [i for i in range(1, 1000+1) if i % 2 != 0] 
# for i in range(1, 1000+1):
#   lista.append(i)

# lista = []

# for i in range(2, 1000+1):
#   primos = True
#   for j in range(2, 1000+1):
#     if i == j:
#       break
#     elif i % j == 0:
#       primos = False
#     else: 
#       continue
#   if primos == True:
#     lista.append(i)   
    
# print(lista)    
# print(len(lista))
    
# print(lista)
  
# try: 
#   print(texto + numero)
# except:
#   print('No se puede sumar un numero con un string') 

# lista = [2, 3, 4]
# print(lista[5])
 
  
  
# concatenacion = texto + numero
# print(concatenacion)




# mensaje = """
# # Tanto los patrones como las cadenas de texto a buscar pueden ser cadenas de Unicode (str) así como cadenas de 8 bits (bytes). 

# # Sin embargo, las cadenas Unicode y las cadenas de 8 bits no se pueden mezclar: es decir, no se puede hacer coincidir una cadena Unicode con un patrón de bytes o viceversa; del mismo modo, al pedir una sustitución, la cadena de sustitución debe ser del mismo tipo que el patrón y la cadena de búsqueda."""

# palabras = re.split(' ', mensaje)

# for palabra in palabras:
#   print(palabra)

# for caracter in mensaje:
  
#     print(caracter) 

# # print(re.findall('un', mensaje)) # Devolverá ['de', 'de']

# print(mensaje)
# print('\n')
# print(re.split(' ', mensaje))

# ejemplo = '593-7-2585150'
# arreglo = []

# for letra in ejemplo:
#   if letra != '-':
#     print(letra)


# print(re.split('-', ejemplo))
# pattern = '4+'
# print(re.findall(pattern, ejemplo)) # Devolverá ['333']
# print(re.match('1', ejemplo) )