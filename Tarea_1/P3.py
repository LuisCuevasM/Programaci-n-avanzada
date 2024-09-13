from time import perf_counter


tiempo_medido = []

# Decorador para medir el tiempo de ejecución de una función
def medir_tiempo_decorador(func):

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
        self.memo = {}

    # Esta función ya no lleva el decorador para evitar medir el tiempo en cada recursión
    def Caminos_recursivo(self, x=1, y=1):
        # Casos base: estar en B o en los bordes de la grilla
        if x == self.N or y == self.M:
            return 1
        # Recursividad
        return self.Caminos_recursivo(x + 1, y) + self.Caminos_recursivo(x, y + 1)

    @medir_tiempo_decorador  # Decoramos la función para medir el tiempo de la primera llamada
    def ejecutar_Caminos_recursivo(self):
        return self.Caminos_recursivo()  # Llamar a la función recursiva sin medir el tiempo en cada recursión

    @medir_tiempo_decorador  # Decoramos la función para medir el tiempo de ejecución
    def Caminos_iterativos(self, x=1, y=1):
        # Inicializar la matriz con None
        matriz = [[None] * self.M for _ in range(self.N)]

        # Casos base / borde
        for i in range(self.N):
            matriz[i][self.M - 1] = 1  # Última columna
        for j in range(self.M):
            matriz[self.N - 1][j] = 1  # Última fila

        # Llenar la matriz de abajo hacia arriba y de derecha a izquierda
        for i in range(self.N - 2, -1, -1):
            for j in range(self.M - 2, -1, -1):
                matriz[i][j] = matriz[i + 1][j] + matriz[i][j + 1]

        return matriz[0][0]

# Crear instancia de la clase PCB
pcb = PCB(6, 6)

# Llamar a la función que ejecuta el camino recursivo decorado
resultado_recursivo = pcb.ejecutar_Caminos_recursivo()
print(f"Resultado recursivo: {resultado_recursivo}")
print(f"Tiempos medidos: {tiempo_medido[-1]}")

# Llamar a los métodos decorados
resultado_iterativo = pcb.Caminos_iterativos()
print(f"Resultado iterativo: {resultado_iterativo}")
print(f"Tiempos medidos: {tiempo_medido[-1]}")