import os
import sys
import time

from db.setup_db import Setup_DB

def run() -> int:
    Setup_DB()
    print("DB Ready")
    
    param = sys.argv[1] if len(sys.argv) > 1 else ""

    if param == "persist":
        while True:
            time.sleep(60)
            print("Waiting on manual cancelation")


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("Script stopped by user")
