from datetime import date
class Periodo:
    def __init__(self, id, descripcion, fecha_inicio, fecha_fin, active=True):
        self.id = id
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.active = active

    def __str__(self):
        return (f'id: {self.id}, descripcion: {self.descripcion}, fecha_inicio: {self.fecha_inicio}, '
                f'fecha_fin: {self.fecha_fin}, active: {self.active}')
    
    def getJson(self):
        return {
            'id': self.id,
            'descripcion': self.descripcion,
            'fecha_inicio': self.fecha_inicio.strftime('%Y-%m-%d'),
            'fecha_fin': self.fecha_fin.strftime('%Y-%m-%d'),
            'active': self.active
        }

if __name__ == '__main__':
    periodo = Periodo(1, 'Primer Periodo', date(2021, 1, 1), date(2021, 3, 31), True)
    print(periodo)