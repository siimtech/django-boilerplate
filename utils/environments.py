import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def load_env(key):
    return os.getenv(key, default="")
