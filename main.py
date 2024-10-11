
def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    letters = [char for char in text if char.isalpha()]
    return len(letters)

def get_char_frequency(text):
    text = text.lower()
    char_frequency = {}

    for char in text:
        if char.isalpha():
            if char in char_frequency:
                char_frequency[char] +=1
            else:
                char_frequency[char] = 1
    return char_frequency

def sort_by_frequency(char_frequency):
    sorted_chars = sorted(char_frequency.items(), key=lambda item: item[1], reverse=True)
    return sorted_chars

def print_report(path_to_file, word_count, sorted_chars):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document\n")
    
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")


if __name__ == "__main__":
    path_to_file = "books/frankenstein.txt"
    file_contents = main()
    
    
    word_count = get_word_count(file_contents)
    print(f"Word count: {word_count}")

    letter_count = get_letter_count(file_contents)
    print(f"Letter count: {letter_count}")

    char_frequency = get_char_frequency(file_contents)
    print(f"Character frequency: {char_frequency}")

    word_count = get_word_count(file_contents)
    char_frequency = get_char_frequency(file_contents)
    sorted_chars = sort_by_frequency(char_frequency)

    print_report(path_to_file, word_count, sorted_chars)
