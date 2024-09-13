from time import perf_counter
import matplotlib.pyplot as plt


############################ P1 ##############################
class PCB:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.memo = {}
        self.tiempo_medido = []
    
    def Caminos_recursivo(self, x = 1, y = 1):
        #casos base, estar en B o en los bordes de la grilla
        if x == self.N or y == self.M:
            return 1
        #recursividad
        return self.Caminos_recursivo(x+1, y) + self.Caminos_recursivo(x, y+1)

    def Caminos_iterativos(self, x=1, y=1):
        # inicializar la matriz con None
        matriz = []
        for i in range(self.N):
            matriz.append([None] * self.M)

        # casos base / borde
        for i in range(self.N):
            matriz[i][self.M - 1] = 1  # Última columna
        for j in range(self.M):
            matriz[self.N - 1][j] = 1  # Última fila

        # llenar la matriz de abajo hacia arriba y de derecha a izquierda
        for i in range(self.N - 2, -1, -1):
            for j in range(self.M - 2, -1, -1):
                matriz[i][j] = matriz[i + 1][j] + matriz[i][j + 1]

        return matriz[0][0]
    
     # Método para medir el tiempo de ejecución del método recursivo
    def tiempo_Caminos_recursivo(self):
        tiempo_inicio = perf_counter()
        resultado = self.Caminos_recursivo() 
        tiempo_total = perf_counter() - tiempo_inicio
        return tiempo_total

    def tiempo_Caminos_iterativos(self):
        tiempo_inicio = perf_counter()
        resultado = self.Caminos_iterativos()  
        tiempo_total = perf_counter() - tiempo_inicio
        return tiempo_total
    
    ############################ P2 ##############################

    def medir_tiempo(self, func, x=1 , y=1):
        tiempo_inicio = perf_counter()
        resultado = func(x, y)
        tiempo_total = perf_counter() - tiempo_inicio
        self.tiempo_medido.append(tiempo_total)
        return resultado 

pcb = PCB(6, 6)
############################ P2 ##############################

#Medir el tiempo de la solución recursiva usando medir_tiempo
resultado_recursivo = pcb.medir_tiempo(pcb.Caminos_recursivo)
print(f"Resultado recursivo: {resultado_recursivo}")
print(f"Tiempos medidos: {pcb.tiempo_medido[-1]}")

#Medir el tiempo de la solución iterativa usando medir_tiempo
resultado_iterativo = pcb.medir_tiempo(lambda x, y: pcb.Caminos_iterativos())
print(f"Resultado iterativo: {resultado_iterativo}")
print(f"Tiempos medidos: {pcb.tiempo_medido[-1]}")

