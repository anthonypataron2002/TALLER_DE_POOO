from datetime import datetime
class Profesor:
    next_id = 0
    def __init__(self, nombre, apellido, active=True):
        Profesor.next_id += 1
        self.__id = Profesor.next_id
        self.nombre = nombre
        self.apellido = apellido
        self.active = active
        self.fecha_creacion = datetime.now().strftime('%d-%m-%Y')
    def __str__(self):
        return f'id: {self.__id}, nombre: {self.nombre}, apellido: {self.apellido}, active: {self.active}, fecha_creacion: {self.fecha_creacion}'
    
    def full_name(self):
        return f'{self.nombre} {self.apellido}'
    
    def getJson(self):
        return {
            'id': self.__id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'active': self.active,
            'fecha_creacion': self.fecha_creacion
        }