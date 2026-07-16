from loguru import logger
from config.settings import settings

logger.add(
    "logs/tradewiz.log",
    rotation="10 MB",
    retention="7 days",
    level=settings.LOG_LEVEL,
)

log = logger