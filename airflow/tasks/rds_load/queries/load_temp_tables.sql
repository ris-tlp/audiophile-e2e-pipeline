CREATE EXTENSION IF NOT EXISTS aws_s3 CASCADE;

CREATE TEMP TABLE Headphone_temp (LIKE Headphone);

CREATE TEMP TABLE InEarMonitor_temp (LIKE InEarMonitor);

SELECT
    aws_s3.table_import_from_s3(
        'Headphone_temp',
        '',
        '(format csv, header true)',
        '{bucket_name}',
        'headphones-silver.csv',
        '{region}',
        '{access_key}',
        '{secret_key}'
    );

SELECT
    aws_s3.table_import_from_s3(
        'InEarMonitor_temp',
        '',
        '(format csv, header true)',
        '{bucket_name}',
        'iems-silver.csv',
        '{region}',
        '{access_key}',
        '{secret_key}'
    );
