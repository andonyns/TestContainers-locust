import os
import sys
import time

from be.db.setup_db import Setup_DB

def run() -> int:
    Setup_DB()
    print("DB Ready")
    
    # while True:
    #     time.sleep(60)
    #     print("Waiting on manual cancelation")


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("Script stopped by user")
