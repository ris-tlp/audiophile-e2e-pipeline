CREATE TABLE IF NOT EXISTS {table_name} (
    id int PRIMARY KEY,
    rank_grade varchar(2) NOT NULL,
    model varchar(50) NOT NULL,
    value_rating int NOT NULL,
    price int NOT NULL,
    audio_signature varchar(50) NOT NULL,
    tone_grade varchar(2) NOT NULL,
    technical_grade varchar(2) NOT NULL,
    driver_type varchar(25) NOT NULL,
    fit_cup varchar(25) NOT NULL
);
