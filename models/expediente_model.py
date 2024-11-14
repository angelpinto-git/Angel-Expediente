from models.base_model import Base


class Expediente(Base):
    filename = 'expedientes.json'

    def __init__(self, num_expediente, caratula, juzgado,demandante, demandado, telefono) -> None:
        self.num_expediente = num_expediente
        self.caratula = caratula
        self.juzgado = juzgado
        self.demandante = demandante
        self.demandado = demandado
        self.telefono =  telefono
                
    def __str__(self) -> str:
        return (
            f"Num_expediente: {self.num_expediente}, Carátula: {self.caratula}, Juzgado: {self.juzgado}, "
            f"Demandante: {self.demandante}, Demandado: {self.demandado}, Teléfono: {self.telefono}"
        )