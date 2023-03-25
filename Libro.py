class Libro:
  def __init__(self, titulo, autor, isbn, editorial, paginas, edicion):
    self.titulo = titulo
    self.autor = autor
    self.isbn = isbn
    self.editorial = editorial
    self.paginas = paginas
    self.edicion = edicion
    
  def detalle(self):
    print(f'Libro: {self.titulo} \n Autor: {self.autor} \n ISBN: {self.isbn} \n Editorial: {self.editorial} \n # de paginas: {self.paginas} \n')  