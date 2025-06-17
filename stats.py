def count_words(text: str) -> int:
    """
    Counts the number of words in a given text.

    Args:
        text: The string to count words from.
    """
    return len(text.split())


def get_num_times_per_char(text: str) -> dict:
    """
    Counts the number of times a character appears in the given text.

    Args:
        text: The string to iterate through.

    Returns:
        A dictionary with the count of each character.
    """
    char_counts = {}

    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
