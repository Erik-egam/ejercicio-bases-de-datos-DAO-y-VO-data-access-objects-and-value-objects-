from modelo.vo.TrabajadorVO import TrabajadorVO
from modelo import queries, dml
from PyQt5.QtWidgets import (QPushButton,
                             QVBoxLayout,
                             QHBoxLayout,
                             QTableWidget,
                             QHeaderView,
                             QTableWidgetItem,
                             QFormLayout,
                             QSlider,
                             QFrame,
                             QLabel,
                             QWidget,
                             QDialog,
                             QLineEdit)
# para darle estilos al texto dandole tipografia, tamaño y peso(bold)
from PyQt5.QtGui import QFont
# Es todo el framework
from PyQt5.QtCore import Qt

from modelo import dml


class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        # titulo de la ventana principal
        self.setWindowTitle("Sistema Gestión de Producción de Aguacate")
        self.setGeometry(100, 100, 800, 600)

        # diccionario con widgets
        self.w = dict()

        # título grande
        self.w['lbl_titulo'] = QLabel(
            "Sistema Gestión de Producción de Aguacate")
        self.w['lbl_titulo'].setFont(QFont("Arial", 18, QFont.Bold))
        self.w['lbl_titulo'].setAlignment(Qt.AlignCenter)

        # botones
        self.w['btn_Trabajadores'] = QPushButton("Ventana de Trabajadores")
        self.w['btn_Arboles'] = QPushButton("Ventana de Árboles")
        self.w['btn_Tareas'] = QPushButton("Ventana de Tareas")

        # aplicar estilo a botones
        for key in ['btn_Trabajadores', 'btn_Arboles', 'btn_Tareas']:
            self.w[key].setMinimumHeight(50)
            self.w[key].setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    border-radius: 10px;
                    font-size: 14px;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: #45a049;
                }
            """)

        # marco para agrupar botones
        self.w['frame_menu'] = QFrame()
        frame_layout = QVBoxLayout(self.w['frame_menu'])
        frame_layout.setSpacing(20)
        frame_layout.addWidget(self.w['btn_Trabajadores'])
        frame_layout.addWidget(self.w['btn_Arboles'])
        frame_layout.addWidget(self.w['btn_Tareas'])

        self.w['frame_menu'].setStyleSheet("""
            QFrame {
                background-color: #f5f5f5;
                border: 1px solid #ddd;
                border-radius: 15px;
                padding: 20px;
            }
        """)

        # layout principal
        self.layout_principal = QVBoxLayout()
        self.layout_principal.addWidget(self.w['lbl_titulo'])
        self.layout_principal.addStretch()
        self.layout_principal.addWidget(
            self.w['frame_menu'], alignment=Qt.AlignCenter)
        self.layout_principal.addStretch()

        self.setLayout(self.layout_principal)


class VentanaTrabajadores(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema Administración de Trabajadores")
        self.setGeometry(100, 100, 800, 600)

        self.w = dict()

        # título
        self.w['lbl_titulo'] = QLabel("Administración de Trabajadores")
        self.w['lbl_titulo'].setFont(QFont("Arial", 18, QFont.Bold))
        self.w['lbl_titulo'].setAlignment(Qt.AlignCenter)

        # botones
        self.w['btn_Listar_trabajadores'] = QPushButton(
            "Listar todos los trabajadores")
        self.w['btn_Registrar_trabajador'] = QPushButton(
            "Registrar un nuevo trabajador")

        for key in ['btn_Listar_trabajadores', 'btn_Registrar_trabajador']:
            self.w[key].setMinimumHeight(40)
            self.w[key].setStyleSheet("""
                QPushButton {
                    background-color: #2196F3;
                    color: white;
                    border-radius: 8px;
                    font-size: 13px;
                    padding: 8px;
                }
                QPushButton:hover {
                    background-color: #1976D2;
                }
            """)

        # marco para botones en horizontal
        self.w['frame_botones'] = QFrame()
        botones_layout = QHBoxLayout(self.w['frame_botones'])
        botones_layout.setSpacing(15)
        botones_layout.addWidget(self.w['btn_Listar_trabajadores'])
        botones_layout.addWidget(self.w['btn_Registrar_trabajador'])

        self.w['frame_botones'].setStyleSheet("""
            QFrame {
                background-color: #f0f0f0;
                border: 1px solid #ddd;
                border-radius: 10px;
                padding: 10px;
            }
        """)

        # tabla
        self.w['tabla_trabajador'] = QTableWidget()
        self.w['tabla_trabajador'].horizontalHeader(
        ).setSectionResizeMode(QHeaderView.Stretch)
        self.w['tabla_trabajador'].setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 8px;
                gridline-color: #ddd;
                font-size: 12px;
            }
            QHeaderView::section {
                background-color: #2196F3;
                color: white;
                padding: 5px;
                border: none;
            }
        """)

        # layout principal
        self.layout_principal = QVBoxLayout()
        self.layout_principal.addWidget(self.w['lbl_titulo'])
        self.layout_principal.addWidget(self.w['frame_botones'])
        self.layout_principal.addWidget(self.w['tabla_trabajador'])

        self.setLayout(self.layout_principal)

    def llenarTabla(self, listado_trabajadores):
        self.w['tabla_trabajador'].setColumnCount(5)
        self.w['tabla_trabajador'].setHorizontalHeaderLabels(
            ['id', 'Nombre', 'telefono', 'EPS', 'ARL'])
        self.w['tabla_trabajador'].setRowCount(len(listado_trabajadores))
        for indice, trabajador in enumerate(listado_trabajadores):
            itemID = QTableWidgetItem(str(trabajador.id_trab))
            itemID.setFlags(itemID.flags() & ~Qt.ItemIsEditable)
            self.w['tabla_trabajador'].setItem(indice, 0, itemID)
            self.w['tabla_trabajador'].setItem(
                indice, 1, QTableWidgetItem(trabajador.nombre))
            self.w['tabla_trabajador'].setItem(
                indice, 2, QTableWidgetItem(trabajador.telefono))
            self.w['tabla_trabajador'].setItem(
                indice, 3, QTableWidgetItem(trabajador.EPS))
            self.w['tabla_trabajador'].setItem(
                indice, 4, QTableWidgetItem(trabajador.ARL))


