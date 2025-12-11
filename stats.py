def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_characters(text):
    character_count={}
    for char in text.lower():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort_on(d):
    return d["num"]

def sort_dictionary(d):
    dict_list=[]
    for key in d:
        dict_list.append({'char': key, 'num': d[key]})
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list