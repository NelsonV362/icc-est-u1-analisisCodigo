public class App {
    public static void main(String[] args) {

        MetodosOrdenamiento ordenador = new MetodosOrdenamiento();
        int[] arregloBurbuja = { 34, 2, 10, 6, 7, 5, 1, 15 };
        int[] arregloSeleccion = { 34, 2, 10, 6, 7, 5, 1, 15 };
        int[] arregloInsercion = { 34, 2, 10, 6, 7, 5, 1, 15 };

        
        int[] arregloBurbujaOrdenado1 = ordenador.burbujaTradicional(arregloBurbuja);
        System.out.println(
                "Resultado burbuja tradicional Metodo 1 : " +
                        java.util.Arrays.toString(arregloBurbujaOrdenado1));

        int[] arregloBurbujaOrdenado2 =
        ordenador.burbujaTradicionalSegundo(arregloBurbuja);
        System.out.println(
        "Resultado burbuja tradicional Metodo 2: " +
        java.util.Arrays.toString(arregloBurbujaOrdenado2));

        int[] arregloBurbujaOrdenado3 =
        ordenador.burbujaTradicionalTercero(arregloBurbuja);
        System.out.println(
        "Resultado burbuja tradicional Metodo 3: " +
        java.util.Arrays.toString(arregloBurbujaOrdenado3));

        int[] arregloSeleccionOrdenado1 =
        ordenador.seleccionPrimero(arregloSeleccion);
        System.out.println(
        "Resultado selección Metodo 1: " +
        java.util.Arrays.toString(arregloSeleccionOrdenado1));

        int[] arregloSeleccionOrdenado2 =
        ordenador.seleccionSegundo(arregloSeleccion);
        System.out.println(
        "Resultado selección Metodo 2: " +
        java.util.Arrays.toString(arregloSeleccionOrdenado2));

        int[] arregloSeleccionOrdenado3 =
        ordenador.seleccionTercero(arregloSeleccion);
        System.out.println(
        "Resultado selección Metodo 3: " +
        java.util.Arrays.toString(arregloSeleccionOrdenado3));

        int[] arregloInsercionOrdenado1 =
        ordenador.insercionPrimero(arregloInsercion);
        System.out.println(
        "Resultado selección Metodo 1: " +
        java.util.Arrays.toString(arregloInsercionOrdenado1));

        int[] arregloInsercionOrdenado2 =
        ordenador.insercionSegundo(arregloInsercion);
        System.out.println(
        "Resultado selección Metodo 1: " +
        java.util.Arrays.toString(arregloInsercionOrdenado2));

        int[] arregloInsercionOrdenado3 =
        ordenador.insercionTercero(arregloInsercion);
        System.out.println(
        "Resultado selección Metodo 1: " +
        java.util.Arrays.toString(arregloInsercionOrdenado3));

    }
}