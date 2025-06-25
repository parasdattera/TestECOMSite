from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../.env")

URL = os.getenv("URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
INVALID_PASSWORD = os.getenv("INVALID_PASSWORD") 

