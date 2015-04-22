// This sqlite example was taken from mattn's gist
// https://gist.github.com/mattn/11454630

package main

import (
	"database/sql"
	_ "github.com/mattn/go-sqlite3"
	"log"
)

func main() {
	db, err := sql.Open("sqlite3", "file:foo.db?cache=shared")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	rows, err := db.Query("select id, value from foo")
	if err != nil {
		log.Fatal(err)
	}
	defer rows.Close()

	for rows.Next() {
		var id int
		var value string

		err = rows.Scan(&id, &value)
		if err != nil {
			log.Fatal(err)
		}

		_, err = db.Exec("insert into bar(id, value) values(?, ?)", id, value)
		if err != nil {
			log.Fatal(err)
		}
	}
}
