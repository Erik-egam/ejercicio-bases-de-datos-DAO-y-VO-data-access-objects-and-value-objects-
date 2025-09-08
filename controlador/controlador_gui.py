from modelo import dml
from vista import vista_gui
from modelo.dao.TrabajadorDAO import TrabajadorDAO
from modelo.dao.ArbolDAO import ArbolDAO


from PyQt5.QtWidgets import QApplication
import sys


# Instalar PyQt5
# python -m pip install PyQt5

class ControladorGUI:
    def mainloop(self):

        # Mostrar la vista principal
        self.ventana_principal.show()

        # Ejecutar la aplicación (proceso, thread)
        self.app.exec_()

    def __init__(self):

        # Instanciar una aplicación
        self.app = QApplication(sys.argv)
        # app = QApplication([])
        self.arbolAux = ArbolDAO()
        # Construir y mostrar la vista
        self.ventana_principal = vista_gui.VentanaPrincipal()
        self.ventana_trabajadores = vista_gui.VentanaTrabajadores()
        self.ventana_arboles = vista_gui.VentanaArboles()

        # Creacion del formulario
        self.formulario_trabajador = vista_gui.FormularioNuevoTrabajador()
        self.formulario_arbol = vista_gui.FormularioNuevoArbol()

        # Formulario actualizar lider
        self.formulario_actualizar_Trabajador = vista_gui.FormularioModificarTrabajador()
        self.formulario_actualizar_arbol = vista_gui.FormularioModificarArbol()

        # Asociar los handlers de las señales
        self._setup_handlers()

    def _setup_handlers(self):

        def handler_modificacion_trabajador(fila: int, columna: int):
            print(f"Evento Doble Click -> {fila} {columna}")

            self.formulario_actualizar_Trabajador.id_trabajador_update = self.ventana_trabajadores.w['tabla_trabajador'].item(
                fila, 0).text()
            self.formulario_actualizar_Trabajador.w['label_id'].setText(
                self.formulario_actualizar_Trabajador.id_trabajador_update)

            self.formulario_actualizar_Trabajador.show()

        # Definir acciones trabajadores
        def handler_ventana_trabajadores():
            # pp.pprint(TrabajadorDAO().get_all())
            self.ventana_trabajadores.show()

        def handler_nuevo_trabajador():
            self.formulario_trabajador.show()

        def handler_formulario_insertar_trabajador():
            tupla_nuevo_trabajador = (
                self.formulario_trabajador.w['input_nombre'].text())
            dml.insert_trabajador(nuevo_trabajador=tupla_nuevo_trabajador)

        def handler_llenar_tabla_trabajadores():
            listado_trabajadores = TrabajadorDAO().get_all()
            self.ventana_trabajadores.llenarTabla(
                listado_trabajadores=listado_trabajadores)

        # Definir acciones arboles

        def handler_ventana_arboles():
            # pp.pprint(TrabajadorDAO().get_all())
            self.ventana_arboles.show()

        def handler_nuevo_arbol():
            self.formulario_arbol.show()

        def handler_formulario_insertar_arbol():
            tupla_nuevo_arbol = (
                self.formulario_arbol.w['input_terreno'].text())
            dml.insert_arbol(nuevo_arbol=tupla_nuevo_arbol)

        def handler_llenar_tabla_arboles():
            listado_arboles = ArbolDAO().get_all()
            self.ventana_arboles.llenarTabla(listado_arboles=listado_arboles)

        def handler_modificacion_arbol(fila: int, columna: int):
            print(f"Evento Doble Click -> {fila} {columna}")

            self.formulario_actualizar_arbol.id_arbol_update = self.ventana_arboles.w['tabla_arbol'].item(
                fila, 0).text()
            enfermedades = self.arbolAux.get_enfermedad_by_arbol_id(
                arbol=self.formulario_actualizar_arbol.id_arbol_update)
            self.formulario_actualizar_arbol.llenarTablaEnfermedades(
                enfermedades)
            tareas = self.arbolAux.get_tarea_by_arbol_id(
                arbol=self.formulario_actualizar_arbol.id_arbol_update)
            self.formulario_actualizar_arbol.llenarTablaTareas(tareas)
            self.formulario_actualizar_arbol.w['label_id'].setText(
                self.formulario_actualizar_arbol.id_arbol_update)

            self.formulario_actualizar_arbol.show()

        def handler_nueva_enfermedad():
            self.formulario_actualizar_arbol.formulario_enfermedad.show()

        def handler_formulario_insertar_enfermedad():
            tupla_nueva_enfermedad = (self.formulario_actualizar_arbol.id_arbol_update,
                                      self.formulario_actualizar_arbol.formulario_enfermedad.w['input_fecha'].text())
            dml.insert_enfermedad(nueva_enfermedad=tupla_nueva_enfermedad)


        def handler_modificacion_enfermedad(fila: int, columna: int):
            print(f"Evento Doble Click -> {fila} {columna}")

            self.formulario_actualizar_arbol.formulario_modificar_enfermedad.id_enfermedad_update = fila + 1
            self.formulario_actualizar_arbol.formulario_modificar_enfermedad.id_arbol_update = self.formulario_actualizar_arbol.id_arbol_update
            self.formulario_actualizar_arbol.formulario_modificar_enfermedad.w['label_id'].setText(
                str(self.formulario_actualizar_arbol.formulario_modificar_enfermedad.id_enfermedad_update))

            self.formulario_actualizar_arbol.formulario_modificar_enfermedad.show()
            # No funciona correctamente problema de diseño de la base de datos
            
            
        def handler_nueva_tarea():
            self.formulario_actualizar_arbol.formulario_tarea.show()

        def handler_formulario_insertar_tarea():
            tupla_nueva_tarea = (
                self.formulario_actualizar_arbol.id_arbol_update,
                self.formulario_actualizar_arbol.formulario_tarea.w['input_fecha'].text(),
                self.formulario_actualizar_arbol.formulario_tarea.w['input_mezcla'].text()
            )
            dml.insert_tarea(nueva_tarea=tupla_nueva_tarea)

        # Botones pantalla principal

        # Al inicio de cada linea de codigo esta el nombre de la ventana la cual va a activar el handler

        # Inicio de la ventana
        self.ventana_principal.w['btn_Trabajadores'].clicked.connect(
            handler_ventana_trabajadores)
        self.ventana_principal.w['btn_Trabajadores'].clicked.connect(
            handler_llenar_tabla_trabajadores)

        self.ventana_principal.w['btn_Arboles'].clicked.connect(
            handler_ventana_arboles)
        self.ventana_principal.w['btn_Arboles'].clicked.connect(
            handler_llenar_tabla_arboles)

        # llenar tablas
        self.ventana_trabajadores.w['btn_Listar_trabajadores'].clicked.connect(
            handler_llenar_tabla_trabajadores)

        self.ventana_arboles.w['btn_Listar_arboles'].clicked.connect(
            handler_llenar_tabla_arboles)

        # Registrar
        self.ventana_trabajadores.w['btn_Registrar_trabajador'].clicked.connect(
            handler_nuevo_trabajador)
        self.formulario_trabajador.w['btn_guardar'].clicked.connect(
            handler_formulario_insertar_trabajador)
        self.formulario_trabajador.w['btn_guardar'].clicked.connect(
            handler_llenar_tabla_trabajadores)

        self.ventana_arboles.w['btn_Registrar_arbol'].clicked.connect(
            handler_nuevo_arbol)
        self.formulario_arbol.w['btn_guardar'].clicked.connect(
            handler_formulario_insertar_arbol)
        self.formulario_arbol.w['btn_guardar'].clicked.connect(
            handler_llenar_tabla_arboles)
        self.formulario_actualizar_arbol.w['btn_guardar'].clicked.connect(
            handler_llenar_tabla_arboles)

        self.formulario_actualizar_arbol.w['btn_registrar_enfermedad'].clicked.connect(
            handler_nueva_enfermedad)
        self.formulario_actualizar_arbol.formulario_enfermedad.w['btn_guardar'].clicked.connect(
            handler_formulario_insertar_enfermedad)

        self.formulario_actualizar_arbol.w['btn_registrar_tarea'].clicked.connect(
            handler_nueva_tarea)
        self.formulario_actualizar_arbol.formulario_tarea.w['btn_guardar'].clicked.connect(
            handler_formulario_insertar_tarea)

        # Modificar
        self.ventana_trabajadores.w['tabla_trabajador'].cellDoubleClicked.connect(
            handler_modificacion_trabajador)
        self.formulario_actualizar_Trabajador.w['btn_guardar'].clicked.connect(
            handler_llenar_tabla_trabajadores)

        self.ventana_arboles.w['tabla_arbol'].cellDoubleClicked.connect(
            handler_modificacion_arbol)
        
        self.formulario_actualizar_arbol.w['tabla_enfermedad'].cellDoubleClicked.connect(
            handler_modificacion_enfermedad)
