#open file in read mode
import heapq
import copy
from timeit import default_timer
from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import msvcrt

def frecuencia(nombreAr):

    file = open(nombreAr,"r")

    frecuencias = []
    caracter = []
    freq = []
    chkp = 0
    while 1:
        char = file.read(1)         
        if not char:
            break
        if not caracter:
            caracter.append(char)
            freq.append(0)
        for i in range(0,len(caracter)):
            if caracter[i] == char:
                freq[i]= freq[i] + 1
                chkp = 0
                break
            else: chkp = 1
        if chkp == 1:
            caracter.append(char)
            freq.append(1)      

    for i in range(0,len(freq)):
        frecuencias.append((freq[i],caracter[i]))    

    file.close()
    return frecuencias
    #return crearArbol(frecuencias)



def crearArbol(listaFreq):
    heap = []
    for freq in listaFreq: heapq.heappush(heap, [freq])
    while (len(heap) > 1):
        izq0 = heapq.heappop(heap)
        der1 = heapq.heappop(heap)

        freqIzq, letraIzq = izq0[0]
        frqDer, letraDer = der1[0]

        freqT = freqIzq + frqDer
        cadena = ''.join(sorted(letraIzq+letraDer))
        nodo = [(freqT,cadena),izq0,der1] 
        #print(nodo)
        heapq.heappush(heap,nodo)
    #print(heap.pop())    
    final = heap.pop()
    return final
    #return tablaCodigo(final)



def printArbol(arbol, nivel = 0, dir = "[Inicio]"):
    freq, letra = arbol[0]
    newletra = ""
    izq0 = arbol[1] if (len(arbol) >=2) else None
    der1 = arbol[2] if (len(arbol)>=3) else None

    if(len(letra)==1):
        for char in letra:
            if(char == "\n"): newletra += ("\\"+"n")
            elif(char == " "): newletra += "' '"
            else: newletra += char
        print('         '*nivel,dir,"(",newletra,",",freq,")")
    else:
        print('         '*nivel,dir,"{",freq,"}")
    if (izq0 != None): [printArbol(izq0,nivel+1, dir= "[0]")]
    if (der1 != None): [printArbol(der1,nivel+1, dir= "[1]")]



def recorreArbol(arbol, codigo, bincode):
    #Arbol = [valor, izq0, der1] 
    if(len(arbol) == 1):
        freq, letra = arbol[0]
        codigo[letra] = bincode
    else: 
        valor,izq0,der1 = arbol
        recorreArbol(izq0,codigo,bincode+'0')
        recorreArbol(der1,codigo,bincode+'1')


def crearCodigo(arbol):
    codigo = dict()
    recorreArbol(arbol, codigo, '')
    #print(codigo)
    return codigo

def codificar(codigo,nombreAr):
    file = open(nombreAr, "r")
    compresion = ""
    while 1:
        char = file.read(1)
        if not char:
            break
        compresion += codigo[char]
        #print (compresion)
    file.close()
    return compresion

def decodificar(compresion,arbol,nombreAr):
    newfile = open("new"+nombreAr,"w")
    newarbol = copy.deepcopy(arbol)
    contador = 0

    for digito in compresion:
        if(digito =='0'): newarbol = newarbol[1]
        else: newarbol = newarbol[2]
        if(len(newarbol) == 1):
            contador += 1
            freq,letra = newarbol[0]
            newfile.write(letra)
            newarbol = arbol
    newfile.close()
    return("new"+nombreAr)
    #print (''.join(chars))


def imagen(k):
    image = Image.open(k).convert("L")
    arr = np.asarray(image)
    plt.imshow(arr, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')
    plt.savefig("p1.png",bbox_inches='tight')
    k=cv2.imread("p1.png",0)
    print(k)
    nombre = 'p1cadena.txt'
    np.savetxt('p1cadena.txt',k, fmt='% 1d')
    return(nombre)


def huffman(nombreAr):
    inicio = default_timer()
    freq = frecuencia(nombreAr)
    arbol = crearArbol(freq)
    codigo = crearCodigo(arbol)
    compresion = codificar(codigo,nombreAr)
    newAr= decodificar(compresion,arbol,nombreAr)
    final = default_timer()
    tiempo = (final-inicio)*1000

    print("\n=========================================== Codificacion ============================================\n")
    print(compresion)
    print("\n============================================= Arbol Binario =============================================\nNota:\n' ' = espacio\n\\"+
        "n = salto de linea\n{} = Nodo \n(a,23) = (letra,frecuencia)\n[0] = Camino izquiera\n[1] = Camino derecha\n")
    printArbol(arbol)

    newletra = ""
    bitscompre = len(compresion)
    bitstext = arbol[0][0]*8
    print("\n=========================================== CASO",nombreAr," ============================================\n")
    print("Archivo de entrada =", nombreAr,"||  Archivo de salida =", newAr,"\n")
    print("Bits totales sin comprimir:", bitstext)
    print("Bits totales después de comprimir:", bitscompre)
    print("Porcentaje total de compresión =",round(((bitscompre*100)/bitstext),2),"%")
    print("Tiempo de compresión y decompresión: ",round(tiempo,4), "milisegundos")
    print()

    header = ["Simbolo", "Frecuencia", "Codigo"]
    matriz = []

    for char in freq:
        if(char[1] == "\n"): newletra = ("\\"+"n")
        elif(char[1] == " "): newletra = "' '"
        else: newletra = char[1]
        matriz.append([newletra,char[0],codigo[char[1]]])
    print(tabulate(sorted(matriz),header, tablefmt='fancy_grid'))

opc = ["ADN1.txt", "ADN2.txt" ,"ADN3.txt", "Texto.txt","Imagen.png"]    
print("Seleccione una opción")
for i in range(len(opc)):
    print(i+1,".-", opc[i])
selec = int(input())
if (selec > len(opc)):
    print("Seleccione una opcion valida")
elif(selec == 5):
    huffman(imagen(opc[selec-1]))
else: 
    huffman(opc[selec-1])

msvcrt.getch()