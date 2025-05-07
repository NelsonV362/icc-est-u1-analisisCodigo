from bechmarkin import Benchmarking
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("Funciona")
    benchmark = Benchmarking()
    resultados = benchmark.get_resultados()

    tiempos_by_metodo = {
        "burbuja": [],
        "burbuja_MEJORADO": [],
        "Seleccion": [],
        "shell": [],
    }

    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)

    plt.figure(figsize=(10, 6))
    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label=nombre, marker="o")

    plt.title("Comparación de tiempo para cada método de ordenamiento")
    plt.xlabel("Nelson Villalta - 06/05/2025-20:04")
    plt.xlabel("Tamaño de los arreglos")
    plt.ylabel("Tiempo de ejecución (ms)")
    plt.legend()
    plt.show()
