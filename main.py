import sys

from stats import chars_dict_to_sorted_list, count_chars, count_words, get_book_report


def main():
    args = sys.argv
    if len(args) != 2:
        print("  Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = args[1]
    book_content = get_book_text(book_path)

    num_words = count_words(book_content)
    char_counts = chars_dict_to_sorted_list(count_chars(book_content))

    msg = get_book_report(
        book_path=book_path, word_count=num_words, char_count_list=char_counts
    )
    print(msg)


def get_book_text(file_path: str):
    with open(file_path) as f:
        book_content = f.read()
        return book_content


main()
