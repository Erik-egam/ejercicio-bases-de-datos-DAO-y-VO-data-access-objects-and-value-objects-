import db.conexion as cbd
# import time

def tablas_completas(nombre_tabla)->list: 
    with cbd.crear_conexion() as conector:        
        sql = f"SELECT * FROM {nombre_tabla};"        
        cursor = conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        print(registros)
        
        return registros    

        
        