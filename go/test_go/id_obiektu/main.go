package main

import "fmt"

func main() {
	// 1. Tworzymy slice (zauważ brak liczby w [])
	// Pod spodem Go tworzy tablicę, a "a" to tylko mała struktura (wskaźnik), która na nią patrzy.
	a := []int{1, 2, 3}

	// 2. Przypisujemy "a" do "b"
	// Kopiujemy tylko "Pilota" (adres w pamięci).
	b := a

	// 3. Zmieniamy "b"
	b[0] = 999

	// 4. Sprawdzamy "a"
	fmt.Println("Oryginał (a):", a) // [999 2 3] <-- ZMIENIŁO SIĘ!
	fmt.Println("Kopia (b):   ", b) // [999 2 3]
}
