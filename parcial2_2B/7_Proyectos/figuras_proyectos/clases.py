import math

class Figuras:
    def __init__(self, x,y,visible):
        self.y=y
        self.x=x
        self.visible=visible
    visible=bool
    def getX(self):
        return self.x
    def getX(self,x):
        self.x=x
    def getY(self):
        return self.y
    def getY(self,y):
        self.y=y
    def getVisible(self):
        return self.visible
    def getVisile(self,visible):
        self.visible=visible



class rectangulos(Figuras):
    def __init__(self,x,y,visible,alto,ancho):
        super().__init__(x,y,visible)
        self.alto=alto
        self.ancho=ancho

    def getAlto(self):
        return self.alto
    def getAlto(self,alto):
        self.alto=alto
    def getAncho(self):
        return self.ancho
    def getAlto(self,ancho):
        self.ancho=ancho
    def AreaR(self):
        return self.alto * self.ancho
    def getInfo(self):
        print(f"El rectángulo tiene una altura de {self.alto} y un ancho de {self.ancho} y visivilidad es{self.visible} su altura es {self.alto} y su ancho es {self.ancho}")

class Circulo(Figuras):
    def __init__(self,x,y,visible,radio):
        super().__init__(x,y,visible)
        self.radio=radio

        
    radio=int
    area=float
    area=radio*3.1416
    def getRadio(self):
        return self.radio
    def getAlto(self,radio):
        self.radio=radio
    def area_circulo(radio):
        return math.pi * (radio ** 2)

    def getInfo(self):
        print(f"la medida de x es {self.getX} la de y es {self.getY} y su visivilidad es {self.getVisible}El radio es {self.radio}")