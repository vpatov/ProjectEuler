// By considering the terms in the Fibonacci sequence whose values 
// do not exceed four million, find the sum of the even-valued terms.
// 4613732
package main

import "fmt"


func main() {
	var fib_nums [64]int
	fib_nums[0] = 1
	fib_nums[1] = 1
	i := 2
	sum := 0
	for fib_nums[i-1] < 4_000_000 {
		fib_nums[i] = fib_nums[i-1] + fib_nums[i-2]
		if fib_nums[i] % 2 == 0 {
			sum += fib_nums[i]
		}
		i += 1
	}
	fmt.Println(sum)

}