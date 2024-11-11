package main

import "fmt"

func main() {
    // Declaración de un array de tamaño fijo
    var fixedArray [5]int
    fixedArray[0] = 10
    fixedArray[1] = 20
    fmt.Println("Array de tamaño fijo:", fixedArray)

    // Declaración de un slice
    var dynamicSlice []int
    dynamicSlice = append(dynamicSlice, 1, 2, 3, 4)
    fmt.Println("Slice dinámico:", dynamicSlice)

    // Declaración de otro array y slice con distintos tipos
    var strArray [3]string = [3]string{"Go", "Lexer", "Test"}
    var boolSlice []bool = []bool{true, false, true}

    fmt.Println("Array de strings:", strArray)
    fmt.Println("Slice de booleanos:", boolSlice)

    // Operadores básicos
    a := 10
    b := 3
    result := a + b
    fmt.Println("Suma:", result)

    // Operaciones con slices y arrays
    fixedArray[2] = result
    dynamicSlice[2] += 5
    fmt.Println("Array modificado:", fixedArray)
    fmt.Println("Slice modificado:", dynamicSlice)

    // Prueba de un comentario en línea
    // Esto es un comentario de una sola línea

    /* Prueba de comentario
       de múltiples líneas */
}
