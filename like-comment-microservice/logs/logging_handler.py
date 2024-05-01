import logging.handlers
from venv import logger
import logging

logger.disabled = True

LOG_FILENAME = 'logs/success_logs.log'
ERROR_LOG_FILENAME = 'logs/error_logs.log'

# Set up a specific logger with our desired output level
sql_alchemy_logger = logging.getLogger('sqlalchemy')
sql_alchemy_logger.setLevel(logging.WARNING)

success_logger = logging.getLogger('success_logs')
success_logger.setLevel(logging.DEBUG)

error_logger = logging.getLogger('error_logs')
error_logger.setLevel(logging.ERROR)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=2000000, backupCount=5)

error_handler = logging.handlers.RotatingFileHandler(
              ERROR_LOG_FILENAME, maxBytes=2000000, backupCount=5)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
error_handler.setFormatter(formatter)
sql_alchemy_logger.addHandler(handler)
success_logger.addHandler(handler)
error_logger.addHandler(error_handler)
