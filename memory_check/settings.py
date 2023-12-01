import logging.config

logging_conf = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "mem_console": {"format": "{asctime} - {name} - {levelname} - {message}%", "style": "{"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "mem_console",
        },
    },
    "loggers": {
        "mem_logger": {
            "level": "DEBUG",
            "handlers": ["console"],
        },
    },
}


logging.config.dictConfig(logging_conf)
logger = logging.getLogger("mem_logger")
