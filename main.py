from stats import count_words
from stats import count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        return book_text
    
def main():
    contents = get_book_text("./books/frankenstein.txt")
    contents_count = count_words(contents)
    characters_count = count_characters(contents)
    print (f"Found {contents_count} total words")
    print (characters_count)
main()