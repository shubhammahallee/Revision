import logging
import os
from datetime import datetime

# Create logs directory if not exists 
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Logs")
os.makedirs(log_dir, exist_ok=True)

# Log file name with timestamp
log_file = os.path.join(log_dir, f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

# Configure logger
logging.basicConfig(
    filename=log_file,
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger()
