import matplotlib.pyplot as plt
from time import perf_counter

tiempo_medido = []

# decorador para medir el tiempo de ejecución de una función
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
            return self.Caminos_recursivo()
        elif self.solucion_activa == 'iterativo':
            return self.Caminos_iterativos()

    # Método para cambiar la solución activa
    def cambiar_solucion(self, nueva_solucion):
        if nueva_solucion in ['recursivo', 'iterativo']:
            self.solucion_activa = nueva_solucion
            
# Generar los datos de los tiempos de ejecución
def generar_datos():
    global tiempo_medido
    tamanios = range(2, 13)  # Tamaños de grilla desde 2x2 hasta 12x12
    tiempos_recursivo = []
    tiempos_iterativo = []

    for tam in tamanios:
        # Instanciar la clase PCB con una grilla de tam x tam
        pcb = PCB(tam, tam)
        
        # Usar la solución recursiva y medir el tiempo
        pcb.cambiar_solucion('recursivo')
        tiempo_medido = [] # Reiniciar la lista de tiempos
        pcb.calcular_caminos()
        tiempos_recursivo.append(tiempo_medido[0]) # Almacenar el último tiempo medido

        # Usar la solución iterativa y medir el tiempo
        pcb.cambiar_solucion('iterativo')
        tiempo_medido = []  
        pcb.calcular_caminos()
        tiempos_iterativo.append(tiempo_medido[0])  

    return tamanios, tiempos_recursivo, tiempos_iterativo

# Función para generar gráficos
def graficar_tiempos(tamanios, tiempos_recursivo, tiempos_iterativo):
    plt.figure(figsize=(10, 6))
    plt.plot(tamanios, tiempos_recursivo, label='Solución Recursiva', marker='o')
    plt.plot(tamanios, tiempos_iterativo, label='Solución Iterativa', marker='s')
    plt.title('Tiempo de ejecución de soluciones recursivas e iterativas')
    plt.xlabel('Tamaño de la grilla N x N')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.legend()
    plt.grid(True)


    plt.savefig('tiempos_ejecucion.svg')  # archivo SVG
    plt.show()
# Programa principal
tamanios, tiempos_recursivo, tiempos_iterativo = generar_datos()
graficar_tiempos(tamanios, tiempos_recursivo, tiempos_iterativo)




