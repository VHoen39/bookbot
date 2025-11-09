from stats import count_words
from stats import count_characters
from stats import sorted_count_characters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        return book_text
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    contents = get_book_text(path_to_book)
    contents_count = count_words(contents)
    characters_count = count_characters(contents)
    sorted = sorted_count_characters(characters_count)

    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {path_to_book}...")
    print ("----------- Word Count ----------")
    print (f"Found {contents_count} total words")
    print ("--------- Character Count -------")
    for i in sorted:
        if i["char"].isalpha():
            text = i["char"] + ": " + str(i["num"])
            print (text)
    print ("============= END ===============")
main()