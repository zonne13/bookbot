from stats import count_words, get_num_times_per_char


def main():
    book_path = "./books/frankenstein.txt"
    book_content = get_book_text(book_path)

    num_words = count_words(book_content)
    char_counts = get_num_times_per_char(book_content)

    msg = f"{num_words} words found in the document"
    print(msg)
    print(char_counts)


def get_book_text(file_path: str):
    with open(file_path) as f:
        book_content = f.read()
        return book_content


main()
