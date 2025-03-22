import os

from testcontainers.postgres import PostgresContainer
from testcontainers.core.network import Network

postgres = PostgresContainer("postgres:16-alpine")


def setup(network: Network):
    print("Setting up DB")
    postgres.start().with_network(network)
    os.environ["DB_CONN"] = postgres.get_connection_url()
    os.environ["DB_HOST"] = postgres.get_container_host_ip()
    os.environ["DB_PORT"] = postgres.get_exposed_port(5432)
    print(os.environ["DB_PORT"])
    os.environ["DB_USERNAME"] = postgres.username
    os.environ["DB_PASSWORD"] = postgres.password
    os.environ["DB_NAME"] = postgres.dbname

    with open('.env', 'w') as f:
        f.write(f"DB_CONN={os.environ["DB_CONN"]}\n")
        f.write(f"DB_HOST={os.environ["DB_HOST"]}\n")
        f.write(f"DB_PORT={os.environ["DB_PORT"]}\n")
        f.write(f"DB_USERNAME={os.environ["DB_USERNAME"]}\n")
        f.write(f"DB_PASSWORD={os.environ["DB_PASSWORD"]}\n")
        f.write(f"DB_NAME={os.environ["DB_NAME"]}\n")
