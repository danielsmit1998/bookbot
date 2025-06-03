import string

def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def count_words(filepath):

    text = get_book_text(filepath)
    numWords = len(text.split())
    return numWords

def count_letters(filepath):

    text = get_book_text(filepath)

    letters = dict()

    for i in list(string.ascii_lowercase):
        letters[i] = text.lower().count(i)

    return letters

def create_report(filepath):

    sorted_by_value = dict(sorted(count_letters(filepath).items(), key=lambda item: item[1], reverse=True))
    countWords = count_words(filepath)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {countWords} total words")
    print("--------- Character Count -------")

    for key, value in sorted_by_value.items():
        print(f"{key}: {value}")

    print("============ END ============")
