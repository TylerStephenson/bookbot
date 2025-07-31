def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = num_of_words(text)
    
    print(f"{word_count} words found in the document")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def num_of_words(words):
    return len(words.split())

main()