from stats import number_of_words, number_of_characters, sort_dictionary
import sys

def get_book_text(path):
    with open(path) as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = number_of_words(book_text)
    character_counts = number_of_characters(book_text)
    sorted_dictionary = sort_dictionary(character_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count --------")
    for item in sorted_dictionary:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()