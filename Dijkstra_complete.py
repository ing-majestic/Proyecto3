#import module
import random
from graphviz import Digraph

class Graphviz():

    #constructor
    def __init__(self, name):
        self.graphvis = {}
        self.name = str(name)
        self.dot = Digraph(name,comment='The Round Graph')
    #Función que agrega nodo con etiqueta para generar el archivo GV y PNG
    def agregaNodol(self,v,et,el):
        vs = str(v)
        es = str(et)
        ex = str(el)
        self.dot.node(vs, es, xlabel= ex)
    #Función que agrega nodo sin etiqueta para generar el archivo GV y PNG
    def agregaNodo(self,v,et):
        vs = str(v)
        es = str(et)
        self.dot.node(vs, es)
    #Función que permite crear la lista en formato adecuado
    def listaedges(self,l2,a,b):
        c = str(a) + str(b)
        l2.append(c)
    #funcion que agrega arista por arista con una variable c con valor false o true
    def agregaedge(self, a, b, f):
        c = str(a)
        d = str(b)
        e = str(f)
        self.dot.edge(c , d, constraint='false', label = e)
    #Función que permite agregar la lista de conexiónes
    def agregaedges(self,l2):
        self.dot.edges(l2)
    #Función encargada de generar el archivo GV como el PNG
    def imprimegrafo(self, nodos):
        #print('-------Impresion y generacion GV de Grafo')
        self.dot.format = 'png'
        a ='Graphviz-output/'
        b = a + str(self.name)+'_'+str(nodos)+'.gv'
        self.dot.render(b, view = True)
        #print(self.dot.source) #doctest: +NORMALIZE_WHITESPACE

class Vertice:
    #Se definen los verices del grafo
    def __init__(self, i):
        self.id = i
        self.vecinos = []
        self.visitado = False
        self.padre = None
        self.distancia = float('inf')

    def agregarVecino(self, v, p):
        if v not in self.vecinos:
            self.vecinos.append([v, p])

class Grafica:

    #Clase que define los vertices de los grafos
    def __init__(self):
        self.vertices = {}


    def agregarVertice(self, id):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id)

    def agregarArista(self, a, b, p):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecino(b, p)
            self.vertices[b].agregarVecino(a, p)

    def imprimirGrafica(self):
        for v in self.vertices:
            print("La distancia del vértice "+str(v)+" es "+ str(self.vertices[v].distancia)+" llegando desde "+str(self.vertices[v].padre))

    def camino(self, N):
        k2 = Graphviz(N)
        print('Ingresa el nodo final: ')
        b = int(input())
        camino = []
        actual = b
        pes = 0
        while actual != None:
            camino.insert(0, actual)
            actual = self.vertices[actual].padre

        for i in range(0,len(camino)-1):
            k2.agregaedge(camino[i],camino[i+1],self.vertices[camino[i+1]].distancia - self.vertices[camino[i]].distancia)
            pes = pes + self.vertices[camino[i+1]].distancia
        k2.agregaNodol(str(b),str(camino[0])+' a nodo '+str(b)+": "+str(self.vertices[camino[i+1]].distancia),'')
        k2.imprimegrafo(N)
        print ("\n\nLa ruta más rápida por Dijkstra junto con su costo es:")
        return [camino, self.vertices[b].distancia]



    def minimo(self, lista):
        if len(lista) > 0:
            m = self.vertices[lista[0]].distancia
            v = lista[0]
            for e in lista:
                if m > self.vertices[e].distancia:
                    m = self.vertices[e].distancia
                    v = e
            return v

    def dijkstra(self):

        print('Ingresa el nodo inicial para Dijkstra: ')
        a = int(input())
        if a in self.vertices:
            self.vertices[a].distancia = 0
            actual = a
            noVisitados = []
            for v in self.vertices:
                if v != a:
                    self.vertices[v].distancias = float('inf')
                self.vertices[v].padre = None
                noVisitados.append(v)
            while len(noVisitados) > 0:
                for vecino in self.vertices[actual].vecinos:
                    if self.vertices[vecino[0]].visitado == False:
                        if self.vertices[actual].distancia + vecino[1] < self.vertices[vecino[0]].distancia:
                            self.vertices[vecino[0]].distancia = self.vertices[actual].distancia + vecino[1]
                            self.vertices[vecino[0]].padre = actual

                self.vertices[actual].visitado = True
                noVisitados.remove(actual)
                actual = self.minimo(noVisitados)
        else:
            return False

#clase del modelo Malla
#Función con la que se integra el GRAFO de estudio
class Malla():
    def __init__(self):
        self.id={}

    def malla(self):
        #Llamado de las clases
        g = Grafica()
        h1 = Graphviz('1_malla_pri')
        #Pide el numero de nodos que tendra el Grafo
        print ("-----GRAFO MALLA------")
        print ("Ingresa el numero de nodos: ")
        N = int(input())
        nodos = str(N)
        l = list(range(1,N+1))
        for v in l:
            g.agregarVertice(v)
            #Se agregan nodos al constructor de GV y PNG
            h1.agregaNodo(v,v)
        #Lista de aristas del Grafo
        l2 = []
        l3 = []
        #Ciclo generador de aristas en pares
        for i in l:
            random.shuffle(l)
            x = random.randint(1,len(l)/2)
            for i in range(0, x - 1, 2):
                a = l[i]
                b = l[i + 1]
                #Pesos aleatorios por arista para calculo de dikstra
                lab = random.randrange(100)
                #agregan aristas al grafo
                g.agregarArista(a, b, lab)
                #Se genera la lista para el archivo GV
                h1.agregaedge(a, b, lab)
                c=str(a)
                d=str(b)
                e='->'
                l2.insert(i, c+e+d)
                l3.insert(i, c)
                l3.insert(i+1, d)

        print('-------Grafo  Conjuntos')
        print('V = %s'%l)
        print('E = %s'%l2)
        #Se imprime encabezado de resultados
        print('-------Grafo lista de adyacentes')
        #Se construye la lista de adyacencia
        for v in g.vertices:
            print(v, g.vertices[v].vecinos)

        #Generacion y guardado de fuente archivo GV y PNG en \Graphviz-output
        h1.imprimegrafo(nodos)
        g.dijkstra()
        print(g.camino('1_ruta_malla'+nodos))
        return (l, l3)

