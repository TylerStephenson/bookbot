def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = num_of_words(text)
    characters_dict = count_characters(text)
    characters_sorted = sort_characters(characters_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in characters_sorted:
        if not item["char"].isalpha():
            continue
        else:
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import num_of_words
from stats import count_characters
from stats import sort_characters

main()