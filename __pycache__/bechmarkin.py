from metodos_ordenamiento import MetodosOrdenamiento
import random
import time

class Benchmarking:
    def __init__(self):
        print('Benchmarking instanciado')
        self.mO = MetodosOrdenamiento()
        arreglo = self.build_arreglo(10000)

        print("\n--- Método: burbujaa ---")
        tarea1 = lambda: self.mO.sort_bubble(arreglo.copy())
        tiempoM1 = self.contar_con_current_time_milles(tarea1)
        tiempoN1 = self.contar_con_nano_time(tarea1)
        print("Tiempo con milisegundos:", tiempoM1)
        print("Tiempo con nano segundos:", tiempoN1)

        print("\n--- Método: Burbja mejorado ---")
        tarea2 = lambda: self.mO.sort_burbuja_mejorado_optimizado(arreglo.copy())
        tiempoM2 = self.contar_con_current_time_milles(tarea2)
        tiempoN2 = self.contar_con_nano_time(tarea2)
        print("Tiempo con milisegundos:", tiempoM2)
        print("Tiempo con nano segundos:", tiempoN2)

        print("\n---Metodo: Seleccion----")
        tarea3 = lambda: self.mO.sort_seleccion(arreglo.copy())
        tiempoM3 = self.contar_con_current_time_milles(tarea3)
        tiempoN3 = self.contar_con_nano_time(tarea3)
        print("Tiempo con milisegundos:", tiempoM3)
        print("Tiempo con nanosegundos:", tiempoN3)

        print("\n ---Metodo: INsercion")
        tarea4 = lambda: self.mO.sort_insertion(arreglo.copy())
        tiempoM4=self.contar_con_current_time_milles(tarea4)
        tiempoN4=self.contar_con_nano_time(tarea4)
        print("TIempo condato con milisegundos:", tiempoM4)
        print("tIempo contado con nanosegundos:", tiempoM4)


    def build_arreglo(self, tamaño):
        arreglo = []  
        for i in range(tamaño):
            numero = random.randint(0, 99999)
            arreglo.append(numero)
        return arreglo

    def contar_con_current_time_milles(self, tarea):
        inicio = time.time()
        tarea()
        fin = time.time()
        return (fin - inicio) * 1000  
    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()  
        tarea()
        fin = time.time_ns()
        return fin - inicio
