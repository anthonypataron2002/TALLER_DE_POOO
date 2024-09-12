from datetime import datetime

class Estudiante:
    next_id = 0
    def __init__(self, nombre, apellido, active=True):
        Estudiante.next_id += 1
        self.__id = Estudiante.next_id
        self.nombre = nombre
        self.apellido = apellido
        self.active = active
        self.fecha_creacion = datetime.now().strftime('%d-%m-%Y')
    
    @property
    def id(self):
        return self.__id
    
    def __str__(self):
        return f'id: {self.__id}, nombre: {self.nombre}, apellido: {self.apellido}, active: {self.active}, fecha_creacion: {self.fecha_creacion}'
    
    def getJson(self):
        return {
            'id': self.__id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'active': self.active,
            'fecha_creacion': self.fecha_creacion
        }
    

if __name__ == '__main__':
    estudiante1 = Estudiante('Steven', 'Garcia')
    estudiante2 = Estudiante('Deimy', 'Barona')
    print(estudiante1)
    print(estudiante2)