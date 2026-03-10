# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(name)s - %(message)s', datefmt='%Y-%b-%d-%a %H:%M:%S')

# logger = logging.getLogger(__name__)
# logger.propagate = False
# logger .info("Hello from log helper")

# logger = logging.getLogger()
# logHandler = logging.StreamHandler()
# formatter = jsonlogger.JsonFormatter()
# logHandler.setFormatter(formatter)
# logger.addHandler(logHandler)

import logging
import logging.config
from pythonjsonlogger import jsonlogger
from logging.handlers import RotatingFileHandler


LOGGING = {
    "version": 1,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            "datefmt": "%Y-%b-%d-%a %H:%M:%S"
        },
        "json": {
            "format": "%(asctime)s %(levelname)s %(name)s %(message)s",
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "datefmt": "%Y-%b-%d-%a %H:%M:%S"
        }

    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "INFO"
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "./log/activity_logger.log",
            "formatter": "standard",
            "level": "INFO"

        },
        "error_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": 10,
            "backupCount": 5,
            "filename": "./log/error.json",
            "formatter": "json",
            "level": "ERROR"
        }

    },
    "loggers": {
        "activity_logger": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False
        },
        "error_logger": {
            "handlers": ["error_file"],
            "level": "ERROR",
            "propagate": False
        }
    }
}

logging.config.dictConfig(LOGGING)
