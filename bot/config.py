import os
from dotenv_vault import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

