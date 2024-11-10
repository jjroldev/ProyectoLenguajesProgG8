package main

import "fmt"
//comentario 1 linea^^&&&*
/*linea1
linea2
linea3&*(*)
*/
func main() {
    var a int = 10
    var b float64 = 20.5
    var c bool = true
    var name string = "LexerTest"
    const d int = 100

    a += 5
    b -= 2.5
    a *= 2
    b /= 2.0
    a %= 3

    if a == 10 && b > 10.0 || !c {
        fmt.Println("Operador lógico AND y OR")
    } else if a != 5 || b <= 15.5 {
        fmt.Println("Operador NOT y comparación")
    }

    a = a & 5
    b = b | 3

    a <<= 2
    b >>= 1

    a++
    b--

    switch name {
    case "LexerTest":
        fmt.Println("Nombre correcto")
    case "Test":
        fmt.Println("Nombre alternativo")
    default:
        fmt.Println("Nombre desconocido")
    }

    for i := 0; i < 5; i++ {
        fmt.Println(i)
    }

    c = false
    if !c && (a < 10 || b >= 20.0) {
        fmt.Println("Condición final")
    }

    if a == 10 {
        fmt.Println("A es igual a 10")
    }

    fmt.Println(a + int(b))
}
