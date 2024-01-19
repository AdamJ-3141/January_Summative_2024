
def shrink(signal: list[0 | 1], element: list[0 | 1]) -> list[0 | 1]:
    """Shrink the foreground of a binary one-dimensional signal using the
    structuring element.

    Args:
        signal: A list composed of 1s and 0s to be shrunk.
        element: The structuring element used to shrink.

    Returns:
        A new list representing the shrunk signal.
    """
    new_signal = []
    for i in range(len(signal)):
        out = 1
        # Checks all overlaps, enumerate creates (index, value) tuples.
        for ind, j in enumerate(element):
            try:
                # If the overlapping region is not all 1s
                if not (signal[ind + i] == j == 1):
                    out = 0
                    break
            except IndexError:  # Structuring element extends past the signal.
                break
        new_signal.append(out)
    return new_signal


def expand(signal: list[0 | 1], element: list[0 | 1]) -> list[0 | 1]:
    """Expand the foreground of a binary one-dimensional signal using the
    structuring element.

    Args:
        signal: A list composed of 1s and 0s to be expanded.
        element: The structuring element used to expand.

    Returns:
        A new list representing the expanded signal.
    """
    new_signal = []
    for i in range(len(signal)):
        out = 0
        # Checks all overlaps, enumerate creates (index, value) tuples.
        for ind, j in enumerate(element):
            try:
                # If any of the overlapping region is 1
                if signal[ind + i] == j == 1:
                    out = 1
            except IndexError:  # Structuring element extends past the signal.
                break
        new_signal.append(out)
    return new_signal


def denoise(signal: list[0 | 1], element: list[0 | 1]) -> list[0 | 1]:
    """Denoise the foreground of a binary one-dimensional signal using the
    structuring element, by shrinking and expanding it.

    Args:
        signal: A list composed of 1s and 0s to be denoised.
        element: The structuring element used to denoise.

    Returns:
        A new list representing the denoised signal.
    """
    return expand(shrink(signal, element), element)
