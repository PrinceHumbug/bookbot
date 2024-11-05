def main():
    book_path = "/home/evanh/workspace/github.com/PrinceHumbug/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_characters = count_characters_dict(text)
    character_sorted_list = char_dict_to_sorted_list(num_characters)

    print (f"--- Begin report of {book_path}---")
    print(f"{num_words} found in the document")
    print()

    for item in character_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item[ 'num']} times")

    print("--- End report ---")


    

def count_words(words):
    word_count = words.split()
    return len(word_count) 

def sort_on(d):
   return d["num"]

def char_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def count_characters_dict(text):
    characters = {}
    for c in text:
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

def get_book_text(path):   
    with open(path) as f:
        return f.read()




main()
