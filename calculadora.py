def calculadora(num1, num2, operacion):  
  """
  Funcion que realiza operaciones de suma, resta, multiplicacion y division a dos numeros de entrada
  Argumentos:
  num1, num2 -- son los numeros con los cuales vamos a realizar las operaciones
  operacion  -- define el tipo de operacion que va a ejecutar la funcion calculadora (suma, resta, multiplicacion, division) 
  """
  if (operacion == 'sumar'):
    return num1 + num2
  elif (operacion == 'restar'):
    return num1 - num2
  elif (operacion == 'multiplicar'):
    return num1 * num2
  elif (operacion == 'dividir'):
    if (num2 == 0):
      print('No se puede dividir para cero')
    else:  
      return num1 / num2
  else:
    print(f'La operacion {operacion} no esta disponible en la calculadora')
    
def potencia(base, exponente):
  """
  Función que calcula la potencia de dos números.
  Argumentos:
  base ‐‐ base de la operación.
  exponente ‐‐ exponente de la operación.
  """
  return base ** exponente  

def dividir(num1, num2):
  return num1/num2