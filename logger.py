import logging

logging.basicConfig(
    filename="api.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_request(method, path):
    logging.info(f"{method} request to {path}")
