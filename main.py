import sys
from stats import get_word_count
from stats import get_char_count
from stats import sort_dict

def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    file_path = sys.argv[1]
    print(f"Analyzing book found at {file_path}...")
    #file_path = "./books/frankenstein.txt"
    text = get_book_text(file_path)
    print("----------- Word Count ----------")
    num_words = get_word_count(text)
    print(f"Found {num_words} total words")
    char_dict = get_char_count(text)
    print("--------- Character Count -------")
    for result in sort_dict(char_dict):
        if result["char"].isalpha():
            print(result["char"] + ": " + str(result["num"]))
    print("============= END ===============")

def usage():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

usage()
main()