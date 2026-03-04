from health import take_damage, heal, is_alive
import pytest

# Helper — inline setup for now, replaced with fixtures tomorrow
def make_player(health=100, max_health=100, alive=True):
    return {"health": health, "max_health": max_health, "alive": alive}


# ---- take_damage ----

def test_take_damage_reduces_health():
    player = make_player()
    result = take_damage(player, 30)
    assert result["health"] == 70

def test_take_damage_cannot_go_below_zero():
    player = make_player()
    result = take_damage(player, 999)
    assert result["health"] == 0

def test_take_damage_kills_player_at_zero():
    player = make_player()
    result = take_damage(player, 100)
    assert result["alive"] == False

def test_take_damage_by_zero():
    player = make_player()
    result = take_damage(player, 0)
    assert result["health"] == 100
    assert result["alive"] == True


# ---- heal ----

def test_heal_increases_health():
    player = make_player(health=60)
    result = heal(player, 20)
    assert result["health"] == 80

def test_heal_cannot_exceed_max_health():
    player = make_player(health=90)
    result = heal(player, 50)
    assert result["health"] == 100

def test_heal_does_nothing_when_dead():
    player = make_player(health=0, alive=False)
    result = heal(player, 50)
    assert result["health"] == 0
    assert result["alive"] == False


# ---- is_alive ----

def test_is_alive_returns_true_when_healthy():
    player = make_player()
    assert is_alive(player) == True

def test_is_alive_returns_false_when_dead():
    player = make_player(health=0, alive=False)
    assert is_alive(player) == False

def test_is_alive_returns_false_at_zero_health():
    player = make_player(health=0, alive=False)
    assert is_alive(player) == False

# ---- is_NOT_alive ----


def test_dead_player_cannot_take_damage(dead_player):
    result = take_damage(dead_player, 50)
    assert result["health"] == 0
    assert result["alive"] is False


def test_is_alive_returns_false_for_dead_player_fixture(dead_player):
    assert is_alive(dead_player) is False
