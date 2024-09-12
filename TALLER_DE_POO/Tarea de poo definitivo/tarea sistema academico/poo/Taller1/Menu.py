import os
import shutil
import time
from Utilidades import reset_color, orange_color, gold_color, lime_green_color, pink_color, teal_color, magenta_color
from Utilidades import borrarPantalla
from CrudEstudiante import CrudEstudiante
from CrudProfesor import CrudProfesor
from CrudAsignatura import CrudAsignatura
from IcrudNivel import CrudNivel
from CrudPeriodo import CrudPeriodo
from crudnotas import CrudNotas
from Nota import Nota

# Obtener dimensiones de la consola
def obtener_dimensiones():
    size = shutil.get_terminal_size()
    return size.lines, size.columns

# Función para dibujar el menú
def dibujar_menu_simple(titulo, opciones, color_titulo, color_opciones, color_numeros):
    # Obtener dimensiones de la consola
    _, ancho_terminal = obtener_dimensiones()

    # Ancho del menú
    ancho_max = max(len(titulo), max(len(opcion) for opcion in opciones)) + 20
    ancho_max = min(ancho_max, ancho_terminal - 20)  # Ajustar el ancho al tamaño de la terminal

    # Centrar el menú en la terminal
    espacio_izquierda = (ancho_terminal - ancho_max) // 2

    # Imprimir el menú centrado
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar pantalla

    print(f"{' ' * espacio_izquierda}{color_titulo}{titulo.center(ancho_max)}{reset_color}")
    print(f"{' ' * espacio_izquierda}{color_titulo}{'─' * (ancho_max)}{reset_color}")

    for i, opcion in enumerate(opciones, 1):
        print(f"{' ' * espacio_izquierda}{color_numeros}{str(i).rjust(2)}.{reset_color} {color_opciones}{opcion.ljust(ancho_max - 4)}{reset_color}")

    print(f"{' ' * espacio_izquierda}{color_titulo}{'─' * (ancho_max)}{reset_color}")

    # Solicitud de entrada
    opcion = input(f"{' ' * espacio_izquierda}Elija opción: ")
    return opcion

