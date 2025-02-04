def word_count(text):
    """Defining a function that splits a given text into individual
    words and counts them by using an iterator and counter.
    Has flexibility for extending for exclusion/inclusion of word types.
    Returns an integer.
    """
    words = text.split()
    word_counter = 0
    for word in words:
        word_counter += 1
    return word_counter


def main():
    """Main function that opens a text using a with block and feeds
    it into the word_count function.
    Prints the result.
    """
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count_result = word_count(file_contents)
        print(word_count_result)

main()