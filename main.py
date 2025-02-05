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

def chara_counter(text):
    """Defining a function that reads individual characters in a given
    text, counts them and adds them to a dictionary as individual keys 
    with their respective counts. Returns a dictionary.
    """
    characters = text.lower()
    chara_dict = {}
    for character in characters:
        if character in chara_dict:
            chara_dict[character] += 1
        else:
            chara_dict[character] = 1
    return chara_dict

def chara_sort(chara_count):
    """Defining a function that takes a dictionary specifically structured as 
    alphanumeric:integer entries, removes all keys that are not alphanumeric, saves 
    them as a list of tuples and sorts the list from greatest value to lowest. Returns 
    a list of tuples as alphanumeric,integer entries
    """
    clean_list = []
    for chara in chara_count:
        value = chara_count[chara]
        if chara.isalpha():
            clean_list.append((chara, value))
    def sort_on(item):
        return item[1]
    clean_list.sort(reverse=True, key=sort_on)
    return clean_list

def main():
    """Main function that opens a text using a with block and feeds
    it into the word_count and chara_count functions. The chara_count
    result is fed into the chara_sort function.
    Prints the result.
    """
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count_result = word_count(file_contents)
        chara_count_result = chara_counter(file_contents)
        clean_list_result = chara_sort(chara_count_result)
        print("---Begin Report of Input Text---")
        print(f"{word_count_result} words were found in the document.")
        for result in clean_list_result:
            print(f"The '{result[0]}' character was found {result[1]} times")
        print("---End of report---")

main()