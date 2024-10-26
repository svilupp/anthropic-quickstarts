import os
import sys
from pathlib import Path

from loguru import logger

# Remove any existing default handlers
logger.remove()

# Create logs directory if it doesn't exist
path_logs = Path(__file__).resolve().parent.parent / "logs"
path_logs.mkdir(exist_ok=True)

# Add console handler with colored output
logger.add(
    sys.stdout,
    format="{time:YYYY-MM-DD HH:mm:ss} | {name}:{function}:{line} | {message}",
    level="INFO",
)

# Add file handler for all logs
logger.add(
    path_logs / "app.log",
    rotation="10 MB",  # Create new file after 10MB
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} | {message}",
    level="DEBUG",
    encoding="utf-8",
)

width = int(os.getenv("WIDTH") or 0)
height = int(os.getenv("HEIGHT") or 0)
logger.info(f"SETTINGS> Screen dimensions: {width}x{height}")
display_num = None
if (display_num_env := os.getenv("DISPLAY_NUM")) is not None:
    display_num = int(display_num_env)
    logger.info(f"SETTINGS> Display number: {display_num}")