#clase del modelo erdos and enry
class Erdosrenyi():
    #constructor
    def __init__(self):
        self.id={}

    def erdosrenyi(self):
        #Inicializa un grafo
        g = Grafica()
        h = Graphviz('2_ErdosRenyi_pri')

        l2 = []
        l3 = []
        #Pide el numero de nodos que tendra el Grafo
        print ("-----GRAFO ERDOS ENRY------")
        print ("Ingresa el numero de nodos: ")
        N = int(input())
        nodos = str(N)
        l = list(range(1,N+1))
        for v in l:
            g.agregarVertice(v)
            #Se agregan nodos al constructor de GV y PNG
            h.agregaNodo(v,v)
        #Pide el rango d eprobabilidad P
        #print("Ingresa el valor de probabilidad de cada nodo: ")
        P = float(1)
        #l representa los nodos que tomara en cuenta el grafo, P representa el numero flotante de probabilidad entre 0.1 y 1.0
        for i in l:
            x = random.randint(1,len(l))
            for j in range(0, x - 1, 2):
                if i < j:
                    #tomando un numero random R
                    R = random.random()
                    #Verificar si R < P
                    if (R < P):
                        #Pesos aleatorios por arista para calculo de dikstra
                        lab = random.randrange(100)
                        # Agrega las aristas para el grafo
                        g.agregarArista(i, j, lab)
                        #Se genera la lista para el archivo GV
                        h.agregaedge(i, j, lab)
                        c=str(i)
                        d=str(j)
                        e = '->'
                        l2.insert(i, c+e+d)
                        l3.insert(i, c)
                        l3.insert(i+1, d)
        #agrega la lista de vetices
        print('-------Grafo  Conjuntos')
        print('V = %s'%l)
        print('E = %s'%l2)
        #Se imprime encabezado de resultados
        print('-------Grafo lista de adyacentes')
        #Se construye la lista de adyacencia
        for v in g.vertices:
            print(v, g.vertices[v].vecinos)
        #Menu para seleccionar el tipo d ecalculo a realizar en al Grafo
        g.dijkstra()
        print(g.camino('2_ruta_erdosrenyi'+nodos))
        h.imprimegrafo(nodos)
        return(l, l3)

class Gilbert():
    #constructor
    def __init__(self):
        self.id={}

    def gilbert(self):
        #Inicializa un grafo
        g3 = Grafica()
        h3 = Graphviz('3_Gilbert_pri')

        l2 = []
        l3 = []
        #Pide el numero de nodos que tendra el Grafo
        print ("-----GRAFO GILBERT------")
        print ("Ingresa el numero de nodos: ")
        N = int(input())
        nodos = str(N)
        l = list(range(1,N+1))

        for v in l:
            g3.agregarVertice(v)
            #Se agregan nodos al constructor de GV y PNG
            h3.agregaNodo(v,v)

        #Pide el rango d eprobabilidad P
        print("Ingresa el valor de probabilidad de cada nodo: ")
        P = float(input())
        #l representa los nodos que tomara en cuenta el grafo, P representa el numero flotante de probabilidad entre 0.1 y 1.0
        for i in l:
            x = random.randint(1,len(l))
            for j in range(0, x - 1, 2):
                if i < j:
                    #tomando un numero random R
                    R = random.random()
                    if (R < P):
                        #Pesos aleatorios por arista para calculo de dikstra
                        lab = random.randrange(100)
                        # Agrega las aristas para el grafo
                        g3.agregarArista(i, j, lab)
                        #Se genera la lista para el archivo GV
                        h3.agregaedge(i, j, lab)
                        c=str(i)
                        d=str(j)
                        e = '->'
                        l2.insert(i, c+e+d)
                        l3.insert(i, c)
                        l3.insert(i+1, d)
        #agrega la lista de vetices
        print('-------Grafo  Conjuntos')
        print('V = %s'%l)
        print('E = %s'%l2)
        #Se imprime encabezado de resultados
        print('-------Grafo lista de adyacentes')
        #Se construye la lista de adyacencia
        for v in g3.vertices:
            print(v, g3.vertices[v].vecinos)
        #Menu para seleccionar el tipo d ecalculo a realizar en al Grafo

        #Generacion y guardado de fuente archivo GV y PNG en \Graphviz-output
        g3.dijkstra()
        print(g3.camino('3_ruta_gilbert'+nodos))
        h3.imprimegrafo(nodos)
        return(l, l3)



def main():
    a = Malla()
    b = Erdosrenyi()
    c = Gilbert()
    #a.malla()
    #b.erdosrenyi()
    c.gilbert()


main()
