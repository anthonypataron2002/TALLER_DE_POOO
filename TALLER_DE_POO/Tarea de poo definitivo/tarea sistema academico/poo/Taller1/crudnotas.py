from Utilidades import reset_color, green_color, blue_color, purple_color,borrarPantalla, gotoxy, linea
from clsJson import JsonFile
from Nota import Nota, DetalleNota
import os
import time


path, file = os.path.split(__file__)

class CrudNotas:
    json_estudiantes = JsonFile(path + '/data/Estudiante.json')
    json_nota = JsonFile(path + '/data/notas.json')
    json_asignaturas = JsonFile(path + '/data/Asignatura.json')
    json_periodos = JsonFile(path + '/data/Periodo.json')
    json_profesores = JsonFile(path + '/data/Profesor.json')
    def create(self):
       borrarPantalla()
       linea(80, green_color)
       print(f"{purple_color}Crear Nota")
       linea(80, green_color)
       
       n_profesor = int(input(f"profesor:"))
       profesor = self.json_profesores.find("id", n_profesor)
       profesor = profesor[0]
       print(f"Nombre del profesor: {profesor['nombre']} Apellido: {profesor['apellido']}")
       
       n_asignatura = int(input(f"Asignatura:"))
       asignatura = self.json_asignaturas.find("id", n_asignatura)
       asignatura = asignatura[0]
       print(f"{asignatura["descripcion"]}")
       
       n_periodo = int(input(f"Periodo:"))
       periodo = self.json_periodos.find("id", n_periodo)
       periodo = periodo[0]
       print(f"{periodo["fecha_inicio"]} - {periodo["fecha_fin"]}")
       
       nota = Nota(1, periodo, profesor, asignatura)
       
       n_estudiantes = int(input(f"Estudiantes:"))
       estudiantes = self.json_estudiantes.find("id", n_estudiantes)
       estudiantes = estudiantes[0]
       print(f"{estudiantes["nombre"]} {estudiantes["apellido"]}")
       
       nota1 = float(input(f"Nota 1:"))
       nota2 = float(input(f"Nota 2:"))
       recuperacion = float(input(f"Recuperacion:"))
       
       detalle_nota = DetalleNota(nota.id, estudiantes, nota1, nota2, recuperacion)
       
       nota.add_nota(detalle_nota) 
       
       notas = self.json_nota.read()
       notas.append(nota.getJson())
       self.json_nota.save(notas)

    def update(self):
        print("Actualizar nota...")

        # Leer las notas desde el archivo JSON usando json_nota
        notas = self.json_nota.read()

        id_nota_str = input("Ingrese el ID de la nota que desea actualizar: ").strip()
        if not id_nota_str.isdigit():
            print("ID de nota inválido. Debe ser un número entero.")
            return

        id_nota = int(id_nota_str)

        # Buscar la nota con el ID proporcionado
        nota_encontrada = next((n for n in notas if n.get('id') == id_nota), None)
        if not nota_encontrada:
            print(f"No se encontró una nota con el ID {id_nota}.")
            return

        print("Nota encontrada:")
        print(nota_encontrada)

        # Actualizar los campos de la nota
        periodo = input(f"Nuevo periodo (actual: {nota_encontrada['periodo']}): ") or nota_encontrada['periodo']
        profesor = input(f"Nuevo profesor (actual: {nota_encontrada['profesor']}): ") or nota_encontrada['profesor']
        asignatura = input(f"Nueva asignatura (actual: {nota_encontrada['asignatura']}): ") or nota_encontrada['asignatura']

        nota_encontrada.update({
            'periodo': periodo,
            'profesor': profesor,
            'asignatura': asignatura
        })

        # Actualizar los detalles de la nota
        while True:
            id_detalle_str = input("Ingrese el ID del detalle que desea actualizar (0 para salir): ").strip()
            if not id_detalle_str.isdigit():
                print("ID de detalle inválido. Debe ser un número entero.")
                continue

            id_detalle = int(id_detalle_str)

            if id_detalle == 0:
                break

            detalle_encontrado = next((d for d in nota_encontrada.get('detalle_notas', []) if d['id'] == id_detalle), None)
            if not detalle_encontrado:
                print(f"No se encontró un detalle con el ID {id_detalle}.")
                continue

            print("Detalle encontrado:")
            print(detalle_encontrado)

            # Actualizar detalles
            estudiante = input(f"Nuevo estudiante (actual: {detalle_encontrado['estudiante']}): ") or detalle_encontrado['estudiante']
            nota1_str = input(f"Nueva calificación 1 (actual: {detalle_encontrado['nota1']}): ") or detalle_encontrado['nota1']
            nota2_str = input(f"Nueva calificación 2 (actual: {detalle_encontrado['nota2']}): ") or detalle_encontrado['nota2']
            recuperacion_str = input(f"Nuevo recuperacion (actual: {detalle_encontrado['recuperacion']}): ") or detalle_encontrado['recuperacion']
            observacion = input(f"Nueva observación (actual: {detalle_encontrado['observacion']}): ") or detalle_encontrado['observacion']

            try:
                nota1 = float(nota1_str)
                nota2 = float(nota2_str)
                recuperacion = float(recuperacion_str) if recuperacion_str else None
            except ValueError:
                print("Las calificaciones y la recuperación deben ser números válidos.")
                continue

            # Actualizar los campos del detalle
            detalle_encontrado.update({
                'estudiante': estudiante,
                'nota1': nota1,
                'nota2': nota2,
                'recuperacion': recuperacion,
                'observacion': observacion
            })

        # Guardar las notas actualizadas
        self.json_nota.save(notas)
        print("Nota actualizada exitosamente.")


    def delete(self):
        print("Eliminar nota...")

        # Leer todas las notas
        notas = self.json_nota.read()
        
        if not notas:
            print("No hay notas registradas.")
            return

        # Solicitar el ID de la nota a eliminar
        id_nota_str = input("Ingrese el ID de la nota que desea eliminar: ").strip()
        
        # Validar que el ID ingresado es un número entero
        if not id_nota_str.isdigit():
            print("ID inválido. Debe ser un número entero.")
            return
        
        id_nota = int(id_nota_str)

        # Buscar la nota con el ID proporcionado
        nota_encontrada = next((n for n in notas if n.get('id') == id_nota), None)
        
        # Si la nota no se encuentra, mostrar un mensaje y salir
        if not nota_encontrada:
            print(f"No se encontró una nota con el ID {id_nota}.")
            return

        # Confirmación antes de eliminar
        confirmacion = input(f"¿Está seguro que desea eliminar la nota con ID {id_nota}? (s/n): ").strip().lower()
        if confirmacion != 's':
            print("Operación cancelada.")
            return

        # Filtrar la lista para eliminar la nota con el ID proporcionado
        notas = [n for n in notas if n['id'] != id_nota]

        # Guardar la lista actualizada en el archivo JSON
        self.json_nota.save(notas)
        
        print(f"Nota con ID {id_nota} eliminada exitosamente.")


    def consult(self):
        borrarPantalla()
        print(f"{purple_color}Consultar Notas")
        id_nota = int(input(f"ID de la nota:"))
        nota = self.json_nota.find("id", id_nota)
        nota = nota[0]
        print(f"ID: {nota['id']}")
        print(f"Periodo: {nota['periodo']}")
        print(f"Profesor: {nota['profesor']}")
        print(f"Asignatura: {nota['asignatura']}")
        print(f"Detalle de notas:")
        for detalle in nota['detalle_notas']:
            print(f"Estudiante: {detalle['estudiante']}")
            print(f"Nota 1: {detalle['nota1']}")
            print(f"Nota 2: {detalle['nota2']}")
            print(f"Recuperación: {detalle['recuperacion']}")
            print(f"Observación: {detalle['observacion']}")
            print("")
        time.sleep(5)
        input("Presiona Enter para regresar al menú principal...")
        return
    