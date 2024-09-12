import os
import datetime
import time
reset_color = "\033[0m"
orange_color = "\033[38;5;214m"  # Naranja brillante
lime_green_color = "\033[38;5;154m"  # Verde lima brillante
pink_color = "\033[38;5;200m"  # Rosa brillante
teal_color = "\033[38;5;49m"  # Verde azulado
gold_color = "\033[38;5;220m"  # Dorado brillante
magenta_color = "\033[38;5;201m"  # Magenta brillante
reset_color = "\033[0m"
red_color = "\033[91m"
green_color = "\033[92m"
yellow_color = "\033[93m"
blue_color = "\033[94m"
purple_color = "\033[95m"
cyan_color = "\033[96m"

def gotoxy(x,y):
    print("%c[%d;%df"%(0x1B,y,x),end="")

def borrarPantalla():
    os.system("cls") 

def mensaje(msg,f,c):
    pass

def linea(longitud, color):
    print(f"{color}{longitud * '-'}{reset_color}")

path, _ = os.path.split(os.path.abspath(__file__))
print(path)


