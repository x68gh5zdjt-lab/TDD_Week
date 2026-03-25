import pytest
from inventory import add_item, remove_item, get_item_count

def empty_inventory():
    return {"items": [], "capacity": 10, "locked": False}
def full_inventory():
    return {"items": ["a"] * 10, "capacity": 10, "locked": False}
def locked_inventory():
    return {"items": ["sword"], "capacity": 10, "locked": True}

def test_add_item_empty():
    item = "item"
    assert add_item(empty_inventory, item)["items"][0] == item

def test_add_item_full():
    item = "item"
    with pytest.raises(ValueError):
        add_item(full_inventory, item)

def test_add_item_locked():
    item = "item"
    assert item not in add_item(locked_inventory, item)["items"]

def test_remove_item_empty():
    item = "sword"
    with pytest.raises(ValueError):
        remove_item(empty_inventory, item)

def test_remove_item_full():
    item = "a"
    assert len(remove_item(full_inventory, item)["items"]) == 9

def test_remove_item_locked():
    item = "sword"
    assert item in remove_item(locked_inventory, item)["items"]
