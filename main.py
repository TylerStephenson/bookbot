def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = num_of_words(text)
    characters_dict = count_characters(text)
    print(f"{word_count} words found in the document")
    print(characters_dict)


def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import num_of_words
from stats import count_characters

main()