CREATE TABLE IF NOT EXISTS Headphone (
    Rank_Grade varchar(5) NOT NULL,
    Value_Rating int NOT NULL,
    Model varchar(500) NOT NULL PRIMARY KEY,
    Price int NOT NULL,
    Audio_Signature varchar(200) NOT NULL,
    Tone_Grade varchar(5) NOT NULL,
    Technical_Grade varchar(5) NOT NULL,
    Driver_Type varchar(200),
    Fit_Cup varchar(200)
);

CREATE TABLE IF NOT EXISTS InEarMonitor (
    Rank_Grade varchar(5) NOT NULL,
    Value_Rating int NOT NULL,
    Model varchar(500) NOT NULL PRIMARY KEY,
    Price int NOT NULL,
    Audio_Signature varchar(200) NOT NULL,
    Tone_Grade varchar(5) NOT NULL,
    Technical_Grade varchar(5) NOT NULL,
    Driver_Type varchar(200)
);
