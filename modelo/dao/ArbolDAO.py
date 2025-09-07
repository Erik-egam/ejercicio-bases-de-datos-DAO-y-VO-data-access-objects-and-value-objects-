from __future__ import annotations
from modelo.vo.EnfermedadVO import EnfermedadVO
from modelo.vo.ArbolVO import ArbolVO
from db.conexion import crear_conexion, ubicacionBD
from modelo.vo.TareaVO import TareaVO

# Ya modifique lo que le dije
# Ya todo el codigo lo puede revisar y si quiere lo comenta para que vaya mirando que entiende y que no
# me avisa cualquier cosa si ya entiende todo es solo ctrl + C  y ctrl + V
# El cuarto lo hacemos juntos


class ArbolDAO:
    def __init__(self):
        self.conector = crear_conexion(rutaBD=ubicacionBD)

    def get_all(self):
        sql = """
        SELECT * FROM Arboles;
        """
        cursor = self.conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        Arboles = list()
        for registro in registros:
            Arboles.append(
                ArbolVO(
                    id_arbol=registro[0],
                    fecha_siembra=registro[1],
                    terreno=registro[2]
                )
                
            )

        # print(registros[0:5])

        return Arboles


    def get_enfermedad_by_arbol_id(self, arbol:int) -> list:
        sql = f"select * from Arboles_Enfermedades join Enfermedades on Arboles_Enfermedades.id_enfermedad = Enfermedades.id_enfermedad where Arboles_Enfermedades.id_arbol = {arbol};"
        cursor = self.conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        enfermedades = list()
        for registro in registros:
            enfermedades.append(
                EnfermedadVO(
                    id_enfermedad=registro[1],
                    nombre=registro[4],
                    causa=registro[-1],
                    fecha_enfermedad=registro[2]
                )
            )

        return enfermedades

    def get_tarea_by_arbol_id(self, arbol:int) -> list:
            sql = f"select * from Arboles join Tareas on Tareas.id_arbol = Arboles.id_arbol join Tipo_tarea on Tipo_tarea.id_tipo_tarea = Tareas.id_tipo_tarea where Arboles.id_arbol = {arbol};"
            cursor = self.conector.cursor()
            cursor.execute(sql)
            registros = cursor.fetchall()
            tareas = list()
            for registro in registros:
                tareas.append(
                    TareaVO(
                        id=registro[3],
                        nombre=registro[-1],
                        mezcla=registro[-5],
                        fecha = registro[-4]
                    )
                )
    
            return tareas
    
