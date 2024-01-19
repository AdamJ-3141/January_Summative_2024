
def trick_score(trick: set[tuple], trump_suit: str):
    """Return the score of a trick using the values of each card,
    given a trump suit.

    Args:
        trick: A set of 4 valid card tuples (rank, suit).
        trump_suit: A string "Hearts", "Clubs", "Diamonds", or "Spades".

    Returns:
        An integer which is the score of the trick.

    Raises:
        TypeError: Trump suit was not a valid suit.
        ValueError: Trick is not composed of exactly 4 valid cards.
    """
    suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
    ranking = {  # Rank: (Not-Trump score, Trump score)
        "Ace": (11, 11),
        "King": (4, 4),
        "Queen": (3, 3),
        "Jack": (2, 20),
        "10": (10, 10),
        "9": (0, 14),
        "8": (0, 0),
        "7": (0, 0)
    }

    # Validating Input
    if trump_suit not in suits:
        raise TypeError("Trump suit is not a valid suit.")
    if len(trick) != 4:
        raise ValueError("Trick is not composed of 4 cards.")
    score = 0
    for card in trick:
        try:
            rank, suit = card
            # Checks keys of ranking dictionary, and checks the card suit
            if rank not in ranking or suit not in suits:
                raise ValueError
        except ValueError:
            raise ValueError(f"Invalid Card: {card}")
        else:
            # Adds to the score depending on whether card is trump
            trump = int(suit == trump_suit)  # 0 or 1
            score += ranking[rank][trump]
    return score
