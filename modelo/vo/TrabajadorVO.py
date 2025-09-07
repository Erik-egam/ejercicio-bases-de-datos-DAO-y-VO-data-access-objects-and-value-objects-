from dataclasses import dataclass

@dataclass
class TrabajadorVO:
    id_trab : int
    nombre : str
    telefono : str
    EPS : str
    ARL : str