# Menu Principal
opc = " "
while opc != '7':  # Cambiado a '7' para incluir la nueva opción
    borrarPantalla()
    # Llamar a la función para dibujar el menú principal
    opc = dibujar_menu_simple("👨‍💻Menú de Gestión👨‍💻", 
                     ["Gestión de Periodo", "Gestión de Nivel", "Gestión de Asignaturas", "Gestión de Profesores", "Gestión de Estudiantes", "Gestión de Notas", "Salir"], 
                     color_titulo=orange_color, color_opciones=pink_color, color_numeros=reset_color)

    if opc == '1':
        opc1 = ""
        while opc1 != "5":
            borrarPantalla()
            opc1 = dibujar_menu_simple("👨‍💻Menú de Periodo👨‍💻", 
                          ["Nuevo Periodo", "Actualizar Periodo", "Eliminar Periodo", "Consultar Periodo", "Salir"], 
                          color_titulo=pink_color, color_opciones=magenta_color, color_numeros=reset_color)
            crud = CrudPeriodo()
            if opc1 == '1':
                print("Crear periodo...")
                crud.create()
            elif opc1 == '2':
                print("Actualizar periodo...")
                crud.update()
            elif opc1 == '3':
                print("Eliminar periodo...")
                crud.delete()
            elif opc1 == '4':
                print("Consultar periodo...")
                crud.consult()
            elif opc1 == '5':
                print("Regresando al menú principal")
              
    elif opc == '2':
        opc2 = ""
        while opc2 != '5':
            borrarPantalla()
            opc2 = dibujar_menu_simple("👨‍💻Menú de Nivel👨‍💻", 
                          ["Nuevo Nivel", "Actualizar Nivel", "Eliminar Nivel", "Consultar Nivel", "Salir"], 
                          color_titulo=orange_color, color_opciones=teal_color, color_numeros=reset_color)
            crud = CrudNivel()
            if opc2 == '1':
                print("Crear nivel...")
                crud.create()
            elif opc2 == '2':
                print("Actualizar nivel...")
                crud.update()
            elif opc2 == '3':
                print("Eliminar nivel...")
                crud.delete()
            elif opc2 == '4':
                print("Consultar nivel...")
                crud.consult()
            elif opc2 == '5':
                print("Regresando al menú principal")
               
    elif opc == '3':
        opc3 = ""
        while opc3 != '5':
            borrarPantalla()
            opc3 = dibujar_menu_simple("👨‍💻Menú de Asignatura👨‍💻", 
                          ["Nueva Asignatura", "Actualizar Asignatura", "Eliminar Asignatura", "Consultar Asignatura", "Salir"], 
                          color_titulo=lime_green_color, color_opciones=gold_color, color_numeros=reset_color)
            crud = CrudAsignatura()
            if opc3 == '1':
                print("Crear asignatura...")
                crud.create()
            elif opc3 == '2':
                print("Actualizar asignatura...")
                crud.update()
            elif opc3 == '3':
                print("Eliminar asignatura...")
                crud.delete()
            elif opc3 == '4':
                print("Consultar asignatura...")
                crud.consult()
            elif opc3 == '5':
                print("Regresando al menú principal")
               
    elif opc == '4':
        opc4 = ""
        while opc4 != "5":
            borrarPantalla()
            opc4 = dibujar_menu_simple("👨‍💻Menú de Profesor👨‍💻", 
                          ["Nuevo Profesor", "Actualizar Profesor", "Eliminar Profesor", "Consultar Profesor", "Salir"], 
                          color_titulo=pink_color, color_opciones=lime_green_color, color_numeros=reset_color)
            crud = CrudProfesor()
            if opc4 == '1':
                print("Crear profesor...")
                crud.create()
            elif opc4 == '2':
                print("Actualizar profesor...")
                crud.update()
            elif opc4 == '3':
                print("Eliminar profesor...")
                crud.delete()
            elif opc4 == '4':
                print("Consultar profesor...")
                crud.consult()
            elif opc4 == '5':
                print("Regresando al menú principal")
           
    elif opc == "5":
        opc5 = ""
        while opc5 != "5":
            borrarPantalla()
            opc5 = dibujar_menu_simple("👨‍💻Menú de Estudiante👨‍💻", 
                          ["Nuevo Estudiante", "Actualizar Estudiante", "Eliminar Estudiante", "Consultar Estudiante", "Salir"], 
                          color_titulo=pink_color, color_opciones=lime_green_color, color_numeros=reset_color)
            crud = CrudEstudiante()
            if opc5 == '1':
                print("Crear estudiante...")
                crud.create()
            elif opc5 == '2':
                print("Actualizar estudiante...")
                crud.update()
            elif opc5 == '3':
                print("Eliminar estudiante...")
                crud.delete()
            elif opc5 == '4':
                print("Consultar estudiante...")
                crud.consult()
            elif opc5 == '5':
                print("Regresando al menú principal")
    
    elif opc == '6':
        opc6 = ""
        while opc6 != "5":
            borrarPantalla()
            opc6 = dibujar_menu_simple("👨‍💻Menú de Notas👨‍💻", 
                          ["Crear Nota", "Actualizar Nota", "Eliminar Nota", "Consultar Nota", "Salir"], 
                          color_titulo=lime_green_color, color_opciones=gold_color, color_numeros=reset_color)
            crud = CrudNotas()  # Define la instancia de crud aquí

            if opc6 == '1':
                print("Crear nota...")
                crud.create()
                input("Presiona Enter para regresar al menú principal...")
            elif opc6 == '2':
                print("Actualizar nota...")
                crud.update()
            elif opc6 == '3':
                print("Eliminar nota...")
                crud.delete()
            elif opc6 == '4':
                print("Consultar nota...")
                crud.consult()
            elif opc6 == '5':
                print("Regresando al menú principal")
              
borrarPantalla()
print("Adiós........👋👋👋")
time.sleep(2)
