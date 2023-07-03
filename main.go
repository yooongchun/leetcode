package main

import "fmt"

func main() {
	str := "worrlddd"
	for i, s := range str {
		fmt.Println(i, string(s))
	}
}
