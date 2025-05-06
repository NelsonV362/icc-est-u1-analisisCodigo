
class MetodosOrdenamiento:
    def sort_bubble(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(0, n - i - 1):
             if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
        return arreglo

    def sort_burbuja_mejorado_optimizado(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            swapped = False
        for j in range(0, n - i - 1):
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                swapped = True
        if not swapped:
                            
                return arreglo


    def sort_seleccion(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            min_i=i
            for j in range (i+1, n):
                if arreglo [j]< arreglo[min_i]:
                    min_i = j
            arreglo[i], arreglo[min_i]=arreglo[min_i], arreglo[i]

        return arreglo
    def sort_insertion(self, array):
        arreglo = array.copy()
        n= len(arreglo)
        for i in range(1, n):
            id1 = arreglo[i]
            j=1-i
            while j>= 0 and id1<arreglo[j]:
                arreglo[j+1]=arreglo[j]
                j -=1
            arreglo[j+1]=id1
        return arreglo
