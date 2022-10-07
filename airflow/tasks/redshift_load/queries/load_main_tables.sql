BEGIN TRANSACTION;

-- Delete rows through inner join
DELETE FROM
    InEarMonitor USING InEarMonitor_Temp
WHERE
    InEarMonitor.Model = InEarMonitor_Temp.Model;

DELETE FROM
    Headphone USING Headphone_Temp
WHERE
    Headphone.Model = Headphone_Temp.Model;

-- Move data from staging table to main tables
INSERT INTO
    InEarMonitor
SELECT
    *
FROM
    InEarMonitor_Temp;

INSERT INTO
    Headphone
SELECT
    *
FROM
    Headphone_Temp;

END TRANSACTION;

-- Drop staging tables
DROP TABLE InEarMonitor_Temp;

DROP TABLE Headphone_Temp;
