package main

import (
	"fmt"
	"github.com/jacqinthebox/escaperooms/db"
)

func main() {
	err := db.CreateDatabase()
	if err != nil {
		fmt.Println(err)
		return
	}
}
