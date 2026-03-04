import pytest

@pytest.fixture
def player():
    return {"health": 100, "max_health": 100, "alive": True}

@pytest.fixture
def new_game():
    return {"score": 0, "level": 1, "active": True}

@pytest.fixture
def dead_player():
    return {"health": 0, "alive": False}
