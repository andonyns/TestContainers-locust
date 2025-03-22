import os
import sys
import time
from typing import Any
from testcontainers.core.image import DockerImage
from testcontainers.core.container import DockerContainer
from testcontainers.core.network import Network

from be.db import setup_db

class Main:

    def execute_main(self) -> int:
        
        network = Network().create()
        setup_db.setup(network)
        
        image = DockerImage(path="./fe/", tag="customer-api", clean_up=False)
        container = DockerContainer(str(image))
        container.with_env_file(".env").start().with_network(network)
        logs = container.get_logs()
        print(logs)
        # with open('./container.log', 'w') as f:
        #     f.write(logs)
        print("API ready")
        while True:
            time.sleep(60)
            print("Waiting on manual cancelation")

        return 0


if __name__ == "__main__":
    main = Main()
    sys.exit(main.execute_main())
