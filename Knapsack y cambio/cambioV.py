from timeit import default_timer
import numpy as np
import matplotlib.pyplot as plt

def cambioVora(V,deno):
    n = len(deno)
    #Arreglo de resultado
    res = []
  
    #Examina las denominaciones
    i = n - 1
    while(i >= 0):
          
        # Encuentra las denoiminaciones
        while (V >= deno[i]):
            V -= deno[i]
            res.append(deno[i])
  
        i -= 1
  
    # Imprime
    for i in range(len(res)):
        print(res[i], end = " ")
lineas = [5,7]
n = 0
deno = []

d = [1, 2, 5, 10]
N = 15
sol={}
for denomination in d:
  sol[denomination]=0

acc = 0
i = len(d)-1
while acc<N:
  if (N-acc) >= d[i]:
    acc += d[i]
    sol[d[i]] += 1
  else:
    i -= 1

m = np.zeros( (len(d), N+1) )
def cambioDyn(k):
  for col in range (1,N+1):
    m[0][col]=col 
  for row in range (1, len(d)):
    for col in range (1, N+1):
      if d[row]>col:
        m[row][col] = m[row-1][col]
      else:
        m[row][col] = min( m[row-1][col], m[row][col-d[row]]+1 )

#Examina los valores dentro del archivo y loa guarda en los arreglos para mandarlos a la función
archivo = open("info_cambioV.txt")
for posicion, linea in enumerate(archivo):
    if posicion in lineas:
        nuevo = linea.split()
        if posicion == 7: 
            n = (int(nuevo[3]))
        elif posicion == 5:
            for i in range(1,len(nuevo)):
                deno.append(int(nuevo[i]))
             
k=0
vD=[]
vV=[]
vN=[]
while(k<5):
  k=k+1
  vN.append(k)
  print("Mínimo de monedas a usar para", n, ": ", end = "")
  t1 = default_timer()
  cambioVora(n,deno)
  f1 = default_timer()
  tV=(f1-t1)*1000000
  vV.append(tV)
  t2 = default_timer()
  cambioDyn(m)
  print('')
  print('')
  print(m)
  print("Min de monedas:"+str(m[len(d)-1][N]))
  f2= default_timer()
  tD=(f2-t2)*10000
  vD.append(tD)
archivo.close()

plt.plot(vN,vV,marker='*',color='Black')
plt.plot(vN,vD,marker='+',color='Red')
plt.xlabel('N-de pruebas')
plt.ylabel('Tiempo')
plt.title("Dynamic vs Greedy-Change", 
          fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 18})
plt.legend(['Greedy','Dynamic'])
plt.text(4400,-1,"Daniel Avila",fontsize=8)
plt.text(10,10,"Sebastian Acevedo",fontsize=8)
plt.show()
