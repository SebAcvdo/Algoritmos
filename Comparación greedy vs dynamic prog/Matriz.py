import sys
from timeit import default_timer
import matplotlib.pyplot as plt
import statistics

def multMatriz(dims):
    n = len(dims)
    c = [[0 for x in range(n + 1)] for y in range((n + 1))]
    for length in range(2, n + 1):        
        for i in range(1, n - length + 2):
            j = i + length - 1
            c[i][j] = sys.maxsize
            k = i
            while j < n and k <= j - 1:
                cost = c[i][k] + c[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                if cost < c[i][j]:
                    c[i][j] = cost
                k = k + 1
    return c[1][n - 1]

def greedyMatriz(p, i, j):
    if i == j:
        return 0
    min = sys.maxsize
    for k in range(i, j):
        count = (greedyMatriz(p, i, k)
                 + greedyMatriz(p, k + 1, j)
                 + p[i-1] * p[k] * p[j])
        if count < min:
            min = count
    return min

dims = [1,2,2,3,3,4,4,5,5,6,6,7]
n = len(dims)
vD=[]
vV=[]
vN=[]
k=0
vA=[]

while(k<5):
    k=k+1
    vN.append(k)
    t1= default_timer()
    multMatriz(dims)
    f1 = default_timer()
    tD=(f1-t1)*10000
    vD.append(tD)

    t2= default_timer()
    greedyMatriz(dims, 1, n-1)

    f2 = default_timer()
    tV=(f2-t2)*10000
    vV.append(tV)

print("Costo de Operaciones Dynamic=", multMatriz(dims))
print("Costo de operaciones Greedy=",greedyMatriz(dims, 1, n-1))
prom1= statistics.mean(vD)
print("Tiempo Dynamic:",prom1,"ms")
prom2= statistics.mean(vV)
print("Tiempo Voraz:",prom2,"ms")


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