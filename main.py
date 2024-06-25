def main():
    # Open and read the file contents
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    # Calculate the word count
    word_count_result = word_count(file_contents)
    
    # Get characters dictionary
    chars_dict = character_count(file_contents)
    
    # Convert the characters dictionary to a sorted list of dictionaries
    sorted_chars_list = chars_dict_to_sorted_list(chars_dict)
    
    # Print the report
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count_result} words found in the document")
    print()
    
    # Print each character's count
    for item in sorted_chars_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def character_count(file_contents):
    characters_dict = {}
    lowered_string = file_contents.lower()
    for character in lowered_string:
        if character in characters_dict:
            characters_dict[character] += 1
        else:
            characters_dict[character] = 1
    return characters_dict

def chars_dict_to_sorted_list(num_chars_dict):
    char_list = []
    for char, count in num_chars_dict.items():
        new_dict = {'char': char, 'num': count}
        char_list.append(new_dict)
    char_list.sort(key=lambda x: x['num'], reverse=True)
    return char_list

if __name__ == "__main__":
    main()