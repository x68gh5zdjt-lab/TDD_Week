def add_item(inventory, item):
    inv = inventory()
    if inv["locked"]:
        return inv
    if len(inv["items"]) == inv["capacity"]:
        raise ValueError
    if item == "":
        raise ValueError
    inv["items"].append(item)
    return inv

def remove_item(inventory, item):
    inv = inventory()
    if item not in inv["items"]:
        raise ValueError
    if inv["locked"]:
        return inv
    inv["items"].remove(item)
    return inv


def get_item_count(inventory):
    pass
