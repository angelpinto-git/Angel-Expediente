from typing import Optional
from termcolor import colored
from models.expediente_model import Expediente
import utils.console_handler as console


class ExpedienteController:
    @classmethod
    def start(cls) -> None:
     Expediente.load()
     console.clear()
     while True:
            print("\nMenú CRUD de Expedientes")
            print("1. Crear Expediente")
            print("2. Leer Expedientes")
            print("3. Actualizar Expediente")
            print("4. Eliminar Expediente")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                cls.add()
            elif opcion == '2':
                cls.list_all()
            elif opcion == '3':
                cls.update()
            elif opcion == '4':
                cls.delete()
            elif opcion == '5':
                Expediente.save()
                print("Datos guardados. Saliendo...")
                break
            else:
                print(colored("Opción inválida.", "red"))

    @classmethod
    def add(cls) -> None:
        console.clear()
        try:
            num_expediente = int(input("Número de expediente: "))
            caratula = input("Nombre de carátula: ")
            juzgado = input("Juzgado: ")
            demandante = input("Demandante: ")
            demandado = input("Demandado: ")
            telefono = input("Teléfono: ")
            new_record = Expediente(num_expediente, caratula, juzgado, demandante, demandado, telefono)
            Expediente.all.append(new_record)
            Expediente.save()
            print(colored("Expediente creado con éxito.", "green"))
        except ValueError as e:
            print(colored(f"Error al crear el Expediente: {e}", "red"))

    @classmethod
    def list_all(cls) -> None:
        console.clear()
        if not Expediente.all:
            print(colored("No hay Expedientes registrados.", "red"))
        for expediente in Expediente.all:
            print (expediente)

    @classmethod
    def update(cls) -> None:
        cls.list_all()
        try:
            num_expediente = int(
                input("Ingrese el número del Expediente a actualizar: "))
            expediente = cls.load_user(num_expediente)
            if expediente:
             expediente.caratula = input("Nueva carátula: ")
             expediente.juzgado = input("Ingrese Juzgado: ")
             expediente.demandante = input("Ingrese demandante: ")
             expediente.demandado = input("Ingrese demandado: ")
             expediente.telefono = input("Nuevo Teléfono: ")
             print(colored("Expediente actualizado.", "green"))
            else:
                print(colored("Expediente no encontrado.", "red"))
        except ValueError as e:
            print(colored(f"Error: {e}", "red"))

    @classmethod
    def delete(cls) -> None:
        try:
            num_expediente = int(
                input("Ingrese el número del Expediente a eliminar: "))
            expediente = cls.load_user(num_expediente)
            if expediente:
                Expediente.all.remove(expediente)
                print(colored("Expediente eliminado.", "green"))
            else:
                print(colored("Expediente no encontrado.", "red"))
        except ValueError as e:
            print(colored(f"Error: {e}", "red"))

    @classmethod
    def load_record(cls, num_expediente: int) -> Optional[Expediente]:
        for expediente in Expediente.all:
            if expediente.num_expediente == num_expediente:
                return expediente
        return None