from copy import copy, deepcopy


class GameObject:
    """An object in the game of Bazar Bizzare.

    Attributes:
        shape [Read-Only]: String indicating the shape of the object.
        colour [Read-Only]: String indicating the colour of the object.
    """

    def __init__(self, shape: str, colour: str):
        """Initialises the object with shape and colour.

        Args:
            shape: The shape of the object (str).
            colour: The colour of the object (str).
        """
        self._shape = shape
        self._colour = colour

    @property
    def shape(self):
        """str: The shape of the object."""
        return self._shape

    @property
    def colour(self):
        """str: The colour of the object."""
        return self._colour

    def __eq__(self, other):
        if isinstance(other, GameObject):
            # Equal if shape and colour are equal
            return self.shape == other.shape and self.colour == other.colour
        else:
            return False

    def __str__(self):
        # For client-side testing, couldn't read the default output.
        return f"{self.colour} {self.shape}"


class GameCard:
    """A card in the game of Bazar Bizzare, which has two objects on it.

    Attributes:
        content [Read-Only]: List of the two GameObjects on the card.
    """

    def __init__(self, obj1: GameObject, obj2: GameObject):
        """Initialises the GameCard with its two objects.

        Args:
            obj1: The first GameObject on the card.
            obj2: The second GameObject on the card.
        """
        self._content = [copy(obj1), copy(obj2)]

    @property
    def content(self):
        """List[GameObject]: Deepcopy of the two objects on the card."""
        return deepcopy(self._content)

    def __eq__(self, other):
        if isinstance(other, GameCard):
            # Turning into sets because order does not matter.
            self_card_set = {str(self._content[0]), str(self._content[1])}
            other_card_set = {str(other.content[0]), str(other.content[1])}
            return self_card_set == other_card_set
        else:
            return False

    def __str__(self):
        # For client-side testing, couldn't read the default output.
        return ", ".join([str(c) for c in self._content])


class CardDeck:
    """Represents the deck of cards in the game of Bazar Bizzare.

    Attributes:
        objects: List of GameObjects to play with.

    Methods:
        generate_deck(): Generates all possible GameCard objects
                         to put in the deck.
    """

    def __init__(self, objects):
        """Initialises the CardDeck with a list of objects.

        Args:
            objects: List of GameObjects to play with.
        """
        if not 3 <= len(objects) <= 5:  # 3, 4, 5
            raise ValueError(f"Expected 3, 4, or 5 objects, got {len(objects)}")
        # Define protected attributes for use later,
        # sets used to remove duplicates.
        self._shapes = set([obj.shape for obj in objects])
        self._colours = set([obj.colour for obj in objects])
        if not len(self._shapes) == len(self._colours) == len(objects):
            raise ValueError(("At least two objects have "
                              "the same shape or colour."))
        self.objects = objects

    def generate_deck(self) -> list[GameCard]:
        """Generate the full deck of valid cards.

        A card is valid if and only if it allows to pick exactly
        one wooden piece.

        Returns:
            A list of GameCard representing the deck.
        """

        def can_choose(game_card: GameCard, obj: GameObject):
            """Checks whether an object can be chosen from the GameCard.

            If one of the objects on the gamecard is identical, choose the
            corresponding piece. Otherwise, choose the only one that has
            nothing in common with the card: neither shape nor colour.

            This function works for 3 and 4 objects, but not for 5. I somehow
            lose half the cards when checking with 5 objects and I have no
            idea why.

            Args:
                game_card: The relevant GameCard.
                obj: The relevant GameObject to be tested.

            Returns:
                Boolean indicating whether the object can be chosen.
            """
            card_obj0 = game_card.content[0]
            card_obj1 = game_card.content[1]
            if card_obj0 == card_obj1:  # Validates the card itself
                return False
            # If one of the objects on the gamecard is identical
            if obj == card_obj0 or obj == card_obj1:
                return True
            # Otherwise check for nothing in common
            elif (obj.colour not in [card_obj0.colour, card_obj1.colour] and
                  obj.shape not in [card_obj0.shape, card_obj1.shape]):
                return True
            else:
                return False

        objects = []
        # Create all possible objects
        for shape in self._shapes:
            for colour in self._colours:
                objects.append(GameObject(shape, colour))
        deck = []
        # Create cards from objects
        for ind, obj1 in enumerate(objects):
            for obj2 in objects[ind:]:
                card = GameCard(obj1, obj2)
                # Filter those cards based on validity
                objects_chosen = [can_choose(card, o) for o in self.objects]
                if sum([i for i in objects_chosen]) == 1:
                    deck.append(card)
        return deck
