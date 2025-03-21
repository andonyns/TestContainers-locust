import os
import sys
from typing import Any

from be.run_db import RunDB
from fe.api import app, setup

class Main:

    def run(self) -> int:
        
        db = RunDB()
        db.run()
        # setup()
        # app.run()

        return 0


if __name__ == "__main__":
    main = Main()
    sys.exit(main.run())
