
def longest_palindromic_numbers(number: str) -> set[str]:
    """Find the set of the longest palindromic numbers within the given number.

    Args:
        number: The number to find the palindromes within (string)

    Returns:
        A set of the longest palindromes within the number.
    """

    def find_palindromes(n: str) -> set[str]:
        """Recursively find all palindromes within the number string given,
        without filtering.

        Args:
            n: The number to find the palindromes within (string)

        Returns:
            A set of all palindromes within the number.
        """
        if n == n[::-1]:  # If the number is the same as its reverse.
            return {n}
        else:
            # Re-run without first and last digit, then combine.
            without_first = find_palindromes(n[1:])
            without_last = find_palindromes(n[:-1])
            return without_last.union(without_first)

    number = number.strip("0")  # Strip leading zeros, does not change answer.
    # Find palindromes in the number
    palindromes = find_palindromes(number)
    # Find the maximum length of the numbers in the set that don't start with 0.
    longest = max([len(p) for p in palindromes if not p.startswith("0")])
    copyset = palindromes.copy()
    # Remove the palindromes that start with 0 or are shorter than the longest.
    for p in copyset:
        if len(p) < longest or p.startswith("0"):
            palindromes.remove(p)

    return palindromes
