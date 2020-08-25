#VISTA
# from tkinter import *
# raiz=Tk()
# raiz.title("Bienvenidos. ")
# raiz.resizable(1,1)
# raiz.iconbitmap("../imagenes/icono.ico")
# raiz.geometry("700x550")
# raiz.config(bg="blue")
# raiz.config(bd=20)
# frame=Frame(raiz, width="900", height="650", bg="red")
# frame.pack()
# miLabel=Label(frame, text="ingrese la gramatica").place(x=10,y=20)
# #miImagen = PhotoImage(file="RUTA")
# #Label(frame, miImagen).place(x=10,y=20)
# raiz.mainloop()
#####################################
class Automata():    
    #metodo listo
    def crearPunto(self, gramatica):
        for i in range (len(gramatica)):
            for i2 in range(len(gramatica[i])):
                if gramatica[i][i2] != ".":
                    if gramatica[i][i2] == "-":
                        gramatica[i].insert(i2+1,".")
            #print(gramatica[i])  
        return gramatica
    
    #metodo listo
    def obtenerArista(self, gramatica, prod):
        for i in range (len(gramatica)):
            for i2 in range(len(gramatica[i])):
                if i2 < len(gramatica[i]):
                    if gramatica[i][i2] == "." and gramatica[i][i2+1] == prod[1]:
                        return prod[1]
            #print(gramatica[i])
        return -1
    
    #Metodo listo
    def quitarPunto(self, gramatica, prod):
        for i in range (len(gramatica)):
            for i2 in range(len(gramatica[i])):
                if i2 < len(gramatica[i]):
                    if gramatica[i][i2] == "." and gramatica[i][i2+1] == prod[1]:
                        gramatica[i].pop(i2)
            #print(gramatica[i])
        return gramatica
    
    #metodo listo
    def limpiarGramatica(self, lista, arista):
        aux = lista
        encontro=False
        #self.mostar_Gramatica(aux)
        i=0
        while i < len(aux):
            for i2 in range(len(aux[i])):
                if aux[i][i2] == ".":
                    encontro=True
            if encontro == True:
                aux.pop(i)
                i=i-1
                encontro=False
            i=i+1
        #self.mostar_Gramatica(aux)
        return aux
    
    def crearEstado(self, gramatica, prod):
        arista=self.obtenerArista(gramatica, prod)
        lista_Aux=self.quitarPunto(gramatica, prod)
        nuevaGramatica=self.verificarSiguiente(lista_Aux, arista)
        
        
        nuevoEstado = self.ponerPunto(gramatica, arista) 
        #hay que mirar el punto para poderlo correr
        print("crear un estado solucionando")
        
        
    def ponerPunto(self, gramatica, arista):
        print("Poner punto sin solucionar")
    
                
        
    # self.mostar_Gramatica(aux)
    def verificarSiguiente(self, lista_Aux, arista):
        aux=self.limpiarGramatica(lista_Aux, arista)
        
        
        return aux
        
        
    def mostar_Gramatica(self, gramatica):
        for i in range(len(gramatica)):
            print(gramatica[i])




class Estado():
    def __init__(self, ide, estado_Inicial, lista):
        self.ide=ide
        self.nodo_Inicial=estado_Inicial
        self.lista=lista
    
    def crear_Estado(lista):
        print("listas")
        return None
        
        
#####################################
producciones=["S","E","T","F"]

lista0=["S","-","E"]
lista1=["E","-","E","+","T"]
lista2=["E","-","T"]
lista3=["T","-","T","*","T"]
lista4=["T","-","F"]
lista5=["F","-","id"]
lista6=["F","-","(","E",")"]

#lista0.insert(2,".")
#lista0.pop(2)

gramatica=[]
gramatica.append(lista0)
gramatica.append(lista1)
gramatica.append(lista2)
gramatica.append(lista3)
gramatica.append(lista4)
gramatica.append(lista5)
gramatica.append(lista6)

a = Automata()
estado0 = a.crearPunto(gramatica)
estado1 = a.crearEstado(estado0, producciones)























