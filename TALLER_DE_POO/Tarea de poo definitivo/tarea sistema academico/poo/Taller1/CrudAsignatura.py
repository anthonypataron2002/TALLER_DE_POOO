from Utilidades import reset_color, orange_color, gold_color, lime_green_color, pink_color, teal_color, magenta_color
from Utilidades import gotoxy, borrarPantalla
from Componenetes import Menu
from Asignatura import Asignatura
from clsJson import JsonFile
from Icrud import ICrud
import time
import os

path, file = os.path.split(__file__)

class CrudAsignatura(ICrud):
    json_file = JsonFile(f"{path}/data/Asignatura.json")

    def create(self):
        borrarPantalla()
        print("Registro de Asignatura")
        try:
            # Asignar ID automáticamente basado en los registros existentes
            asignaturas = self.json_file.read()
            new_id = max([asig['id'] for asig in asignaturas], default=0) + 1

            # Validar que la descripción no esté vacía
            while True:
                descripcion = input("Ingrese la descripción de la Asignatura: ").strip()
                if descripcion:
                    break
                print("La descripción no puede estar vacía.")
            
            # Validar que el nivel no esté vacío
            while True:
                nivel = input("Ingrese el nivel de la Asignatura: ").strip()
                if nivel:
                    break
                print("El nivel no puede estar vacío.")
            
            active = True  # Se define como activo al crear la asignatura

            # Crear objeto Asignatura
            asignatura = Asignatura(new_id, descripcion, nivel, active)
            asignaturas.append(asignatura.getJson())
            self.json_file.save(asignaturas)

            print(f"Asignatura '{descripcion}' registrada exitosamente.")
        except Exception as e:
            print(f"Error al registrar la asignatura: {e}")
        time.sleep(3)

    def update(self):
        borrarPantalla()
        print("Actualizar datos de Asignatura")
        try:
            asignaturas = self.json_file.read()
            if asignaturas:
                # Validar que el ID sea un número entero
                while True:
                    try:
                        asignatura_id = int(input("Ingrese el ID de la asignatura: ").strip())
                        break
                    except ValueError:
                        print("ID inválido. Debe ser un número entero.")
                
                for asignatura in asignaturas:
                    if asignatura['id'] == asignatura_id:
                        print(f"Asignatura encontrada: {asignatura['descripcion']} (Nivel: {asignatura['nivel']})")

                        # Validar que la descripción no esté vacía
                        asignatura['descripcion'] = input(f"Ingrese la nueva descripción (actual: {asignatura['descripcion']}): ").strip() or asignatura['descripcion']

                        # Validar que el nivel no esté vacío
                        asignatura['nivel'] = input(f"Ingrese el nuevo nivel (actual: {asignatura['nivel']}): ").strip() or asignatura['nivel']

                        # Validar entrada de activo (True/False)
                        while True:
                            active_str = input("Asignatura activa (True/False): ").strip().lower()
                            if active_str in ['true', 'false']:
                                asignatura['active'] = active_str == 'true'
                                break
                            print("Debe ingresar 'True' o 'False'.")

                        self.json_file.save(asignaturas)
                        print("Datos actualizados correctamente.")
                        break
                else:
                    print("Asignatura no encontrada.")
            else:
                print("No hay asignaturas registradas.")
        except Exception as e:
            print(f"Error al actualizar la asignatura: {e}")
        time.sleep(3)

    def delete(self):
        borrarPantalla()
        print("Eliminar Asignatura")
        try:
            asignaturas = self.json_file.read()
            if asignaturas:
                # Validar que el ID sea un número entero
                while True:
                    try:
                        asignatura_id = int(input("Ingrese el ID de la Asignatura a eliminar: ").strip())
                        break
                    except ValueError:
                        print("ID inválido. Debe ser un número entero.")
                
                for asignatura in asignaturas:
                    if asignatura['id'] == asignatura_id:
                        asignaturas.remove(asignatura)
                        self.json_file.save(asignaturas)
                        print(f"Asignatura con ID {asignatura_id} eliminada correctamente.")
                        break
                else:
                    print("Asignatura no encontrada.")
            else:
                print("No hay asignaturas registradas.")
        except Exception as e:
            print(f"Error al eliminar la asignatura: {e}")
        time.sleep(3)

    def consult(self):
        borrarPantalla()
        print("Consulta de Asignaturas")
        try:
            asignaturas = self.json_file.read()
            if asignaturas:
                print("Lista de Asignaturas registradas:")
                for asignatura in asignaturas:
                    print(f"ID: {asignatura['id']} | Descripción: {asignatura['descripcion']} | Nivel: {asignatura['nivel']} | Activa: {asignatura['active']}")
            else:
                print("No hay asignaturas registradas.")
        except Exception as e:
            print(f"Error al consultar las asignaturas: {e}")
        time.sleep(3)
