STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

import string


def print_word_freq(file):
    """Read in 'file' and print out the frequency of words in that file"""
    with open(file) as text_file:
        lines = text_file.read()
        lines = string_format(lines)
        """remove STOP_WORDS from lines"""
        lines = [word for word in lines if word not in STOP_WORDS]
        lines = count_words(lines)
        lines = sorted(lines.items(), key=lambda item: item[1], reverse=True)
        display_words(lines)
        #print(lines)


def string_format(input_string):
    """Format each line read in to be processed in the count"""
    input_string = input_string.replace("-", " ")
    input_string = input_string.replace("—", " ")
    input_string = input_string.replace("\n", "  ")
    input_string = input_string.translate(str.maketrans('', '', string.punctuation))
    input_string = input_string.lower()
    input_string = input_string.split(" ")
    while '' in input_string:
        input_string.remove('')
    return input_string


def count_words(word_list):
    """Count the formated and filtered list of words"""
    """Returns a word dictionary with number of the word counted as the key value"""
    word_dict = {}
    for word in word_list:
        if not word_dict.get(word) == None:
            updated_value = word_dict.get(word) + 1
            word_dict.update({word : updated_value})
        else:
            word_dict[word] = 1
    return word_dict


def display_words(tuple_list):
    longest_word_len = 0
    for tuple in tuple_list:
        if len(tuple[0]) > longest_word_len:
            longest_word_len = len(tuple[0])
    for tuple in tuple_list:
        half_print_string = f"{tuple[0]} | "
        half_print_string = half_print_string.rjust(longest_word_len + 4)
        print(half_print_string + f"{tuple[1]}".rjust(2) + " " + add_stars(tuple[1]))

def add_stars(number):
    stars = "*"
    return stars*number

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)