def loot_checker(pre_inventory, post_inventory, desired_item_id):
    pre_dict = {item["id"]: item for item in pre_inventory}
    post_dict = {item["id"]: item for item in post_inventory}

    added_items = []
    removed_items = []
    modified_items = []
    got_desired_item = False

    for item_id in post_dict:
        if item_id not in pre_dict:
            added_items.append(post_dict[item_id])
            if item_id == desired_item_id:
                got_desired_item = True
        elif post_dict[item_id]["quantity"] != pre_dict[item_id]["quantity"]:
            modified_items.append(
                {
                    "id": item_id,
                    "name": post_dict[item_id]["name"],
                    "quantity_change": post_dict[item_id]["quantity"]
                    - pre_dict[item_id]["quantity"],
                }
            )

    for item_id in pre_dict:
        if item_id not in post_dict:
            removed_items.append(pre_dict[item_id])

    return added_items, removed_items, modified_items, got_desired_item
