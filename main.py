from Clases import Registro, Animal
from datetime import datetime


        
def main():
    
    registro = Registro()
    opc = 0
    
    while opc != 6:
        
        print("""
              Menú:
              1. Agregar perro
              2. Agregar gato
              3. Obtener perro
              4. Obtener gato
              5. Obtener animal
              6. Salir""")
        opc = int(input("Ingrese una opción: "))
        
        match(opc):
            
            case 1:
                
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                date = datetime.now()
                perro = Animal(nombre, edad, date)
                registro.agregarPerro(perro)
                print("Perro agregado.")
                
            case 2:
                
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                date = datetime.now()
                gato = Animal(nombre, edad, date)
                registro.agregarGato(gato)
                print("Gato agregado.")
                
            case 3:
                
                perro = registro.getPerro()
                if perro is not None:
                    
                    print("Perro obtenido: ")
                    print(f"Nombre: {perro.nombre}, Edad: {perro.edad}, Fecha de llegada: {perro.date}")
                
                else:
                    pass
                
            case 4:
                
                gato = registro.getGato()
                if gato is not None:
                    
                    print("Gato obtenido: ")
                    print(f"Nombre: {gato.nombre}, Edad: {gato.edad}, Fecha de llegada: {gato.date}")

                else:
                    pass
                
                                
            case 5:
                
                animal, tipo = registro.getAnimal()
                
                if animal == None:
                    
                    pass
                
                if tipo == "gato":
                    print("Animal obtenido: gato")
                    
                else:
                    print("Animal obtenido: perro")
                    
                print(f"Nombre: {animal.nombre}, Edad: {animal.edad}, Fecha de llegada: {animal.date}")
                
    print("Saliendo...")
    
main()