# main.py
import logging
import os
import sys
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from browser_management.browser_init import setup_browser
from browser_management.character_select import select_character
from browser_management.login import login
from browser_management.navigate import navigate_to_homepage
from browser_management.save_game import save_game
from inventory_management.open_chest import open_chest
from inventory_management.inventory_operations import fetch_inventory
from inventory_management.loot_checker import loot_checker
from utils.game_state import check_game_ready
import config.settings as settings


def main():
    logging.basicConfig(level=logging.INFO)
    driver = None
    got_desired_item = (
        False  # Initialize the flag to track if the desired item is found
    )
    try:
        driver = setup_browser()
        navigate_to_homepage(driver, settings.GAME_URL)
        login(driver, settings.USERNAME, settings.PASSWORD)
        select_character(driver, settings.CHARACTER_NAME)

        if check_game_ready(driver):
            logging.info("Game Loaded. Initiating pre-chest opening inventory capture.")
            pre_inventory = fetch_inventory(driver)

            logging.info("Opening the chest.")
            open_chest(driver)

            logging.info("Initiating post-chest opening inventory capture.")
            post_inventory = fetch_inventory(driver)

            added, removed, modified, got_desired_item = loot_checker(
                pre_inventory, post_inventory, settings.DESIRED_ITEM_ID
            )
            logging.info(f"Added items: {added}")

            if got_desired_item:
                logging.info("Desired item obtained! Saving the game configuration.")
                save_game(driver)
                logging.info(
                    "Game saved successfully! Waiting 5 seconds before further action..."
                )
                time.sleep(5)  # 5-second sleep after saving the game
            else:
                logging.info(
                    "Desired item not obtained. Re-rolling by logging out and restarting."
                )
                driver.quit()  # Close the current session
                main()  # Restart the main function to re-initiate the game

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        if (
            driver and not got_desired_item
        ):  # Ensure the driver only closes if needing to re-roll
            logging.info("Closing the game driver.")
            driver.quit()


if __name__ == "__main__":
    main()
