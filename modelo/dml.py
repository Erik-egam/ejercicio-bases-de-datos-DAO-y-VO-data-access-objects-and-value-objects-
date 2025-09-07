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