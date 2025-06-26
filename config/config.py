import os
from dotenv import load_dotenv
from pathlib import Path

# load the env file variable from .env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# variables read from env
URL: str = os.getenv("URL", "https://www.saucedemo.com/")
USERNAME: str = os.getenv("USERNAME", "standard_user")
PASSWORD: str = os.getenv("PASSWORD", "secret_sauce")
INVALID_PASSWORD: str = os.getenv("INVALID_PASSWORD", "wrong_password")

# raising exception if missing!
required_vars = {"URL": URL, "USERNAME": USERNAME, "PASSWORD": PASSWORD}
missing = [key for key, value in required_vars.items() if not value]
if missing:
    raise EnvironmentError(f"Missing required environment variables: {', '.join(missing)}")
