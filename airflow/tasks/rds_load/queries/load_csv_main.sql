CREATE EXTENSION IF NOT EXISTS aws_s3 CASCADE;

SELECT
    aws_s3.table_import_from_s3(
        'Headphone',
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
        'InEarMonitor',
        '',
        '(format csv, header true)',
        '{bucket_name}',
        'iems-silver.csv',
        '{region}',
        '{access_key}',
        '{secret_key}'
    );
