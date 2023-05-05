// Author: fransay
// Date: 05/05/23
// Description: Project Euler (Multiples of 3 or 5)

package main

import "fmt"

// program entry point
func main() {
	var sum int = 0
	for i := 0; i < 1000; i++ {
		if i%3 == 0 || i%5 == 0 {
			sum += i
		}
	}
	fmt.Println("SUM: ", sum)
}
