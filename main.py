def main():
    book_path = "/home/evanh/workspace/github.com/PrinceHumbug/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")

    

def count_words(words):
    word_count = words.split()
    return len(word_count) 

def get_book_text(path):   
    with open(path) as f:
        return f.read()




main()
