


# generar_trabajadores.py --> es un Script para crear un archivo con insert para trabajadores completamente con datos
# aleatorios de las siguientes listas
eps_list = ["Sura", "Sanitas", "Compensar", "Nueva EPS"]
arl_list = ["Colpatria", "Positiva", "Colmena", "Bolívar"]

with open("trabajadores.sql", "w", encoding="utf-8") as f:
    f.write("INSERT INTO Trabajadores (id_trab, nombre, telefono, EPS, ARL) VALUES\n")
    values = []
    for i in range(7, 1007):
        nombre = f"Trabajador_{i}"
        telefono = f"3{str(100000000 + i)[1:]}"  # teléfonos simulados
        eps = eps_list[i % len(eps_list)]
        arl = arl_list[i % len(arl_list)]
        values.append(f"({i}, '{nombre}', '{telefono}', '{eps}', '{arl}')")
    f.write(",\n".join(values) + ";\n")
