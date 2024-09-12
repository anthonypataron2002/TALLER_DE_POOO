from datetime import date

class Asignatura:
    def __init__(self, id, descripcion, nivel, active):
        self.id = id  
        self.descripcion = descripcion  
        self.nivel = nivel  
        self.fecha_creacion = date.today()  
        self.active = active  
    
    def __str__(self):
        return (f'id: {self.id}, descripcion: {self.descripcion}, nivel: {self.nivel},active: {self.active}, fecha_creacion: {self.fecha_creacion}')
    
    def getJson(self):
        return {
            'id': self.id,
            'descripcion': self.descripcion,
            'nivel': self.nivel,
            'active': self.active,
            'fecha_creacion': self.fecha_creacion.strftime('%Y-%m-%d')
        }
        
if __name__ == '__main__':
    asignatura = Asignatura(1, 'Matemáticas', 'Primero', True)
    print(asignatura)