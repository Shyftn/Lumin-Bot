import random

def roll_dice(dice: str):
    """
    Roll a dice in NdN format.
    """
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        # The input was not in the correct format
        return "Format has to be in NdN!"

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))

    return result
