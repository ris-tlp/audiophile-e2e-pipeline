CREATE TABLE IF NOT EXISTS Headphone (
    rank_grade varchar(2) NOT NULL,
    value_rating int NOT NULL,
    model varchar(max) NOT NULL PRIMARY KEY,
    price int NOT NULL,
    audio_signature varchar(max) NOT NULL,
    tone_grade varchar(2) NOT NULL,
    technical_grade varchar(2) NOT NULL,
    driver_type varchar(max) NOT NULL,
    fit_cup varchar(max) NOT NULL
);

CREATE TABLE IF NOT EXISTS InEarMonitor (
    rank_grade varchar(2) NOT NULL,
    value_rating int NOT NULL,
    model varchar(max) NOT NULL PRIMARY KEY,
    price int NOT NULL,
    audio_signature varchar(max) NOT NULL,
    tone_grade varchar(2) NOT NULL,
    technical_grade varchar(2) NOT NULL,
    driver_type varchar(max) NOT NULL
);
