#Ejercicio 2
def esta_en_equilibrio(self):
    return self.energia < 300 and self.energia > 150

#Ejercicio 3
class Ornitologo:
  def __init__(self):
    self.aves_en_estudio=[]

  def estudiarAve(self, ave):
    self.aves_en_estudio.append(ave)
  
  def avesEnEstudio(self):
    self.aves_en_estudio
  
  def realizarRutinaSobreAves(self):
    for ave in self.aves_en_estudio:
      ave.alimentacion(80)
      ave.volar(70)
      ave.alimentacion(10)

  def avesEnEquilibrio(self):
    for ave in self.aves_en_estudio:
      if ave.esta_en_equilibrio():
        return ave

class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia = self.energia + 4 * gramos

  def volar(self, kms):
    self.energia -= 10 + kms

  def esta_en_equilibrio(self):
    return self.energia < 300 and self.energia > 150

  def alimentacion(self, gramos):
    self.comer_alpiste(gramos)

class Gorrion:
  def __init__(self, energia):
    self.energia = energia
  
  def comer_avena(self, gramos):
    self.energia = self.energia + 0.5 * gramos

  def volar(self, kms):
    self.energia -= 2 * kms

  def esta_en_equilibrio(self):
    return self.energia < 300 and self.energia > 150

  def alimentacion(self, gramos):
    self.comer_avena(gramos)

perry=Ornitologo()
phineas=Golondrina(500)
ferb=Golondrina(150)
isabella=Gorrion(300)
candance=Gorrion(750)

#Ejercicio 4
class MedioDeTransporte:
  def cargar_combustible(self, litros):
    self.combustible+=litros
  
  def entran(self, personas):
    if self.lugares_libres>=personas:
      self.lugares_libres-=personas

  def cargar_combustible(self, litros):
    self.combustible+=litros

class Moto(MedioDeTransporte):
  def __init__(self, combustible):
    self.combustible=combustible
    self.lugares_libres=2

  def recorrer(self, kilometros):
    self.combustible-=0.5*kilometros

class Auto(MedioDeTransporte):
  def __init__(self,combustible):
    self.combustible=combustible
    self.lugares_libres=5

  def recorrer(self, kilometros):
    self.combustible-=kilometros

rayo=Auto(100)
mate=Auto(35)
guido=Moto(57)