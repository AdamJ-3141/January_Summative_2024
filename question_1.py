
def string_pattern(size: int):
    """Create an 'X' pattern of a given size.

    Example with size 5:
        +---+
        -+-+-
        --+--
        -+-+-
        +---+

    Args:
        size: The size of the 'X' to be generated.

    Returns:
        str: A string which looks like an X when printed, lines separated by \n.

    Raises:
        ValueError: The size inputted was less than 3.
    """

    def string_replace(s: str, ind: int, new: str):
        """Replace a character a given string with a new string.

        Args:
            s: String to be changed.
            ind: Index at which the character is changed.
            new: The string to replace the character with.

        Returns:
            str: A new string with the character replaced.
        """
        if ind == -1:  # Because s[ind + 1] would be s[0].
            return s[:ind] + new
        else:
            return s[:ind] + new + s[ind + 1:]

    if size <= 2:
        raise ValueError("Size cannot be less than 3")
    else:
        pattern = ""
        for i in range(size):
            base_str = "-" * size  # Creates a base string of length size
            # Replaces mirroring characters with "+".
            base_str = string_replace(base_str, i, "+")
            base_str = string_replace(base_str, -(i + 1), "+")
            pattern += base_str + "\n"
        return pattern
