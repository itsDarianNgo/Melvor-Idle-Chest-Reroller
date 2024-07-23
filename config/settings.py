# config/settings.py

import os

from dotenv import load_dotenv

load_dotenv()

# Game settings
GAME_URL = "https://melvoridle.com/"
USERNAME = os.getenv("MELVOR_USERNAME")
PASSWORD = os.getenv("MELVOR_PASSWORD")
CHARACTER_NAME = os.getenv("CHARACTER_NAME")

# Item settings
CHEST_ITEM_ID = "Scroll_of_Terran"
DESIRED_ITEM_ID = "Big_Ron"  # The new desired item name to check for
