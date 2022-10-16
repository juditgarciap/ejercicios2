#ejercicio1 tema2 (parte 1)

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def __str__ (self): 
        return "({},{})".format (self.x,self.y)
#Esta funcion nos permite saber en que cuadrante está el punto
    def obtenerCuadrante(self):
        if self.x == 0 and self.y == 0:
            cuadrante = 'El punto ({},{}) no esta en nigún cuadrante, esta en el origen'.format(self.x, self.y)
        elif self.x >= 0 and self.y >= 0:
            cuadrante = 'El punto ({},{}) esta en el cuadrante 1'.format(self.x, self.y)
        elif self.x<0 and self.y>= 0:
            cuadrante = 'El punto ({},{}) esta en el cuadrante 2'.format(self.x, self.y)
        elif self.x<=0 and self.y<=0:
            cuadrante = 'El punto ({},{}) esta en el cuadrante 3'.format(self.x, self.y)
        elif self.x>=0 and self.y<=0:
            cuadrante = 'El punto ({},{}) esta en el cuadrante 4'.format(self.x, self.y)

        return cuadrante

punto_1 = Punto(4, -7)
punto_origen = Punto()
punto_2 = Punto(2,2)

print(punto_1)
print(punto_origen)

print(punto_origen.x)
print(punto_1.y)

punto_origen.obtenerCuadrante()

punto_1.obtenerCuadrante()



#esta función calcula el vector resultante  
def vector (self, punto):
    x= punto.x - self.x 
    y= punto.y - self.y


    return x,y 

punto_1.vector(punto_origen)

punto_1.vector(punto_2)


#optativo, toma otro punto y calcula la distancia entre los dos puntos 
import math
def distancia(self, punto):
    distancia = math.sqrt ((punto.x - self.x)**2 + (punto.y - self.y)**2)

    return distancia 

punto_1.distancia(punto_origen)




#ejercicio1 tema2 (parte 2)
#crear una clase rectangulo   y metodo constructor puntos 
class Rectangulo:
    def __init__(self, punto_1=Punto(), punto_2=Punto()):
        self.punto_1 = punto_1
        self.punto_2 = punto_2
#metodo llamado base que muestra la base
    def ObtenerBase(self):
        self.base = abs(self.punto_2.x - self.punto_1.x)

        return self.base
#metodo llamado altura que muestra la altura
    def ObtenerAltura(self):
        self.altura = abs(self.punto_2.y - self.punto_1.y)

        return self.altura
#metodo llamado area que muestra el area
    def ObtenerArea(self):
        area = self.base * self.altura

        return area

A = Punto(2,3) 
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)

# Consulta a que cuadrante pertenece los puntos A, C, D

# Consulta los vectores AB y BA

# Consulta la distancia entre los puntos A y B - B y A


# Determina cual de los 3 puntos se encuentra mas lejos del origen (0,0)

# Crear un rectangulo usando los puntos A y B
rectangulo = Rectangulo(A,B)

# consultar la base
rectangulo.ObtenerBase()

# consultar la altura
rectangulo.ObtenerAltura()

# consultar el area del rectangulo
rectangulo.ObtenerArea()


