def add_points(game, amount):
    if amount <= 0:
        raise ValueError
    results = game()
    if not results["active"]:
        return results
    results["score"] += amount * results["multiplier"]
    return results


def apply_multiplier(game, multiplier):
    if multiplier < 1:
        raise ValueError
    results = game()
    if not results["active"]:
        return results
    results["multiplier"] = multiplier
    return results


def reset_score(game):
    results = game()
    results["score"] = 0
    results["multiplier"] = 1
    return results


def is_high_score(game, threshold):
    if threshold < 0:
        raise ValueError
    results = game()
    return results["score"] > threshold
