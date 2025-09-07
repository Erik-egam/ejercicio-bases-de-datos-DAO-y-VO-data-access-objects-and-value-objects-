from dataclasses import dataclass

@dataclass
class EnfermedadVO:
    id_enfermedad: int
    nombre: str
    causa: str
    fecha_enfermedad: str