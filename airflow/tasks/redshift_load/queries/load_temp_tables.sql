CREATE TEMP TABLE InEarMonitor_temp (LIKE InEarMonitor);

CREATE TEMP TABLE Headphone_temp (LIKE Headphone);

-- Load CSV contents in temporary tables
COPY InEarMonitor_temp
FROM
    's3://{bucket_name}/iems-silver.csv' CREDENTIALS 'aws_access_key_id={aws_access_id};aws_secret_access_key={aws_secret_key}' IGNOREHEADER 1 DELIMITER ',' CSV;

COPY Headphone_temp
FROM
    's3://{bucket_name}/headphones-silver.csv' CREDENTIALS 'aws_access_key_id={aws_access_id};aws_secret_access_key={aws_secret_key}' IGNOREHEADER 1 DELIMITER ',' CSV;
