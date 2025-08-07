from loguru import logger

# Configure log file
logger.add("logs/app.log", rotation="1 MB", level="DEBUG")

def get_logger():
    return logger