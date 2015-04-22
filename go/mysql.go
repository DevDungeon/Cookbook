package main



import (
	//"fmt"
	_	"github.com/go-sql-driver/mysql"
	"database/sql"
	"log"
	"fmt"
)



func main() {

	// Establish mysql connection
	var db *sql.DB
	var err error
	db, err = sql.Open("mysql", "user:pass@tcp(127.0.0.1:3306)/db_name")
	if err != nil {
		log.Println(err)
	}
	defer db.Close()

	// Single query
	var str string
	str = singleQuery(db)
	fmt.Println(str)

	// Another query - multiple rows
	var rows *sql.Rows
	rows = query(db)
	printRows(rows)
	rows.Close()

	// Insert statement
	//stmt, err := db.Prepare("INSERT INTO users(username, password) VALUES(?, ?)")
	//if err != nil {	log.Fatal(err) }
	//_, err = stmt.Exec("myuser", "mypass")
	//if err != nil {	log.Fatal(err) }

}



// Perform a one-shot single row query
func singleQuery(db *sql.DB) string {
	var str string
	q := "SELECT username FROM users"
	err := db.QueryRow(q).Scan(&str)
	if err != nil {
		log.Fatal(err)
	}
	return str
}



// Multiple row query
func query(db *sql.DB) *sql.Rows {
	q := "SELECT id, username FROM users"
	rows, err := db.Query(q)
	if err != nil {
		log.Fatal(err)
	}
	return rows
}



// Print a set of MySQL rows returned from a query
func printRows(rows *sql.Rows) string {

	// Iterate rows and print fields
	var id int
	var str, output string
	for rows.Next() {
		err := rows.Scan(&id, &str)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(id)
		fmt.Println(str)
	}

	// Check errors
	err := rows.Err()
	if err != nil {
		rows.Close()
		log.Fatal(err)
	}

	return output
}