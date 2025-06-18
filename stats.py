def chars_dict_to_sorted_list(chars: dict):
    """
    Takes the char counts dict from count_chars() and returns a sorted list.

    Args:
        chars: A dictionary with char count {"char": count}

    Returns:
        Sorted list of char dict {"char": char, "num": count}
    """
    def sort_on(dict):
        return dict["num"]

    list_chars = [{"char": k, "num": v} for k, v in chars.items()]
    list_chars.sort(reverse=True, key=sort_on)
    return list_chars


def get_book_report(book_path: str, word_count: int, char_count_list: list) -> str:
    """
    Generates a report string with the total word count and a sorted list of characters and their count.
    """
    report = "============ BOOKBOT ============\n"
    report += f"Analyzing book found at {book_path[2:]}...\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {word_count} total words\n"
    report += "--------- Character Count -------\n"
    for char in char_count_list:
        if char["char"].isalpha():
            report += f"{char['char']}: {char['num']}\n"
    report += "============= END ==============="

    return report


def count_words(text: str) -> int:
    """
    Counts the number of words in a given text.

    Args:
        text: The string to count words from.

    Returns:
        The word count found in the text.
    """
    return len(text.split())


def count_chars(text: str) -> dict:
    """
    Counts the number of times a character appears in the given text.

    Args:
        text: The string to iterate through.

    Returns:
        A dictionary with the count of each character.
            {
                "char": count
            }
    """
    char_counts = {}

    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
