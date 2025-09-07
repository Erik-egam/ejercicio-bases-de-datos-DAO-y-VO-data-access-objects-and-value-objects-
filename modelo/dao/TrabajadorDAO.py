from __future__ import annotations
from modelo.vo.TrabajadorVO import TrabajadorVO
from db.conexion import crear_conexion, ubicacionBD


# Ya modifique lo que le dije
# Ya todo el codigo lo puede revisar y si quiere lo comenta para que vaya mirando que entiende y que no
# me avisa cualquier cosa si ya entiende todo es solo ctrl + C  y ctrl + V
# El cuarto lo hacemos juntos


class TrabajadorDAO:
    def __init__(self):
        self.conector = crear_conexion(rutaBD=ubicacionBD)

    def get_all(self):
        sql = "SELECT * FROM Trabajadores;"
        cursor = self.conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        Trabajadores = list()
        for registro in registros:

            Trabajadores.append(
                TrabajadorVO(
                    id_trab=registro[0],
                    nombre=registro[1],
                    telefono=registro[2],
                    EPS=registro[3],
                    ARL=registro[4]
                )
            )

        # print(registros[0:5])

        return Trabajadores

    def get_Trabajador_by_id(self, Trabajador: TrabajadorVO) -> TrabajadorVO:
        sql = f"select * from Trabajadores WHERE id_trab = {Trabajador.id}"
        cursor = self.conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        Trabajador = list()
        for registro in registros:
            Trabajador.append(
                TrabajadorVO(
                    id_trab=registro[0],
                    nombre=registro[1],
                    telefono=registro[2],
                    EPS=registro[3],
                    ARL=registro[4]
                )
            )

        return Trabajador[0]
