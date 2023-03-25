# from calculadora import potencia

# ### Funciones
# def mi_funcion():
#   print('Buenos dias')

# copiar una  funcion en una variable78

# nuevafuncion = mi_funcion

# llamada a funciones
# # mi_funcion()
# # nuevafuncion()
    
# print('Bienvenido a la funcion calculadora')    
# numero_1 = int(input('Ingrese el primer numero: '))
# numero_2 = int(input('Ingrese el segundo numero: '))   
# operacion = input('Que operacion desea realizar (sumar, restar, multiplicar o dividir): ')

# print(potencia(2, 8))   

# import math

# print(math.fabs(-1234))
# print(math.gcd(34, 82))


# print(math.ceil(198.19))
# print(6%2)

# arreglo = [1, 2, 3, 4, 5, 6, 7, 8]
# print(min(arreglo))

# print(math.log10(0.0007))

## Datetime
# # 25/03/2023
# # 25-MAR-23
# from calculadora import *
# import datetime
# fecha = datetime.datetime.now()
# # print(fecha)
# # # # 25-03-2023

# print('Bienvenido a la funcion calculadora')    
# print(f'Fecha: {fecha.strftime("%d")}-{fecha.strftime("%m")}-{fecha.strftime("%Y")}')
# numero_1 = int(input('Ingrese el primer numero: '))
# numero_2 = int(input('Ingrese el segundo numero: '))   
# operacion = input('Que operacion desea realizar (sumar, restar, multiplicar o dividir): ')
# resultado = calculadora(numero_1, numero_2, operacion)   
# print(f'El resultado de {operacion} {numero_1} con {numero_2} es: ', resultado)

### Funciones lambda

# def dividir(num1,num2):
#   return num1/num2

# from calculadora import dividir
  
# resultado = lambda num1, num2: num1/num2
# print(resultado(7,9))

# edades = [5, 12, 17, 18, 24, 32]
# adultos = filter(lambda x: x>=18, edades)
# menores = filter(lambda x: x<18, edades)

# for x in menores:
#   print(x)

### Clases -- Programacion Orientada a Objeto
# class MiCarro:
#   def __init__(self, marca, color):
#     # Atributos de la clase carro
#     self.marca = marca
#     self.color = color

#   # Metodos 
#   def caracteristicas(self):
#     print(f'Carro marca {self.marca}, color {self.color}')
#   def conducir(self):
#     print('se conduce')
    
#   def pitar(self):
#     print('honk honk')  

# from MiCarro import *

# carro_toyota = MiCarro('toyota', 'rojo')  # Se esta creando el objeto carro
# carro_toyota.caracteristicas()
# carro_toyota.pitar()

# carro_volkswagen = MiCarro('volkswagen', 'gris') # Se esta creando otro objeto carro
# carro_volkswagen.caracteristicas()
# carro_volkswagen.acelerar()

# carro_peugeot = MiCarro('peugeot', 'azul') # Se esta creando otro objeto carro
# carro_peugeot.caracteristicas()

# carro_chevrolet = MiCarro('chevrolet', 'blanco') # Se esta creando otro objeto carro
# carro_chevrolet.caracteristicas()
# carro_chevrolet.frenar()

# from Libro import *

# libro_quijote = Libro('Don Quijote de la Mancha', 'Miguel de Cervantes', '0987-7489', 'Mi Editorial', 934, 34 )
# libro_quijote.detalle()

# libro_mimo = Libro('Fundamentals of massive MIMO', 'Thomas L. Marzetta', '978-1-107-17557-0', 'Cambridge',230, 1)
# libro_mimo.detalle()

class Animal:
  def __init__(self,nombre):
    self.nombre = nombre
  
  def respirar(self):  
    print('El animal está vivo')

class Ave(Animal):
  def volar(self):
    print('Vuela');    

class Pez(Animal): 
  def nadar(self):
    print('Nada')

pez1 = Pez('trucha')
pez1.respirar()
pez1.nadar()    

ave1 = Ave('Halcon')
ave1.respirar()
ave1.volar()  
    
      

