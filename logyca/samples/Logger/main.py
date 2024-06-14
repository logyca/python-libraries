from logyca import Logger
import os

CURRENT_ROOT_FOLDER=os.path.join(os.path.dirname(__file__),"logs")

# Default parameters
logger = Logger(log_dir=CURRENT_ROOT_FOLDER)

# Custom parameters
# logger = Logger(log_dir=CURRENT_ROOT_FOLDER,log_file_name="App_Test", is_enabled=os.getenv("logs_enabled",True), backup_count=7)

from ms1.main import main_run as run1
from ms2.main import main_run as run2

if __name__ == "__main__":
    logger.info("startup")
    run1()
    run2()
