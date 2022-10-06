DROP TABLE Headphone;

DROP TABLE InEarMonitor;

CREATE TABLE IF NOT EXISTS Headphone (
    rank_grade varchar(5) NOT NULL,
    value_rating int NOT NULL,
    model varchar(500) NOT NULL PRIMARY KEY,
    price int NOT NULL,
    audio_signature varchar(200) NOT NULL,
    tone_grade varchar(5) NOT NULL,
    technical_grade varchar(5) NOT NULL,
    driver_type varchar(200),
    fit_cup varchar(200)
);

CREATE TABLE IF NOT EXISTS InEarMonitor (
    rank_grade varchar(5) NOT NULL,
    value_rating int NOT NULL,
    model varchar(500) NOT NULL PRIMARY KEY,
    price int NOT NULL,
    audio_signature varchar(200) NOT NULL,
    tone_grade varchar(5) NOT NULL,
    technical_grade varchar(5) NOT NULL,
    driver_type varchar(200)
);
