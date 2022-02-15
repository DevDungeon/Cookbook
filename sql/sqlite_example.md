# SQLite notes


```sql
/* Example
 Sqlite commands */

-- Common commands
.help
.open my.db
.tables
SELECT name FROM sqlite_master;
-- Save as ...
.backup myfile.db


CREATE TABLE IF NOT EXISTS images(path TEXT, thumbs_up INT);


CREATE TABLE my_table (
    some_int INT,
    some_text TEXT,
    some_float REAL,
    some_blob BLOB,
    CONSTRAINT enforce_unique_numbers UNIQUE (some_int, some_float)
);

DROP TABLE mytable;

-- Rename table
ALTER TABLE mytable RENAME to mynewtable;
-- Add a column
ALTER TABLE ADD COLUMN username TEXT;

SELECT * FROM mytable;
SELECT field1, field2 FROM mytable;
SELECT COUNT(*) FROM mytable;
SELECT * FROM mytable ORDER BY create_date DESC;
-- The % means match zero or more characters, and the _ means match up to a single character.
SELECT FROM images WHERE path LIKE '%.png';
SELECT FROM images WHERE path LIKE '%.jp_g';
SELECT FROM images WHERE path like '%dog%'

INSERT INTO images (path, thumbs_up) VALUES ("image1.png", 0);


UPDATE images SET thumbs_up=5 WHERE path="image1.png";
# To set multiple fields at once:
UPDATE images SET thumbs_up=10, description="an image" WHERE path="image1.png";


DELETE FROM images WHERE path="image1.png";


/*
 Indexing
 */

CREATE INDEX image_path_index ON images (path);
CREATE INDEX IF NOT EXISTS image_path_index ON images (path);
CREATE UNIQUE INDEX unique_image_path_index ON images (path);

DROP INDEX image_path_index;
DROP INDEX [IF EXISTS] image_path_index;

/**
Transactions
*/
BEGIN TRANSACTION;
-- Perform whatever actions you want now.

-- Undo anything done since `BEGIN` and end transaction
ROLLBACK TRANSACTION;

-- Save changes done since `BEGIN` to the database and end transaction
COMMIT TRANSACTION;


/*Null fields */
CREATE TABLE users (
    id INT,
    profile_id INT NOT NULL
);

/* Default values */
CREATE TABLE users (
    id INT,
    profile_id INT DEFAULT NULL
);

/**
Primary and Foreign Keys

Foreign keys will require a valid value or it won't accept the entry. You can optionally add an ON UPDATE clause that will specify what to do if the referenced foreign object is deleted. You can choose from the following:

    NO ACTION - Do nothing
    RESTRICT - Do not allow deleting when foreign key reference exists
    SET NULL - Set to null
    SET DEFAULT - Use the fields default value
    CASCADE - Delete the foreign reference too
*/
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    profile_id INT,
    FOREIGN KEY(profile_id) REFERENCES profiles(id)
);
CREATE TABLE profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    bio TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id) ON UPDATE CASCADE
);
CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    content TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
CREATE TABLE clans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);
CREATE TABLE clans_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    clan_id INT,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(clan_id) REFERENCES clans(id)
);

/** Autoincrement */
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
```