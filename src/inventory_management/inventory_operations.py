import json


def fetch_inventory(driver):
    """
    Fetches the current inventory from the game using JavaScript execution in Selenium.
    Returns a list of dictionaries containing the details of each item in the inventory.
    """
    inventory_js = """
        let allItems = [];
        game.bank.items.forEach((value, key) => {
            if (key && value) {
                allItems.push({
                    id: key._localID || 'undefined',
                    name: key._name || 'Unknown Item',
                    quantity: value.quantity || 0
                });
            }
        });
        return JSON.stringify(allItems);  // Convert to JSON string to handle data
    """
    inventory_state_json = driver.execute_script(inventory_js)
    inventory_state = json.loads(
        inventory_state_json
    )  # parse the JSON to a Python list
    return inventory_state
