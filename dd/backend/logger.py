from loguru import logger


def configure_logger() -> None:
    logger.remove()  # Remove the default logger
    logger.add("logs/app.log", rotation="1 MB", level="INFO", backtrace=True, diagnose=True)
