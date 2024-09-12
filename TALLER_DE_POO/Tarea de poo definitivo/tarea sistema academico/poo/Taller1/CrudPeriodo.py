from Utilidades import reset_color, orange_color, gold_color, lime_green_color, pink_color, teal_color, magenta_color
from Utilidades import gotoxy, borrarPantalla
from Componenetes import Menu
from Periodo import Periodo
from clsJson import JsonFile
from Icrud import ICrud
import time
from datetime import datetime
import os

path, file = os.path.split(__file__)

class CrudPeriodo(ICrud):
    json_file = JsonFile(f"{path}/data/Periodo.json")

    def create(self):
        borrarPantalla()
        print("Registro de un nuevo Periodo")
        try:
            periodos = self.json_file.read()
            new_id = max([periodo["id"] for periodo in periodos], default=0) + 1

            # Validar que la descripción no esté vacía
            while True:
                descripcion = input("Ingrese la Descripción del periodo: ").strip()
                if descripcion:
                    break
                print("La descripción no puede estar vacía.")
            
            # Validar formato y lógica de fechas
            while True:
                fecha_inicio_str = input("Ingrese la fecha de inicio (YYYY-MM-DD): ").strip()
                try:
                    fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d').date()
                    break
                except ValueError:
                    print("Fecha de inicio inválida. Debe estar en formato YYYY-MM-DD.")

            while True:
                fecha_fin_str = input("Ingrese la fecha de fin (YYYY-MM-DD): ").strip()
                try:
                    fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%d').date()
                    if fecha_fin >= fecha_inicio:
                        break
                    else:
                        print("La fecha de fin debe ser igual o posterior a la fecha de inicio.")
                except ValueError:
                    print("Fecha de fin inválida. Debe estar en formato YYYY-MM-DD.")

            active = True

            periodo = Periodo(new_id, descripcion, fecha_inicio, fecha_fin, active)
            periodos.append(periodo.getJson())
            self.json_file.save(periodos)

            print(f"Período '{descripcion}' registrado exitosamente.")
        except Exception as e:
            print(f"Error al registrar el período: {e}")
        time.sleep(3)

    def update(self):
        borrarPantalla()
        print("Actualizar datos de Período Académico")
        try:
            periodos = self.json_file.read()
            if periodos:
                while True:
                    try:
                        periodo_id = int(input("Ingrese el ID del período: ").strip())
                        break
                    except ValueError:
                        print("ID inválido. Debe ser un número entero.")

                for periodo in periodos:
                    if periodo['id'] == periodo_id:
                        print(f"Período encontrado: {periodo['descripcion']} (Fecha de inicio: {periodo['fecha_inicio']})")

                        # Validar que la descripción no esté vacía
                        periodo['descripcion'] = input(f"Ingrese la nueva descripción (actual: {periodo['descripcion']}): ").strip() or periodo['descripcion']

                        # Validar formato y lógica de fechas
                        while True:
                            fecha_inicio_str = input(f"Ingrese la nueva fecha de inicio (actual: {periodo['fecha_inicio']}) (YYYY-MM-DD): ").strip()
                            if fecha_inicio_str:
                                try:
                                    fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d').date()
                                    if fecha_inicio <= datetime.strptime(periodo['fecha_fin'], '%Y-%m-%d').date():
                                        periodo['fecha_inicio'] = fecha_inicio_str
                                        break
                                    else:
                                        print("La nueva fecha de inicio debe ser anterior o igual a la fecha de fin.")
                                except ValueError:
                                    print("Fecha de inicio inválida. Debe estar en formato YYYY-MM-DD.")
                            else:
                                periodo['fecha_inicio'] = periodo['fecha_inicio']

                        while True:
                            fecha_fin_str = input(f"Ingrese la nueva fecha de fin (actual: {periodo['fecha_fin']}) (YYYY-MM-DD): ").strip()
                            if fecha_fin_str:
                                try:
                                    fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%d').date()
                                    if fecha_fin >= datetime.strptime(periodo['fecha_inicio'], '%Y-%m-%d').date():
                                        periodo['fecha_fin'] = fecha_fin_str
                                        break
                                    else:
                                        print("La nueva fecha de fin debe ser igual o posterior a la fecha de inicio.")
                                except ValueError:
                                    print("Fecha de fin inválida. Debe estar en formato YYYY-MM-DD.")
                            else:
                                periodo['fecha_fin'] = periodo['fecha_fin']

                        while True:
                            active_str = input("Período activo (True/False): ").strip().lower()
                            if active_str in ['true', 'false']:
                                periodo['active'] = active_str == 'true'
                                break
                            print("Debe ingresar 'True' o 'False'.")

                        self.json_file.save(periodos)
                        print("Datos actualizados correctamente.")
                        break
                else:
                    print("Período no encontrado.")
            else:
                print("No hay períodos registrados.")
        except Exception as e:
            print(f"Error al actualizar el período: {e}")
        time.sleep(3)

    def delete(self):
        borrarPantalla()
        print("Eliminar Período Académico")
        try:
            periodos = self.json_file.read()
            if periodos:
                while True:
                    try:
                        periodo_id = int(input("Ingrese el ID del Período a eliminar: ").strip())
                        break
                    except ValueError:
                        print("ID inválido. Debe ser un número entero.")

                for periodo in periodos:
                    if periodo['id'] == periodo_id:
                        periodos.remove(periodo)
                        self.json_file.save(periodos)
                        print(f"Período con ID {periodo_id} eliminado correctamente.")
                        break
                else:
                    print("Período no encontrado.")
            else:
                print("No hay períodos registrados.")
        except Exception as e:
            print(f"Error al eliminar el período: {e}")
        time.sleep(3)

    def consult(self):
        borrarPantalla()
        print("Consulta de Períodos Académicos")
        try:
            periodos = self.json_file.read()
            if periodos:
                print("Lista de Períodos registrados:")
                for periodo in periodos:
                    print(f"ID: {periodo['id']} | Descripción: {periodo['descripcion']} | "
                          f"Fecha Inicio: {periodo['fecha_inicio']} | Fecha Fin: {periodo['fecha_fin']} | Activo: {periodo['active']}")
            else:
                print("No hay períodos registrados.")
        except Exception as e:
            print(f"Error al consultar los períodos: {e}")
        time.sleep(3)
