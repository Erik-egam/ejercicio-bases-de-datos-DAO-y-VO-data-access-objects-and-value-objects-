import db.conexion as cdb


def insert_trabajador(nuevo_trabajador: tuple) -> int:
    with cdb.crear_conexion() as conector:
        print(nuevo_trabajador)
        sql = f"""INSERT INTO Trabajadores (
            nombre, telefono,
            EPS, ARL
            ) VALUES (
            ?, '1234567890',
            'Sanitas', 'Positiva'
            )"""
        cursor = conector.cursor()
        cursor.execute(sql,
                       [nuevo_trabajador]
                       )
        conector.commit()
        return cursor.lastrowid
            
def update_trabajador(cambios:dict):
    with cdb.crear_conexion() as conector:
        print(cambios)
        sql = """
        UPDATE Trabajadores SET
        """
        
        
        # WHERE id_trab = ?
        
        # Nombre
        if cambios["nombre"]:
            sql += f"nombre = '{cambios["nombre"]}',"
        if cambios["telefono"]:
            sql += f"telefono = '{cambios["telefono"]}',"
        if cambios["eps"]:
            sql += f"EPS = '{cambios["eps"]}',"
        if cambios["arl"]:
            sql += f"ARL = '{cambios["arl"]}',"
                    
        sql = sql[:-1]
        # print(sql)
        sql += f"WHERE id_trab = {cambios["id"]}"
        cursor = conector.cursor()
        cursor.execute(sql)
        conector.commit()
        return cursor.lastrowid
    
def insert_arbol(nuevo_arbol: tuple) -> int:
    with cdb.crear_conexion() as conector:
        print(nuevo_arbol)
        sql = f"""INSERT INTO Arboles (
            terreno,fecha_siembra
            ) VALUES (
            ?, '2006-01-01'
            )"""
        cursor = conector.cursor()
        cursor.execute(sql,
                       [nuevo_arbol]
                       )
        conector.commit()
        return cursor.lastrowid
            
def update_arbol(cambios:dict):
    with cdb.crear_conexion() as conector:
        print(cambios)
        sql = f"""
        UPDATE Arboles SET terreno = '{cambios['terreno']}' 
        """
        
        
        # WHERE id_trab = ?
                    
        sql = sql[:-1]
        # print(sql)
        sql += f"WHERE id_arbol = {cambios["id"]}"
        cursor = conector.cursor()
        cursor.execute(sql)
        conector.commit()
        return cursor.lastrowid
    
    
def insert_enfermedad(nueva_enfermedad: tuple) -> int:
    with cdb.crear_conexion() as conector:
        print(nueva_enfermedad)
        sql = f"""INSERT INTO Arboles_Enfermedades (
            id_arbol,id_enfermedad, fecha_enfermedad
            ) VALUES (
                """
        sql += f"{nueva_enfermedad[0]},"
        sql += f"1,"
        sql += f"'{nueva_enfermedad[1]}')"
        cursor = conector.cursor()
        cursor.execute(sql)
        conector.commit()
        return cursor.lastrowid

def insert_tarea(nueva_tarea: tuple) -> int:
    with cdb.crear_conexion() as conector:
        print(nueva_tarea)
        sql = f"""INSERT INTO Tareas (
            id_arbol,id_tipo_tarea, fecha_tarea, mezcla
            ) VALUES (
                """
        sql += f"{nueva_tarea[0]},"
        sql += f"2,"
        sql += f"'{nueva_tarea[1]}',"
        sql += f"'{nueva_tarea[2]}')"
        cursor = conector.cursor()
        cursor.execute(sql)
        conector.commit()
        return cursor.lastrowid
    
    
    
    
def update_enfermedad(cambios:dict):
    with cdb.crear_conexion() as conector:
        print(cambios)
        sql = """
        UPDATE Arboles_Enfermedades SET
        """

        sql += f"fecha_enfermedad = '{cambios['fecha']}' "
        
        sql += f"WHERE Arboles_Enfermedades.id_arbol = {cambios["id_arbol"]} AND Arboles_Enfermedades.id_enfermedad = {cambios['id_enfermedad']};"
        cursor = conector.cursor()
        cursor.execute(sql)
        conector.commit()
        return cursor.lastrowid
