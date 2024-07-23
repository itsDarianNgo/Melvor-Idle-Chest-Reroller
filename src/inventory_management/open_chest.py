import config.settings as settings


def open_chest(driver):
    js_script = """
        try {
            const items = game.bank.itemsByTab[0];
            const itemObject = items.find(item => item.item._localID === arguments[0]);

            if (itemObject && itemObject.item) {
                const quantity = itemObject.quantity;
                game.bank.processItemOpen(itemObject.item, quantity);
                return 'Opened ' + arguments[0];
            } else {
                return "Item '" + arguments[0] + "' not found.";
            }
        } catch (error) {
            return 'Error processing "' + arguments[0] + '": ' + error.message;
        }
    """
    # Passing item from settings to JS
    response = driver.execute_script(js_script, settings.CHEST_ITEM_ID)
    print(response)


# Example usage with a properly initialized `driver`:
# open_chest(driver)
