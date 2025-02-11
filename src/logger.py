import logging
import datetime
import os.path

# Get the current date
current_date = datetime.datetime.now()

# Format the date as a string
date_string = current_date.strftime("%Y-%m-%d")

log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"logs",f"{date_string}-output.log")

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(log_path, encoding='utf-8'),
                        logging.StreamHandler()
                    ])

def info(info:str):
    logging.info(info)

def error(err:str):
    logging.error(err)
