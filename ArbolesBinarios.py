#Clase NodoArbol representa un nodo individual en el Árbol. 
#Cada nodo tiene un dato, un puntero a su hijo izquierdo y un puntero a su hijo derecho.

class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None


#Clase ArbolBinario representa el árbol en sí. 
#Tiene un atributo llamado "raiz" que es el nodo principal del Árbol.

class ArbolBinario: 
    def __init__(self):
        self.raiz =  None


#Función insertar que permite agregar un nuevo número al Árbol. 

    def insertar (self, dato):
        if self.raiz is None:
            self.raiz = NodoArbol(dato)
        else:
            self._insertar_recursivo(self.raiz, dato)

#Si el árbol está vacío, crea un nuevo nodo con el dato proporcionado y lo establece como la raíz, en el caso opuesto; llama a la función privada _insertar_recursivo.

    def _insertar_recursivo(self, nodo, nuevo_dato):
        if nuevo_dato == nodo.dato:
            print(f"El número {nuevo_dato} ya exíste en el Árbol.")
            return  #Si el número ya existe en el Árbol, no lo inserta

        if nuevo_dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(nuevo_dato)
            else:
                self._insertar_recursivo(nodo.izquierda, nuevo_dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(nuevo_dato)
            else:
                self._insertar_recursivo(nodo.derecha, nuevo_dato)


#Esta función de mostrar_arbol imprime el Árbol en la consola y llama a la función privada _mostrar_arbol_recursivo.

    def mostrar_arbol(self):
        self._mostrar_arbol_recursivo(self.raiz,0)
    def _mostrar_arbol_recursivo(self, nodo, nivel):
        if nodo is not None:
            self._mostrar_arbol_recursivo(nodo.derecha, nivel +1)
            print ("    "*nivel + str(nodo.dato))
            self._mostrar_arbol_recursivo(nodo.izquierda, nivel +1)


#Aquí la función de buscar hace la busqueda de un dato en el Árbol y devuelve el nodo que contiene ese dato.

    def buscar (self, dato):
        return self._buscar_recursivo(self.raiz, dato)
    def _buscar_recursivo(self, nodo, dato):
        if nodo is None or nodo.dato == dato:
            return nodo
        if dato < nodo.dato:
            return self._buscar_recursivo(nodo.izquierda, dato)
        return self._buscar_recursivo(nodo.derecha, dato)


#Esta función elimina un dato del Árbol.

    def eliminar (self, dato):
        self.raiz = self._eliminar_recursivo(self.raiz, dato)
    def _eliminar_recursivo(self, nodo, dato):
        if nodo is None:
            return nodo
        if dato < nodo.dato:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, dato)
        elif dato > nodo.dato:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, dato)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            nodo.dato = self._encontrar_minimo(nodo.derecha)
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, nodo.dato)
        return nodo

    def _encontar_minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual.dato


#Función de recorrer en PreOrden devuelve una lista con los datos del Árbol en recorrido PreOrden.

    def recorrer_preOrden(self):
        resultado = []
        self.preOrden(self.raiz, resultado)
        return resultado
    def preOrden(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.dato)
            self.preOrden(nodo.izquierda, resultado)
            self.preOrden(nodo.derecha, resultado)


#Función de recorrer en InOrden devuelve una lista con los datos del Árbol en recorrido InOrden.

    def recorrer_inOrden(self):
        resultado = []
        self.inOrden(self.raiz, resultado)
        return resultado
    def inOrden(self, nodo, resultado):
        if nodo is not None:
            self.inOrden(nodo.izquierda, resultado)
            resultado.append(nodo.dato)
            self.inOrden(nodo.derecha, resultado)


#Función de recorrer en PostOrden devuelve una lista con los datos del Árbol en recorrido PostOrden.

    def recorrer_postOrden(self):
        resultado = []
        self.postOrden(self.raiz, resultado)
        return resultado
    def postOrden(self, nodo, resultado):
        if nodo is not None:
            self.postOrden(nodo.izquierda, resultado)
            self.postOrden(nodo.derecha, resultado)
            resultado.append(nodo.dato)



#Código para probar la implementación del Árbol:

#Llamando a que se ejecute la clase
arbol = ArbolBinario()

#Insertar Elementos Predeterminadamente
elemento_para_insertar = [8, 3, 1, 10, 14, 6, 7, 4, 13]
for elemento in elemento_para_insertar:
    arbol.insertar(elemento)

#Mostrar Arbol Completo
arbol.mostrar_arbol()

#Insertar elementos en la consola
while True:
    #Preguntar al usuario si desea ingresar números
    respuesta = input("¿Desea ingresar números al Árbol? (si/no): ").lower()

    if respuesta != 'si':
        break  #Salir del bucle si la respuesta no es "si"

    #Solicitar la cadena de números al usuario y convertirla a una lista
    numeros_ingresar = input("Ingrese el (los) números que desea poner en el Árbol seguidos de un espacío: ")
    numeros_ingresar = [int(num) for num in numeros_ingresar.split()]

    #Insertar cada número en el Árbol
    for numero_ingresar in numeros_ingresar:
        arbol.insertar(numero_ingresar)

#Mostrar el Árbol después de la inserción
arbol.mostrar_arbol()


#Buscar Elemento
dato_buscar = int (input("¿Qué número quieres buscar? "))
nodo_encontrado = arbol.buscar(dato_buscar)
if nodo_encontrado:
    print(f"El número {dato_buscar} fue encontrado en el Árbol.")
else:
    print(f"El número {dato_buscar} no fue encontrado en el Árbol")


#Eliminar Elemento
dato_eliminar = int(input("¿Ingresa el número que quieres eliminar?: "))
nodo_encontrado = arbol.buscar(dato_eliminar)

if nodo_encontrado:
    arbol.eliminar(dato_eliminar)
    print(f"Se eliminó el número {dato_eliminar} correctamente del Árbol")
else:
    print(f"El el número {dato_eliminar} no existe en el Árbol")

#Muestra el Árbol despues de la eliminación
arbol.mostrar_arbol()


#RECORRIDOS

#El rrecorrido en PreOrden
print("El rrecorrido en PreOrden es: ", arbol.recorrer_preOrden())

#El rrecorido el InOrden
print("El rrecorido en InOrden es: ", arbol.recorrer_inOrden())

# El recorrido en PostOrden
print("El recorrido en PostOrden es: ", arbol.recorrer_postOrden())