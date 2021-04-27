#Ejercicio 1

#Código copiado:
class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2

#Respuesta:
#La interfaz es energía, comer, acariciar y estaDebil y su estado es alimento y caricias.

#Ejercicio 2
def volar(self, kms):
    if self.energia-(10 + kms)>=0:
        self.energia -= 10 + kms

#Ejercicio 3
class Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca=marca
        self.modelo=modelo
        self.precio=precio

    def desceunto(self, descuento):
        self.precio-=(descuento/100)*precio
        print("El precio final (con el descuento aplicado) es "+int(self.precio))

#Ejercicio 4
class contador:
    def __init__(self, valor_inicial):
        self.valor=valor_inicial
    
    def inc(self):
        self.valor+=1
    
    def dis(self):
        self.valor-=1
    
    def reset(self):
        self.valor=0
    
    def valorActual(self):
        self.valor
    
    def valorNuevo(self, valor_nuevo):
        self.valor=valor_nuevo

#Ejercicio 5
class contador:
    def __init__(self, valor_inicial):
        self.valor=valor_inicial
    
    def inc(self):
        self.valor+=1
    
    def dis(self):
        self.valor-=1
    
    def reset(self):
        self.valor=0
    
    def valorActual(self):
        self.valor
    
    def valorNuevo(self, valor_nuevo):
        self.valor=valor_nuevo
    
    def ultimoComando(self):
        ???

#Ejercicio 6
class calculadora:
    def __init__(self):
        self.resultado=0
    
    def cargar(self, numero):
        self.resultado=numero
    
    def sumar(self, numero):
        self.resultado+=numero
    
    def restar(self, numero):
        self.resultado-=numero
    
    def multiplicar(self, numero):
        self.resulado=self.resultado*numero
    
    def valorActual(self):
        self.resultado

#Ejercicio 7