import os
import json

class JsonFile:
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        # Asegúrate de que el directorio existe
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        try:
            with open(self.filename, 'w') as file:
                json.dump(data, file, indent=4)  # Añadido indent para formato
        except IOError as e:
            print(f"Error al guardar en el archivo: {e}")

    def read(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)  # Cargar datos desde el archivo JSON
        except FileNotFoundError:
            data = []
        except json.JSONDecodeError as e:
            print(f"Error decodificando JSON: {e}")
            data = []
        return data

    def find(self, atributo, buscado):
        try:
            with open(self.filename, 'r') as file:
                datas = json.load(file)
                data = [item for item in datas if item[atributo] == buscado]
        except FileNotFoundError:
            data = []
        except json.JSONDecodeError as e:
            print(f"Error decodificando JSON: {e}")
            data = []
        return data
