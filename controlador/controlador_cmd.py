from modelo import queries
from vista import vista_cmd

def mainloop():
    
    flag_funcionamiento = True
    while flag_funcionamiento:
        opcion = vista_cmd.menu_principal()
        if opcion == 1:
            listado_completo_lideres = queries.lideres_completos()
            vista_cmd.mostrar_lideres_completos(listado_lideres=listado_completo_lideres)
        elif opcion == 2:
            numero = vista_cmd.numero_lideres()
            lista_lideres = queries.listado_lideres_limitado(numero)
            vista_cmd.mostrar_lideres_limitado(lista_lideres)
        elif opcion == 0:
            flag_funcionamiento = False
        else:
            vista_cmd.mensaje_error("Opción inválida")