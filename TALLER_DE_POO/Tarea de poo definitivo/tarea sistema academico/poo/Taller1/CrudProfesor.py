from Utilidades import reset_color, orange_color, gold_color, lime_green_color, pink_color, teal_color, magenta_color
from Utilidades import gotoxy, borrarPantalla
from Componenetes import Menu
from Profesor import Profesor
from clsJson import JsonFile
from Icrud import ICrud
import time
import os

path, file = os.path.split(__file__)

class CrudProfesor(ICrud):
    json_file = JsonFile(f"{path}/data/Profesor.json")

    def create(self):
        borrarPantalla()
        print("Registro de Profesor")
        try:
            while True:
                nombre = input("Ingrese el nombre del Profesor: ").strip()
                if nombre:
                    break
                print("El nombre no puede estar vacío.")
            
            while True:
                apellido = input("Ingrese el apellido del Profesor: ").strip()
                if apellido:
                    break
                print("El apellido no puede estar vacío.")
            
            profesor = Profesor(nombre, apellido)
            profesores = self.json_file.read()
            profesores.append(profesor.getJson())
            self.json_file.save(profesores)
            print("Profesor registrado exitosamente")
        except Exception as e:
            print(f"Error al registrar el profesor: {e}")
        time.sleep(3)

    def update(self):
        borrarPantalla()
        print("Actualizar datos de Profesor")
        try:
            profesores = self.json_file.read()
            if profesores:
                while True:
                    try:
                        profesor_id = int(input("Ingrese el ID del Profesor a actualizar: ").strip())
                        break
                    except ValueError:
                        print("ID inválido. Debe ser un número entero.")
                
                for profesor in profesores:
                    if profesor['id'] == profesor_id:
                        print(f"Profesor encontrado: {profesor['nombre']} {profesor['apellido']}")
                        
                        while True:
                            nuevo_nombre = input("Ingrese el nuevo nombre: ").strip()
                            if nuevo_nombre:
                                profesor['nombre'] = nuevo_nombre
                                break
                            print("El nombre no puede estar vacío.")
                        
                        while True:
                            nuevo_apellido = input("Ingrese el nuevo apellido: ").strip()
                            if nuevo_apellido:
                                profesor['apellido'] = nuevo_apellido
                                break
                            print("El apellido no puede estar vacío.")
                        
                        self.json_file.save(profesores)
                        print("Datos actualizados correctamente.")
                        break
                else:
                    print("Profesor no encontrado.")
            else:
                print("No hay profesores registrados.")
        except Exception as e:
            print(f"Error al actualizar el profesor: {e}")
        time.sleep(3)

    def delete(self):
        borrarPantalla()
        print("Eliminar Profesor")
        try:
            profesores = self.json_file.read()
            if profesores:
                while True:
                    try:
                        profesor_id = int(input("Ingrese el ID del Profesor a eliminar: ").strip())
                        break
                    except ValueError:
                        print("ID inválido. Debe ser un número entero.")
                
                for profesor in profesores:
                    if profesor['id'] == profesor_id:
                        profesores.remove(profesor)
                        self.json_file.save(profesores)
                        print("Profesor eliminado correctamente.")
                        break
                else:
                    print("Profesor no encontrado.")
            else:
                print("No hay profesores registrados.")
        except Exception as e:
            print(f"Error al eliminar el profesor: {e}")
        time.sleep(3)

    def consult(self):
        borrarPantalla()
        print("Consulta de Profesores")
        try:
            profesores = self.json_file.read()
            if profesores:
                print("Lista de Profesores registrados:")
                for profesor in profesores:
                    print(f"ID: {profesor['id']} | Nombre: {profesor['nombre']} {profesor['apellido']}")
            else:
                print("No hay profesores registrados.")
        except Exception as e:
            print(f"Error al consultar los profesores: {e}")
        time.sleep(3)
