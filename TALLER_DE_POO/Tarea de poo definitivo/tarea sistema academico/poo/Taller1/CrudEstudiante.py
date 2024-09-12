from Utilidades import reset_color, orange_color, gold_color, lime_green_color, pink_color, teal_color, magenta_color
from Utilidades import gotoxy, borrarPantalla
from Componenetes import Menu
from Estudiante import Estudiante
from clsJson import JsonFile
from Icrud import ICrud
import time
import os

path, file = os.path.split(__file__)

class CrudEstudiante(ICrud):
    json_file = JsonFile(f"{path}/data/Estudiante.json")
    
    def create(self):
        borrarPantalla()
        print("Registro de Estudiante")
        
        # Validar que el nombre no esté vacío
        while True:
            name = input("Ingrese el nombre del estudiante: ").strip()
            if name:
                break
            print("El nombre no puede estar vacío.")
        
        # Validar que el apellido no esté vacío
        while True:
            lastname = input("Ingrese el apellido del estudiante: ").strip()
            if lastname:
                break
            print("El apellido no puede estar vacío.")
        
        estudiante = Estudiante(name, lastname)
        estudiantes = self.json_file.read()
        estudiantes.append(estudiante.getJson())
        self.json_file.save(estudiantes)
        time.sleep(3)
        print("Estudiante registrado exitosamente")
        
    def update(self):
        borrarPantalla()
        print("Actualizar datos de Estudiante")
        estudiantes = self.json_file.read()
        
        if estudiantes:
            # Validar que el ID sea un número entero
            while True:
                try:
                    estudiante_id = int(input("Ingrese el ID del Estudiante a actualizar: ").strip())
                    break
                except ValueError:
                    print("ID inválido. Debe ser un número entero.")
            
            for estudiante in estudiantes:
                if estudiante['id'] == estudiante_id:
                    print(f"Estudiante encontrado: {estudiante['nombre']} {estudiante['apellido']}")
                    # Validar entrada vacía y mantener el valor anterior
                    estudiante['nombre'] = input(f"Ingrese el nuevo nombre (actual: {estudiante['nombre']}): ").strip() or estudiante['nombre']
                    estudiante['apellido'] = input(f"Ingrese el nuevo apellido (actual: {estudiante['apellido']}): ").strip() or estudiante['apellido']
                    self.json_file.save(estudiantes)
                    print("Datos actualizados correctamente.")
                    break
            else:
                print("Estudiante no encontrado.")
        else:
            print("No hay estudiantes registrados.")
        time.sleep(3)

    def delete(self):
        borrarPantalla()
        print("Eliminar Estudiante")
        estudiantes = self.json_file.read()
        
        if estudiantes:
            # Validar que el ID sea un número entero
            while True:
                try:
                    estudiante_id = int(input("Ingrese el ID del estudiante a eliminar: ").strip())
                    break
                except ValueError:
                    print("ID inválido. Debe ser un número entero.")
                    time.sleep(3)
                    return
            
            for estudiante in estudiantes:
                if estudiante['id'] == estudiante_id:
                    estudiantes.remove(estudiante)
                    self.json_file.save(estudiantes)
                    print("Estudiante eliminado correctamente.")
                    break
            else:
                print("Estudiante no encontrado.")
        else:
            print("No hay estudiantes registrados.")
        time.sleep(3)

    def consult(self):
        borrarPantalla()
        print("Consulta de Estudiantes")
        estudiantes = self.json_file.read()
        
        if estudiantes:
            print("Lista de estudiantes registrados:")
            for estudiante in estudiantes:
                print(f"ID: {estudiante['id']} | Nombre: {estudiante['nombre']} {estudiante['apellido']}")
        else:
            print("No hay estudiantes registrados.")
        time.sleep(3)
