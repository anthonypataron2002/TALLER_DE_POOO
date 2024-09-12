from datetime import date

class Nivel:
    def __init__(self, id, nivel, active=True):
        self.id = id  
        self.nivel = nivel  
        self.fecha_creacion = date.today()
        self.active = active

    def __str__(self):
        return (f'id: {self.id}, nivel: {self.nivel}, active: {self.active}, fecha_creacion: {self.fecha_creacion}')

    def getJson(self):
        return {
            'id': self.id,
            'nivel': self.nivel,
            'fecha_creacion': self.fecha_creacion.strftime('%Y-%m-%d'),
            'active': self.active
        }
        
if __name__ == '__main__':
    Nivel1 = Nivel(1, 'Primero', True)
    print(Nivel1)
