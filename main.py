import sys
from stats import get_num_words, get_letter_distribution, get_sorted_dict_list

def get_books_test(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = args[1]
    books = get_books_test(path)
    num_words = get_num_words(books)
    dist = get_letter_distribution(books)
    sorted_list = get_sorted_dict_list(dist)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")
main()
