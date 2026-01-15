import logging
from tenacity import retry, stop_after_attempt, wait_fixed

def setup_logging(log_file, level=logging.INFO):
    logging.basicConfig(
        filename=log_file,
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def retryable():
    return retry(
        stop=stop_after_attempt(3),
        wait=wait_fixed(5)
    )