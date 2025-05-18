-- lib/create.sql
DROP TABLE IF EXISTS bears;

CREATE TABLE bears (
    id           INTEGER PRIMARY KEY,
    name         TEXT,
    age          INTEGER,
    sex          TEXT,
    color        TEXT,
    temperament  TEXT,
    alive        INTEGER  -- 0 = false, 1 = true
);
