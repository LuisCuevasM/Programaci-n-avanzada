from time import perf_counter

tiempo_medido = []

# Decorador para medir el tiempo de ejecución de una función
def almacenar_tiempo_decorador(func):

    def nueva_fuccion(x=1, y=1):
        tiempo_inicio = perf_counter()
        resultado = func(x)
        tiempo_total = perf_counter() - tiempo_inicio
        tiempo_medido.append(tiempo_total)
        return resultado 
    return nueva_fuccion

############################ P1 ##############################
class PCB:
    def __init__(self, N, M):
        self.N = N
        self.M = M

    # Método recursivo para calcular caminos
    def Caminos_recursivo(self, x=1, y=1):
        if x == self.N or y == self.M:
            return 1
        return self.Caminos_recursivo(x + 1, y) + self.Caminos_recursivo(x, y + 1)

    # Método iterativo para calcular caminos
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
            matriz[i][self.M - 1] = 1  
        for j in range(self.M):
            matriz[self.N - 1][j] = 1  

        # llenar la matriz de abajo hacia arriba y de derecha a izquierda
        for i in range(self.N - 2, -1, -1):
            for j in range(self.M - 2, -1, -1):
                matriz[i][j] = matriz[i + 1][j] + matriz[i][j + 1]

        return matriz[0][0]

    # Decoramos este nuevo método para medir y almacenar el tiempo
    @almacenar_tiempo_decorador
    def calcular_caminos(self):
        if self.solucion_activa == 'recursivo':
            print("Usando la solución recursiva")
            return self.Caminos_recursivo()
        elif self.solucion_activa == 'iterativo':
            print("Usando la solución iterativa")
            return self.Caminos_iterativos()

    # Método para cambiar la solución activa
    def cambiar_solucion(self, nueva_solucion):
        if nueva_solucion in ['recursivo', 'iterativo']:
            self.solucion_activa = nueva_solucion
        else:
            print("Solución no válida. Usa 'recursivo' o 'iterativo'.")

# Ejemplo de uso
pcb = PCB(15, 15)


pcb.cambiar_solucion('recursivo')
# Usar la solución recursiva
resultado_recursivo = pcb.calcular_caminos()
print(f"Resultado recursivo: {resultado_recursivo}")
print(f"Tiempos medidos: {tiempo_medido[-1]}")

# Ccmbiar a la solución iterativa
pcb.cambiar_solucion('iterativo')

resultado_iterativo = pcb.calcular_caminos()
print(f"Resultado iterativo: {resultado_iterativo}")
print(f"Tiempos medidos: {tiempo_medido[-1]}")
