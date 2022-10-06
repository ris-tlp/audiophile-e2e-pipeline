BEGIN TRANSACTION;

-- Delete rows through inner join
DELETE FROM
    InEarMonitor USING InEarMonitor_temp
WHERE
    InEarMonitor.model = InEarMonitor_temp.model;

DELETE FROM
    Headphone USING Headphone_temp
WHERE
    Headphone.model = Headphone_temp.model;

-- Move data from staging table to main tables
INSERT INTO
    InEarMonitor
SELECT
    *
FROM
    InEarMonitor_temp;

INSERT INTO
    Headphone
SELECT
    *
FROM
    Headphone_temp;

END TRANSACTION;

-- Drop staging tables
DROP TABLE InEarMonitor_temp;

DROP TABLE Headphone_temp;
