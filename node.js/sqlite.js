// npm install sqlite3
const sqlite3 = require('sqlite3');

const db = new sqlite3.Database('mydb.sqlite3');

db.serialize(function() {
  db.run("CREATE TABLE IF NOT EXISTS posts (title TEXT, content TEXT)");
 
  var stmt = db.prepare("INSERT INTO posts VALUES (?, ?)");
  stmt.run("test title", "test content");
  stmt.finalize();
 
  db.each("SELECT rowid, title, content FROM posts", (err, row) => {
      console.log(`${row.rowid}: ${row.title} - ${row.content}`);
  });
});

db.close();
