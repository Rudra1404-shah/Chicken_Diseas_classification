import os
import sys
import logging
logging_str=['%(asctime)s : %(levelname)s : %(module)s : %(message)s']
logs_dir='logs'
log_file=os.path.join(logs_dir,'running_logs.log')
os.makedirs(logs_dir,exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format=logging_str[0],
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)
logger=logging.getLogger('cnnClassifier')