class FormularioNuevoTrabajador(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Formulario Nuevo Trabajador')
        self.setGeometry(100, 100, 400, 300)
        self.w = dict()
        self.w['label_nombre'] = QLabel('Nombre: ')
        self.w['input_nombre'] = QLineEdit()
        self.w['btn_guardar'] = QPushButton('Guardar')
        self.layout_principal = QVBoxLayout()

        for w in self.w.values():
            self.layout_principal.addWidget(w)

        self.setLayout(self.layout_principal)

        self.w['btn_guardar'].clicked.connect(self.accept)


class FormularioModificarTrabajador(QDialog):
    def __init__(self):
        super().__init__()

        self.id_trabajador_update: int

        self.setWindowTitle('Formulario Modificar Trabajador')
        self.setGeometry(100, 100, 400, 200)

        self.w = dict()
        self.w['label_id'] = QLabel("ID: ____")
        self.w['label_nombre'] = QLabel('Nuevo Nombre:')
        self.w['input_nombre'] = QLineEdit()
        self.w['label_telefono'] = QLabel('Nuevo Telefono:')
        self.w['input_telefono'] = QLineEdit()
        self.w['label_EPS'] = QLabel('Nueva EPS:')
        self.w['input_EPS'] = QLineEdit()
        self.w['label_ARL'] = QLabel('Nueva ARL:')
        self.w['input_ARL'] = QLineEdit()

        self.w['btn_guardar'] = QPushButton('Guardar')

        # Placeholder en el campo de texto
        self.w['input_nombre'].setPlaceholderText("Ingrese el nuevo nombre...")
        self.w['input_telefono'].setPlaceholderText(
            "Ingrese el nuevo telefono...")
        self.w['input_EPS'].setPlaceholderText("Ingrese la Nueva EPS...")
        self.w['input_ARL'].setPlaceholderText("Ingrese la nueva ARL")

        # Fuente más clara para labels
        font_label = QFont()
        font_label.setPointSize(10)
        self.w['label_id'].setFont(font_label)
        self.w['label_nombre'].setFont(font_label)
        self.w['label_telefono'].setFont(font_label)
        self.w['label_EPS'].setFont(font_label)
        self.w['label_ARL'].setFont(font_label)

        # Estilo del botón
        self.w['btn_guardar'].setStyleSheet("""
            QPushButton {
                background-color: #2e86de;
                color: white;
                border-radius: 8px;
                padding: 6px 12px;
                font-size: 11pt;
            }
            QPushButton:hover {
                background-color: #1b4f72;
            }
        """)

        # Layout del formulario
        form_layout = QFormLayout()
        form_layout.addRow(self.w['label_id'])
        form_layout.addRow(self.w['label_nombre'], self.w['input_nombre'])
        form_layout.addRow(self.w['label_telefono'], self.w['input_telefono'])
        form_layout.addRow(self.w['label_EPS'], self.w['input_EPS'])
        form_layout.addRow(self.w['label_ARL'], self.w['input_ARL'])
        form_layout.setVerticalSpacing(8)
        # Botón alineado a la derecha
        botones_layout = QHBoxLayout()
        botones_layout.addStretch()
        botones_layout.addWidget(self.w['btn_guardar'])

        # Layout principal con margen
        self.layout_principal = QVBoxLayout()
        self.layout_principal.setContentsMargins(20, 20, 20, 20)
        self.layout_principal.addLayout(form_layout)
        self.layout_principal.addLayout(botones_layout)

        def guardar():
            dml.update_trabajador({"id": int(self.id_trabajador_update),
                                   "nombre": self.w['input_nombre'].text(),
                                   "telefono": self.w['input_telefono'].text(),
                                   "eps": self.w['input_EPS'].text(),
                                   "arl": self.w['input_ARL'].text(),
                                   })
        self.setLayout(self.layout_principal)

        self.w['btn_guardar'].clicked.connect(guardar)
        self.w['btn_guardar'].clicked.connect(self.accept)


# ------------------------------------------
#
#                ARBOLES
#
# ------------------------------------------
class VentanaArboles(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema Administración de Arboles")
        self.setGeometry(100, 100, 800, 600)

        self.w = dict()

        # título
        self.w['lbl_titulo'] = QLabel("Administración de Arboles")
        self.w['lbl_titulo'].setFont(QFont("Arial", 18, QFont.Bold))
        self.w['lbl_titulo'].setAlignment(Qt.AlignCenter)

        # botones
        self.w['btn_Listar_arboles'] = QPushButton("Listar todos los arboles")
        self.w['btn_Registrar_arbol'] = QPushButton("Registrar un nuevo arbol")

        for key in ['btn_Listar_arboles', 'btn_Registrar_arbol']:
            self.w[key].setMinimumHeight(40)
            self.w[key].setStyleSheet("""
                QPushButton {
                    background-color: #2196F3;
                    color: white;
                    border-radius: 8px;
                    font-size: 13px;
                    padding: 8px;
                }
                QPushButton:hover {
                    background-color: #1976D2;
                }
            """)

        # marco para botones en horizontal
        self.w['frame_botones'] = QFrame()
        botones_layout = QHBoxLayout(self.w['frame_botones'])
        botones_layout.setSpacing(15)
        botones_layout.addWidget(self.w['btn_Listar_arboles'])
        botones_layout.addWidget(self.w['btn_Registrar_arbol'])

        self.w['frame_botones'].setStyleSheet("""
            QFrame {
                background-color: #f0f0f0;
                border: 1px solid #ddd;
                border-radius: 10px;
                padding: 10px;
            }
        """)

        # tabla
        self.w['tabla_arbol'] = QTableWidget()
        self.w['tabla_arbol'].horizontalHeader(
        ).setSectionResizeMode(QHeaderView.Stretch)
        self.w['tabla_arbol'].setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 8px;
                gridline-color: #ddd;
                font-size: 12px;
            }
            QHeaderView::section {
                background-color: #2196F3;
                color: white;
                padding: 5px;
                border: none;
            }
        """)

        # layout principal
        self.layout_principal = QVBoxLayout()
        self.layout_principal.addWidget(self.w['lbl_titulo'])
        self.layout_principal.addWidget(self.w['frame_botones'])
        self.layout_principal.addWidget(self.w['tabla_arbol'])

        self.setLayout(self.layout_principal)

    def llenarTabla(self, listado_arboles):

        self.w['tabla_arbol'].setColumnCount(3)
        self.w['tabla_arbol'].setHorizontalHeaderLabels(
            ["ID", "fecha siembra", "terreno"]
        )
        self.w['tabla_arbol'].setRowCount(len(listado_arboles))
        for indice, arbol in enumerate(listado_arboles):
            itemID = QTableWidgetItem(str(arbol.id_arbol))
            itemID.setFlags(itemID.flags() & ~Qt.ItemIsEditable)
            self.w['tabla_arbol'].setItem(indice, 0, itemID)
            self.w['tabla_arbol'].setItem(
                indice, 1, QTableWidgetItem(arbol.fecha_siembra))
            self.w['tabla_arbol'].setItem(
                indice, 2, QTableWidgetItem(arbol.terreno))


class FormularioNuevoArbol(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Formulario Nuevo arbol')
        self.setGeometry(100, 100, 400, 300)
        self.w = dict()
        self.w['label_terreno'] = QLabel('Terreno: ')
        self.w['input_terreno'] = QLineEdit()
        self.w['btn_guardar'] = QPushButton('Guardar')
        self.layout_principal = QVBoxLayout()

        for w in self.w.values():
            self.layout_principal.addWidget(w)

        self.setLayout(self.layout_principal)

        self.w['btn_guardar'].clicked.connect(self.accept)


class FormularioModificarArbol(QDialog):
    def __init__(self):
        super().__init__()

        self.id_arbol_update: int

        self.setWindowTitle('Formulario Modificar arbol')
        self.setGeometry(100, 100, 1500, 400)

        self.w = dict()
        self.w['label_id'] = QLabel("ID: ____")
        self.w['label_terreno'] = QLabel('Nuevo Terreno:')
        self.w['input_terreno'] = QLineEdit()
        

        self.w['btn_guardar'] = QPushButton('Guardar')

        # Placeholder en el campo de texto
        self.w['input_terreno'].setPlaceholderText(
            "Ingrese el nuevo terreno...")

        # Fuente más clara para labels
        font_label = QFont()
        font_label.setPointSize(10)
        self.w['label_id'].setFont(font_label)
        self.w['label_terreno'].setFont(font_label)

        # Estilo del botón
        self.w['btn_guardar'].setStyleSheet("""
            QPushButton {
                background-color: #2e86de;
                color: white;
                border-radius: 8px;
                padding: 6px 12px;
                font-size: 11pt;
            }
            QPushButton:hover {
                background-color: #1b4f72;
            }
        """)

        # Layout del formulario
        form_layout = QFormLayout()
        form_layout.addRow(self.w['label_id'])
        form_layout.addRow(self.w['label_terreno'], self.w['input_terreno'])
        form_layout.setVerticalSpacing(8)
        # Botón alineado a la derecha
        botones_layout = QHBoxLayout()
        botones_layout.addStretch()
        botones_layout.addWidget(self.w['btn_guardar'])

        # Layout principal con margen
        self.layout_principal = QVBoxLayout()
        self.layout_principal.setContentsMargins(20, 20, 20, 20)
        self.layout_principal.addLayout(form_layout)
        self.layout_principal.addLayout(botones_layout)

        def guardar():
            dml.update_arbol({"id": int(self.id_arbol_update),
                              "terreno": self.w['input_terreno'].text()
                              })
        self.setLayout(self.layout_principal)

        self.w['btn_guardar'].clicked.connect(guardar)
        self.w['btn_guardar'].clicked.connect(self.accept)
        
        # tabla
        self.w['tabla_enfermedad'] = QTableWidget()
        self.w['tabla_enfermedad'].horizontalHeader(
        ).setSectionResizeMode(QHeaderView.Stretch)
        self.w['tabla_enfermedad'].setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 8px;
                gridline-color: #ddd;
                font-size: 12px;
            }
            QHeaderView::section {
                background-color: #2196F3;
                color: white;
                padding: 5px;
                border: none;
            }
        """)
        self.layout_principal.addWidget(self.w['tabla_enfermedad'])
        
        # tabla
        self.w['tabla_tarea'] = QTableWidget()
        self.w['tabla_tarea'].horizontalHeader(
        ).setSectionResizeMode(QHeaderView.Stretch)
        self.w['tabla_tarea'].setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 8px;
                gridline-color: #ddd;
                font-size: 12px;
            }
            QHeaderView::section {
                background-color: #2196F3;
                color: white;
                padding: 5px;
                border: none;
            }
        """)
        
        # self.layout_principal.addWidget(self.w['tabla_tarea'])
        
    def llenarTablaEnfermedades(self, listado_enfermedades):
        self.w['tabla_enfermedad'].setColumnCount(4)
        self.w['tabla_enfermedad'].setHorizontalHeaderLabels(
            ["ID", "nombre", "causa", "fecha enfermedad"]
        )
        self.w['tabla_enfermedad'].setRowCount(len(listado_enfermedades))
        for indice, enfermedad in enumerate(listado_enfermedades):
            itemID = QTableWidgetItem(str(enfermedad.id_enfermedad))
            # itemID.setFlags(itemID.flags() & ~Qt.ItemIsEditable)
            self.w['tabla_enfermedad'].setItem(indice, 0, itemID)
            self.w['tabla_enfermedad'].setItem(
                indice, 1, QTableWidgetItem(enfermedad.nombre))
            self.w['tabla_enfermedad'].setItem(
                indice, 2, QTableWidgetItem(enfermedad.causa))
            self.w['tabla_enfermedad'].setItem(
                indice, 3, QTableWidgetItem(enfermedad.fecha_enfermedad))
            
    # def llenarTablaTareas(self, listado_tareas):
    #     self.w['tabla_tarea'].setColumnCount(4)
    #     self.w['tabla_tarea'].setHorizontalHeaderLabels(
    #         ["ID", "nombre", "mezcla", "fecha"]
    #     )
    #     self.w['tabla_tarea'].setRowCount(len(listado_tareas))
    #     for indice, tarea in enumerate(listado_tareas):
    #         itemID = QTableWidgetItem(str(tarea.id))
    #         # itemID.setFlags(itemID.flags() & ~Qt.ItemIsEditable)
    #         self.w['tabla_tarea'].setItem(indice, 0, itemID)
    #         self.w['tabla_tarea'].setItem(
    #             indice, 1, QTableWidgetItem(tarea.nombre))
    #         self.w['tabla_tarea'].setItem(
    #             indice, 2, QTableWidgetItem(tarea.mezcla))
    #         self.w['tabla_tarea'].setItem(
    #             indice, 3, QTableWidgetItem(tarea.fecha))

