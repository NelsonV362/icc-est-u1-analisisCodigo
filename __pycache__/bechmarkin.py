from metodos_ordenamiento import MetodosOrdenamiento
import random
import time

class Benchmarking:
    def __init__(self):
        print('Benchmarking instanciado')
        self.mO = MetodosOrdenamiento()
        self.resultados = []

        tamanio = 10000
        arreglo = self.build_arreglo(tamanio)

        print("\n--- Método: burbuja ---")
        tarea1 = lambda: self.mO.sort_bubble(arreglo.copy())
        tiempo = self.contar_con_current_time_milles(tarea1)
        self.resultados.append((tamanio, "burbuja", tiempo))
        print("Tiempo (ms):", tiempo)

        print("\n--- Método: burbuja_MEJORADO ---")
        tarea2 = lambda: self.mO.sort_burbuja_mejorado_optimizado(arreglo.copy())
        tiempo = self.contar_con_current_time_milles(tarea2)
        self.resultados.append((tamanio, "burbuja_MEJORADO", tiempo))
        print("Tiempo (ms):", tiempo)

        print("\n--- Método: Seleccion ---")
        tarea3 = lambda: self.mO.sort_seleccion(arreglo.copy())
        tiempo = self.contar_con_current_time_milles(tarea3)
        self.resultados.append((tamanio, "Seleccion", tiempo))
        print("Tiempo (ms):", tiempo)

        print("\n--- Método: shell ---")
        tarea4 = lambda: self.mO.sort_insertion(arreglo.copy())
        tiempo = self.contar_con_current_time_milles(tarea4)
        self.resultados.append((tamanio, "shell", tiempo))
        print("Tiempo (ms):", tiempo)

    def build_arreglo(self, tamaño):
        return [random.randint(0, 99999) for _ in range(tamaño)]

    def contar_con_current_time_milles(self, tarea):
        inicio = time.time()
        tarea()
        fin = time.time()
        return (fin - inicio) * 1000  # tiempo en milisegundos

    def get_resultados(self):
        return self.resultados
