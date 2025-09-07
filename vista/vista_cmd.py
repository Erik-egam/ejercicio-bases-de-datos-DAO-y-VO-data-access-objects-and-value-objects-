import pprint as pp
from modelo import *

def menu_principal()->int:
    print("---------------------")
    print("1. Listar Líderes")
    print("2. Listar Líderes Limitados")
    print("0. Salir")
    print("---------------------")
    opcion = int(input("Ingresar opción: "))
    return opcion

def mostrar_lideres_completos(listado_lideres:list)->None:
    print("-----> Listado Líderes <------")
    pp.pprint(listado_lideres)

def mensaje_error(mensaje:str)->None:
    print("!!!!!!!!!!!")
    print(mensaje)
    print("!!!!!!!!!!!")


def mostrar_lideres_limitado(listado_lideres:list)->None:
    print("--------Listado de lideres limitados-------")
    pp.pprint(listado_lideres)
    print("!!!!!!!!!")

def numero_lideres()->int:
    return int(input("Numero de lideres: "))
