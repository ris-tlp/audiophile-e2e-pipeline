import yaml
import pathlib
from dotenv import dotenv_values

# Load config
configuration_path = pathlib.Path(__file__).parent.parent.resolve()
script_path = pathlib.Path(__file__).parent.resolve()
config = dotenv_values(f"{configuration_path}/configuration.env")

dbt_profile = dict(
    dbt_transform = dict(
        target = "dev",
        outputs = dict(
            dev = dict(
                dbname = config["redshift_database"],
                host = config["redshift_host"].split(":")[0],
                password = config["redshift_password"],
                port = int(config["redshift_port"]),
                schema = "public",
                threads = 1,
                type = "redshift",
                user = config["redshift_user"]
            )
        )
    )
)

with open(f"{script_path}/profiles.yml", "w") as outfile:
    yaml.dump(dbt_profile, outfile, default_flow_style=False)
