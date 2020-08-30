import copy
class Automata():    
    lista=[]
    producciones=[]
    
    def __init__(self, producciones):
        self.producciones=producciones
    
    def crearPunto(self, gramatica):
        gramatica_Aux=gramatica.copy()
        for i in range (len(gramatica_Aux)):
            for i2 in range(len(gramatica_Aux[i])):
                if gramatica_Aux[i][i2] != ".":
                    if gramatica_Aux[i][i2] == "-":
                        gramatica_Aux[i].insert(i2+1,".")
        self.lista.append(gramatica_Aux)
    
    def obtenerArista(self, gramatica):
        aux_Gramatica=copy.deepcopy(gramatica)
        for i in range (len(aux_Gramatica)):
            for i2 in range(len(aux_Gramatica[i])):
                if i2 + 1  < len(aux_Gramatica[i]):
                    if aux_Gramatica[i][i2] == "." and aux_Gramatica[i][i2+1] != None:
                        return aux_Gramatica[i][i2+1]
            # print(aux_Gramatica[i])        
        
        return -1
    
    #Metodo listo
    def quitarPunto(self, gramatica, arista):
        aux_Gramatica=copy.deepcopy(gramatica)
        
        for i in range (len(aux_Gramatica)):
            for i2 in range(len(aux_Gramatica[i])):
                if i2 + 1  < len(aux_Gramatica[i]):
                    if aux_Gramatica[i][i2] == "." and aux_Gramatica[i][i2+1] == arista:
                        aux_Gramatica[i].pop(i2)
        return aux_Gramatica.copy()
    
    #metodo listo
    def limpiarGramatica(self, gramatica, arista):
        aux = copy.deepcopy(gramatica)
        encontro=False
        i=0
        while i < len(aux):
            for i2 in range(len(aux[i])):
                if aux[i][i2] == ".":
                    encontro=True
                ###############organizarl el punto#####################
            if encontro == True:
                aux.pop(i)
                i=i-1
                encontro=False
            i=i+1
        return aux
    
    def crearEstado(self, gramatica2):
        #si arista es -1 es porque ya acabo de ir a los estados
        gramatica = copy.deepcopy(gramatica2)
        # copy.deepcopy()
        
        for i in range(len(producciones)):
            aux_Gramatica=copy.deepcopy(gramatica)
            # arista=self.obtenerArista(aux_Gramatica)
            arista = producciones[i]
            lista_Aux=self.quitarPunto(copy.deepcopy(aux_Gramatica), arista)
            nuevaGramatica=self.verificarSiguiente(copy.deepcopy(lista_Aux), arista)
            if len(nuevaGramatica) > 0 :
                self.lista.append([arista])
                self.lista.append(copy.deepcopy(nuevaGramatica))
                
        
    def ponerPunto(self, lista2, arista):
        l=copy.deepcopy(lista2)
        for i in range (len(l)):
            for i2 in range(2,len(l[i])):
                if l[i][i2] != ".":
                    if l[i][i2] == arista:
                        l[i].insert(i2+1,".")
        return l 
    
    def verificarSiguiente(self, lista, arista):
        lista_Aux= copy.deepcopy(lista)
        aux=self.limpiarGramatica(lista_Aux, arista).copy()
        aux=self.ponerPunto(aux, arista)
        for i in range(len(aux)):
            for i2 in range(2, len(aux[i])):
                if (i2 + 1  < len(aux[i])):
                    for i3 in range (len(self.producciones)):
                        if (aux[i][i2] == "." and aux[i][i2 + 1] == self.producciones[i3]):
                            self.devolver_Produccion(self.producciones[i3], aux)
                           
                    
        return aux
    
    #Devuelve la produccion despues del punto
    def devolver_Produccion(self, arista, aux):
        li=[]
        pri_Gramatica=[]
        pri_Gramatica = copy.deepcopy(self.lista[0])
        for i in range(len(pri_Gramatica)):
            if (arista == pri_Gramatica[i][0]):
                aux.append(pri_Gramatica[i])
                li.append(arista)
        
        for i in range(len(aux)):
            for i2 in range(len(aux[i])):
                for i3 in range(len(li)):
                    if ((i2 + 1) < (len(aux[i]))):
                        if(aux[i][i2] == "."):
                            if aux[i][i2+1] != li[i3]:
                                self.prueba(aux[i][i2+1], aux, li)
                                break
                                
        
        
    def prueba(self, letra, aux, li):
        pri_Gramatica=[]
        pri_Gramatica = copy.deepcopy(self.lista[0])
        
        for i in range(2,len(pri_Gramatica)):
            if (letra == pri_Gramatica[i][0]):
                aux.append(pri_Gramatica[i])
                
                
    def mostar_Gramatica(self, gramatica):
        for i in range(len(gramatica)):
            print(gramatica[i])
            
    def mostrar_Grafo(self):
        for estado in range(len(self.lista)):
            if self.lista[estado] != None:
                self.mostar_Gramatica(self.lista[estado])
                print(".------------------",estado,"-----------.-------------------")
 

class Estado():
    def __init__(self, ide, estado_Inicial, lista):
        self.ide=ide
        self.nodo_Inicial=estado_Inicial
        self.lista=lista
    
    def crear_Estado(lista):
        print("listas")
        return None
        
        
#####################################
producciones=["S","E","T","F","+","*","id","(",")"]

lista0=["S","-","E"]
lista1=["E","-","E","+","T"]
lista2=["E","-","T"]
lista3=["T","-","T","*","F"]
lista4=["T","-","F"]
lista5=["F","-","id"]
lista6=["F","-","(","E",")"]

gramatica=[]
gramatica.append(lista0)
gramatica.append(lista1)
gramatica.append(lista2)
gramatica.append(lista3)
gramatica.append(lista4)
gramatica.append(lista5)
gramatica.append(lista6)

a = Automata(producciones)
e = a.crearPunto(gramatica)
a.crearEstado(a.lista[0].copy())
a.crearEstado(a.lista[2].copy())
a.crearEstado(a.lista[4].copy())
a.crearEstado(a.lista[10].copy())
# a.crearEstado(a.lista[8].copy())
# a.crearEstado(a.lista[5].copy())
# a.crearEstado(a.lista[6].copy())

a.mostrar_Grafo()

# print(a.lista[1])

