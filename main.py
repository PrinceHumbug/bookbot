def main():
    book_path = "/home/evanh/workspace/github.com/PrinceHumbug/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_characters = count_characters_dict(text)
    print(f"{num_words} words found in the document, with a total of {num_characters} characters.")

    

def count_words(words):
    word_count = words.split()
    return len(word_count) 

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
