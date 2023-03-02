package db

import (
	"database/sql"
	"fmt"
	"github.com/lib/pq"
)

func CreateDatabase() error {
	// Connect to the Postgresql server using the pq driver
	db, err := sql.Open("postgres", "postgres://postgres:mysecretpassword@localhost:5432/postgres?sslmode=disable")
	if err != nil {
		return fmt.Errorf("failed to connect to database: %v", err)
	}
	defer db.Close()

	// Create the new database
	_, err = db.Exec("CREATE DATABASE newdb")
	if err != nil {
		// Check if the error is a "database already exists" error
		if pqErr, ok := err.(*pq.Error); ok && pqErr.Code == "42P04" {
			// Database already exists, do nothing
			fmt.Println("Database already exists")
			return nil
		}
		return fmt.Errorf("failed to create database: %v", err)
	}

	fmt.Println("Database created successfully")
	return nil
}
