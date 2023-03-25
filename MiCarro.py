class MiCarro:
  def __init__(self, marca, color):
    # Atributos de la clase carro
    self.marca = marca
    self.color = color

  # Metodos 
  def caracteristicas(self):
    print(f'Carro marca {self.marca}, color {self.color}')
  def conducir(self):
    print('se conduce')
    
  def pitar(self):
    print('honk honk')  
    
  def frenar(self):  
    print('Frena')
    
  def acelerar(self):  
    print('Acelerar')  