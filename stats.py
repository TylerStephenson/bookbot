def num_of_words(text):
    return len(text.split())

def count_characters(text):
    lower_case = text.lower()
    characters_dict = {}
    for character in lower_case:
        if character in characters_dict:
            characters_dict[character] += 1
        else:
            characters_dict[character] = 1
    return characters_dict

def sort_on(items):
    return items["num"]

def sort_characters(dictionary):
    char_list = []
    for char , num in dictionary.items():
        new_dict = {"char": char, "num": num}
        char_list.append(new_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list