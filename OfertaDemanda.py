#Pd= DAPmax - d*Qd
#Pd: precio pagado por el consumidor
#DAPmax: maxima dispocision a pagar del consumidor
#d: pendiente de la demanda
#Qd: cantidad que el consumidor quiere comprar para su determinado precio

#Ps = COmin + s*Qs
#Ps: precio percibido por el productor
#Comin: costo de oportunidad minimo (interseccion con eje y) 
#s: pemdiente oferta
#Qs: cantidad que el productor quiere proveer
class mercado:

    def __init__(self, DAPmax, COmin, d, s):
        self.DAPmax, self.COmin, self.d, self.s = DAPmax, COmin, d, s
        
        if DAPmax < COmin:
            raise ValueError('Demanda insuficiente.')

    def cantidad_equilibrio(self):
        "Cálculo cantidad de equilibrio"
        return  (self.DAPmax - self.COmin)/(self.d + self.s)

    def precio_equilibrio(self):
        "Cálculo cantidad de equilibrio"
        return  self.DAPmax - self.d * self.cantidad_equilibrio()

    def excedente_consumidor(self):
        "Cálculo excedente consumidor"
        return (self.DAPmax - self.precio_equilibrio())*self.cantidad_equilibrio()/2

    def excedente_productor(self):
        "Cálculo excedente productor"
        return (self.precio_equilibrio() - self.COmin) * self.cantidad_equilibrio() /2

    def excedente_total(self):
        "Cálculo excedente total"
        return self.excedente_productor() + self.excedente_consumidor()
    
    def demanda(self,x):
        "Función demanda"
        return self.DAPmax - self.d*x
        
    def oferta(self,x):
        "Función oferta"
        return self.COmin + self.s*x
