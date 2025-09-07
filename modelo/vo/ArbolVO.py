from dataclasses import dataclass
from  modelo.vo.EnfermedadVO import EnfermedadVO
@dataclass
class ArbolVO:
    id_arbol : int
    fecha_siembra : str
    terreno : str