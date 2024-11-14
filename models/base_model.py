from utils.file_handler import write_json_file, read_json_file


class Base:
     all: list = []
     filename = ''

     @classmethod
     def save(cls) -> None:
         """Guarda todos los objetos de la clase en el archivo JSON."""
         write_json_file(
             cls.filename, [expediente.__dict__ for expediente in cls.all])

     @classmethod
     def load(cls) -> None:
        """Carga todos los objetos de la clase desde el archivo JSON."""
        for expediente_dict in read_json_file(cls.filename):
            # Utilizamos los valores del diccionario para crear una instancia
            expediente_obj = cls(**expediente_dict)
            cls.all.append(expediente_obj)
    