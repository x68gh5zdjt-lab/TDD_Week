from score import add_points, apply_multiplier, reset_score, is_high_score


def game():
    return {"score": 0, "multiplier": 1, "active": True}


def test_add_points():
    assert add_points(game, 1)["score"] == 1


def test_apply_multiplier():
    assert apply_multiplier(game, 2)["multiplier"] == 2


def test_reset_score():
    assert reset_score(game)["score"] == 0
    assert reset_score(game)["multiplier"] == 1


def test_is_high_score():
    assert is_high_score(game, 20) is False
