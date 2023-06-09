class Node:
    
    
    def __init__(self, valor) -> None:
        self.value = valor
        self.next = None
    
    
class LinkedList:
    
    
    def __init__(self, valor = None) -> None:
        
        if valor != None:
            
            new_node = Node(valor)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        
        else:
            
            nodo_vacio = Node("")
            self.head = nodo_vacio
            self.tail = nodo_vacio
            self.length = 0
            
    
    def __repr__(self) -> str:
            
        lista = "["
        obj = self.head
        
        while obj.next:
            
            lista += "{} -> ".format(str(obj.value))
            obj = obj.next
            
        lista += "{}]".format(str(obj.value))
        
        return lista
    
        
    def append(self, valor):
        
        new_node = Node(valor)
        
        if self.length == 0:
            
            self.head = new_node
            self.tail = new_node
            self.length = 1
            
        else:
            
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            
        
    def pop(self):
        
        return_node = self.tail
        
        if self.length == 1:
            nodo_vacio = Node("")
            self.head = nodo_vacio
            self.tail = nodo_vacio
            self.length = 0
        
        elif self.length == 0:
            pass
        
        else:
            cont = 1
            nodo = self.head
            
            while cont < self.length -1:
                nodo = nodo.next
                cont += 1
                
            self.tail = nodo
            self.tail.next = None
            self.length -= 1
            
        return return_node.value
    
    
    
    def popFirst(self):
        
        return_node = self.head
        
        if self.length == 1:
            nodo_vacio = Node("")
            self.head = nodo_vacio
            self.tail = nodo_vacio
            self.length = 0
            
        else:
            
            self.head = self.head.next
            self.length -= 1
        
        return return_node.value
    
    def remove(self, valor):
        
        obj_remove = self.head
        obj_ant = None
        obj_post = None
        
        while obj_remove.value != valor:
            
            obj_ant = obj_remove
            obj_remove = obj_remove.next
        
        if obj_remove == self.head:
            
            self.popFirst()
            
        elif obj_remove == self.tail:
            
            self.pop()
            
        else:
            
            obj_post = obj_remove.next
            obj_ant.next = obj_post
    
    
    def prepend(self, valor):
        
        new_node = Node(valor)
        
        if self.length == 0:
            
            self.head = new_node
            self.tail = new_node
            self.length = 1
            
        else:
            
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            
    
    def get(self, index):
        
        if index > self.length-1 or index < 0:
            
            print("Indice invalido")
            return
        
        else:
            
            nodo_actual = self.head
            
            for i in range(0, index):
                nodo_actual = nodo_actual.next
            
            return(nodo_actual)
        
        
    def insert(self, index, valor):
        
        if index > self.length or index < 0:
            
            print("Indice invalido")
            return
        
        elif index == 0:
            self.prepend(valor)
        
        elif index == self.length:
            self.append(valor)

        else:
            
            nuevo_nodo = Node(valor)
            nodo_anterior = self.get(index-1)
            nodo_indicado = nodo_anterior.next
            nodo_anterior.next = nuevo_nodo
            nuevo_nodo.next = nodo_indicado
            self.length += 1
            
        
    def set(self, index, valor):
        
        nodo_modif = self.get(index)
        nodo_modif.value = valor
        
        
    def removeByIndex(self, index):
        
        if index < 0 or index > self.length-1:
            
            print("Indice invalido.")
            return
        
        elif index == 0:
            self.popFirst()
            
        elif index == self.length-1:
            self.pop()
            
        else:
        
            nodo_ant = self.get(index-1)
            nodo_elim = nodo_ant.next
            nodo_post = nodo_elim.next 
            nodo_ant.next = nodo_post
            self.length -= 1
            
            
class Registro:
    
    def __init__(self) -> None:
        
        self.perros = LinkedList()
        self.gatos = LinkedList()
        
        
    def agregarPerro(self, objPerro):
        
        self.perros.append(objPerro)
        
    
    def agregarGato(self, objGato):
        
        self.gatos.append(objGato)
        
        
    def getPerro(self):
        
        if self.perros.length > 0:
                    
            return self.perros.popFirst()
        
        else:
            
            print("Ya no quedan perros en el registro.")
            return None
    
    
    def getGato(self):
        
        if self.gatos.length > 0:
            
            return self.gatos.popFirst()
        
        else:
            
            print("Ya no quedan gatos en el registro.")
            return None
    
    
    def getAnimal(self):
        
        
        
        if self.perros.length > 0 and self.gatos.length > 0:
            
            perro = self.perros.get(0).value
            gato = self.gatos.get(0).value
            
            if perro.date > gato.date:
                
                return self.gatos.popFirst(), "gato"
            
            elif perro.date < gato.date:
                
                return self.perros.popFirst(), "perro"
            
        elif self.perros.length > 0 and self.gatos.length == 0:
            
            print("Ya no quedan gatos en el registro")
            return self.perros.popFirst(), "perro"
        
        elif self.perros.length == 0 and self.gatos.length > 0:
            
            print("Ya no quedan perros en el registro")
            return self.gatos.popFirst(), "gato"
        
        elif self.perros.length == 0 and self.gatos.length == 0:
            
            print("No quedan animales en el registro.")
            return None, ""
    
            

class Animal:
    
    def __init__(self, nombre, edad, fecha) -> None:
        self.nombre = nombre
        self.edad = edad
        self.date = fecha