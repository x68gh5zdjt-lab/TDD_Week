def add_points(game, amount):
    if amount <= 0:
        raise ValueError("amount must be positive")

    if not game["active"]:
        return game
    
    game["score"] += amount * game["multiplier"]
    return game


def apply_multiplier(game, multiplier):
    if multiplier < 1:
        raise ValueError("multiplier must be >= 1")

    if not game["active"]:
        return game

    game["multiplier"] = multiplier
    return game


def reset_score(game):
    game["score"] = 0
    game["multiplier"] = 1
    return game


def is_high_score(game, threshold):
    if threshold < 0:
        raise ValueError("threshold must be >= 0")

    return game["score"] > threshold
