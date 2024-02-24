from timeit import default_timer
import matplotlib.pyplot as plt

def mochila(p_mochila, p_articulos, valor, n):
    #Se crea la tabla
    K = [[0 for w in range(p_mochila + 1)]for i in range(n + 1)]
             
    # Se construye la tabla (Bottom Up)
    for i in range(n + 1):
        for j in range(p_mochila + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif p_articulos[i - 1] <= j:
                K[i][j] = max(valor[i - 1] + K[i - 1][j - p_articulos[i - 1]] , K[i - 1][j])
            else:
                K[i][j] = K[i - 1][j]
 
    #Guarda el resultado de el mejor caso para mostrar 
    res = K[n][p_mochila]
    print("Cantidad de ganancia máxima: ",res)
     
    j = p_mochila
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # Una vez la tabla finalizada y viendo el resultado, este puede venir ya sea de (K[i-1][w]) o (valor[i-1]+ K[i-1] [w-p_articulos[i-1]]). 
        #Si viene de (valor[i-1]+ K[i-1] [w-p_articulos[i-1]]) significa que ese objeto va dentro de la mochila.
        if res == K[i - 1][j]:
            continue
        else:
            #Como se mencionó antes => Viene de (valor[i-1]+ K[i-1] [w-p_articulos[i-1]]) por lo tanto se inlcuye.
            print("Peso del artículo: ", p_articulos[i - 1], end=" || ")
            print("Valor del artículo: ",valor[i - 1])
             
            # Se deduce el valor a partir del peso del objeto ya incluido.
            res = res - valor[i - 1]
            j = j - p_articulos[i - 1]

def greedy_knapsack(objetos, p_mochila,n):
    objetos = sorted(objetos, key=lambda objetos:objetos[0], reverse=True)
    new_objetos = objetos
    res = 0
    for i in range(0,n):
        p_articulos,valor = objetos[i]  
        cantidad = (p_mochila-p_mochila%p_articulos)/p_articulos
        new_objetos[i] = (cantidad,valor)
        p_mochila = p_mochila%p_articulos
        res += cantidad*valor
    print("Cantidad de ganancia máxima:",round(res,2))
    for j in range (0,n):
        if new_objetos[j][0] != 0:
            print("Cantidad",new_objetos[j][0], end=" || ")
            print("Valor",new_objetos[j][1])

lineas = [5,11,12,13,14,15]
p_mochila = 0
p_articulos = []
valor = []

#Examina los valores dentro del archivo y loa guarda en los arreglos para mandarlos a la función
archivo = open("info_mochilaD.txt")
for posicion, linea in enumerate(archivo):
    if posicion in lineas:
        nuevo = linea.split()
        if posicion == 5: p_mochila = (int(nuevo[2]))
        else:
            p_articulos.append(int(nuevo[1]))
            valor.append(int(nuevo[2]))


n = len(valor)  

objetos = []
for i in range(0,n):
    objetos.append([p_articulos[i],valor[i]])

k=0
vD=[]
vV=[]
vN=[]
while(k<5):
    k=k+1
    vN.append(k)
    #Toma el tiempo de ejecución dinamica
    print("===================Programacióon dinámica===================")
    t1= default_timer()
    mochila(p_mochila, p_articulos, valor, n)
    f1 = default_timer()
    tD=(t1-f1)*10000
    vD.append(tD)

    #Toma el tiempo de ejecución voraz
    print("===================Método Voraz===================")
    t2 = default_timer()
    greedy_knapsack(objetos, p_mochila,n)
    f2 = default_timer()
    tV=(t1-f2)*10000
    vV.append(tV)

archivo.close()

plt.plot(vN,vD,marker='*',color='red')
plt.plot(vN,vV,marker='+',color='blue')
plt.xlabel('N-de pruebas')
plt.ylabel('Tiempo')
plt.title("Dynamic vs Greedy", 
          fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 18})
plt.legend(['Dynamic','Greedy'])
plt.text(4400,-1,"Daniel Avila",fontsize=8)
plt.text(10,10,"Sebastian Acevedo",fontsize=8)
plt.show()