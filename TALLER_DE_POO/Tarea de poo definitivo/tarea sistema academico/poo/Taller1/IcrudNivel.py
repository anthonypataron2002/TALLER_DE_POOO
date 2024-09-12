from Utilidades import reset_color,orange_color,gold_color,lime_green_color,pink_color,teal_color,magenta_color
from Utilidades import gotoxy,borrarPantalla
from Componenetes import Menu
from nivel import Nivel
from clsJson import JsonFile
from Icrud import ICrud
import time
import os

path, file = os.path.split(__file__)

class CrudNivel(ICrud):
    json_file = JsonFile(f"{path}/data/Nivel.json")

    def create(self):
        borrarPantalla()
        print("Registro de Nivel")
        try:
            niveles = self.json_file.read()
            new_id = max([nivel['id'] for nivel in niveles], default=0) + 1
            nivel_descripcion = input("Ingrese la descripción del Nivel: ")
            active = True

            nivel = Nivel(new_id, nivel_descripcion, active)
            niveles.append(nivel.getJson())
            self.json_file.save(niveles)

            print(f"Nivel '{nivel_descripcion}' registrado exitosamente.")
        except Exception as e:
            print(f"Error al registrar el nivel: {e}")
        time.sleep(3)

    def update(self):
        borrarPantalla()
        print("Actualizar datos de Nivel")
        try:
            niveles = self.json_file.read()
            if niveles:
                while True:
                    nivel_id_str = input("Ingrese el ID del Nivel (número entero): ").strip()
                    
                    if nivel_id_str.isdigit():
                        nivel_id = int(nivel_id_str)
                        break
                    else:
                        print("ID inválido. Debe ser un número entero.")
                
                nivel_encontrado = False
                for nivel in niveles:
                    if nivel['id'] == nivel_id:
                        nivel_encontrado = True
                        print(f"Nivel encontrado: {nivel['nivel']}")
                        nivel['nivel'] = input("Ingrese la nueva descripción del Nivel: ")
                        nivel['active'] = input("Nivel activo (True/False): ").lower() == 'true'
                        self.json_file.save(niveles)
                        print("Datos del nivel actualizados correctamente.")
                        break
                
                if not nivel_encontrado:
                    print("Nivel no encontrado.")
            else:
                print("No hay niveles registrados.")
        except Exception as e:
            print(f"Error al actualizar el nivel: {e}")
        time.sleep(3)

    def delete(self):
        borrarPantalla()
        print("Eliminar Nivel")
        try:
            niveles = self.json_file.read()
            if niveles:
                while True:
                    nivel_id_str = input("Ingrese el ID del Nivel a eliminar (número entero): ").strip()
                    
                    if nivel_id_str.isdigit():
                        nivel_id = int(nivel_id_str)
                        break
                    else:
                        print("ID inválido. Debe ser un número entero.")
                
                nivel_encontrado = False
                for nivel in niveles:
                    if nivel['id'] == nivel_id:
                        nivel_encontrado = True
                        niveles.remove(nivel)
                        self.json_file.save(niveles)
                        print(f"Nivel con ID {nivel_id} eliminado correctamente.")
                        break
                
                if not nivel_encontrado:
                    print("Nivel no encontrado.")
            else:
                print("No hay niveles registrados.")
        except Exception as e:
            print(f"Error al eliminar el nivel: {e}")
        time.sleep(3)


    def consult(self):
        borrarPantalla()
        print("Consulta de Niveles")
        try:
            niveles = self.json_file.read()
            if niveles:
                print("Lista de Niveles registrados:")
                for nivel in niveles:
                    print(f"ID: {nivel['id']} | Descripción: {nivel['nivel']} | Activo: {nivel['active']} | Fecha de Creación: {nivel['fecha_creacion']}")
            else:
                print("No hay niveles registrados.")
        except Exception as e:
            print(f"Error al consultar los niveles: {e}")
        time.sleep(3)
