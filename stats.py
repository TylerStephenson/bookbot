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