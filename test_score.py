import pytest
from score import add_points, apply_multiplier, reset_score, is_high_score


def test_add_points(game):
    result = add_points(game, 10)
    assert result["score"] == 10


def test_add_points_multiplier(game):
    game["multiplier"] = 67
    result = add_points(game, 10)
    assert result["score"] == 670


def test_add_points_inactive(game):
    game["active"] = False
    result = add_points(game, 10)
    assert result["score"] == 0


def test_add_points_rejects_negative(game):
    with pytest.raises(ValueError):
        add_points(game, -5)


def test_apply_multiplier_basic(game):
    result = apply_multiplier(game, 3)
    assert result["multiplier"] == 3


def test_multiplier_rejects_zero(game):
    with pytest.raises(ValueError):
        apply_multiplier(game, 0)


def test_apply_multiplier_inactive_game(game):
    game["active"] = False
    result = apply_multiplier(game, 3)
    assert result["multiplier"] == 1


def test_reset_score(game):
    game["score"] = 50
    game["multiplier"] = 5
    result = reset_score(game)
    assert result["score"] == 0
    assert result["multiplier"] == 1


def test_reset_score_inactive_game(game):
    game["score"] = 100
    game["multiplier"] = 4
    game["active"] = False
    result = reset_score(game)
    assert result["score"] == 0
    assert result["multiplier"] == 1


def test_is_high_score_true(game):
    game["score"] = 100
    assert is_high_score(game, 50) is True


def test_is_high_score_false(game):
    game["score"] = 50
    assert is_high_score(game, 50) is False


def test_is_high_score_invalid_threshold(game):
    with pytest.raises(ValueError):
        is_high_score(game, -10)


