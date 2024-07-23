from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def save_game(driver):
    try:
        # Locate the Force Save button using the provided XPath and click it
        force_save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/div[13]/main/header/div/div[2]/button[1]/lang-string",
                )
            )
        )
        force_save_button.click()
        print("Game saved successfully!")

    except Exception as e:
        print(f"An error occurred while trying to save the game: {str(e)}")
