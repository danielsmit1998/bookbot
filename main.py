
def main():
    bookPath = "books/frankenstein.txt"
    text = readBook(bookPath)
    numWords = countWords(text)
    letters = countCharacters(text)
    print(f"--- Begin report of {bookPath} ---")
    print(f"{numWords} words found in the document\n")
    sortedPrint(letters)
    print(f"--- End report ---")
    


def readBook(book):
    with open(book) as f:
        return f.read()

def countWords(text):
    words = text.split()
    return len(words)

def countCharacters(text):
     lowerCase = text.lower()
     letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
     letterDict = dict()

     for letter in letters:
         numLetter = lowerCase.count(letter)
         letterDict[letter] = numLetter

     return letterDict

def sortedPrint(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    
    for key,value in sorted_dict.items():
        print(f"The '{key}' character was found {value} times")


main()