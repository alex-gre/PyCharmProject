PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users (uid integer primary key autoincrement, name text, addres text,phone text);
INSERT INTO "users" VALUES(1,'Alex Many','Texas','_793556346');
INSERT INTO "users" VALUES(2,'Andry Hadson','London','_792323222322');
INSERT INTO "users" VALUES(3,'Bill Joy','California','+792343433433');
INSERT INTO "users" VALUES(4,'Deny Duron','New York','_79234343434');
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('users',4);
COMMIT;
