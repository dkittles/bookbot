def main():
    book_path = "books/frankestein.txt"
    text = get_text(book_path)
    split = split_text(text)
    words = count_letters(split)
    sorted_letters = sorted(words.items(), key=lambda x:x[1], reverse=True)
    print(print_dict(sorted_letters))
    # print(sorted_letters)

def get_text(path):
    with open(path) as f:
        return f.read()

def split_text(texts):
    text = texts.split()
    return text

def count_letters(words):
    alpha_dict = {}
    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter in alpha_dict and letter.isalpha():
                alpha_dict[letter] += 1
            elif letter not in alpha_dict and letter.isalpha():
                alpha_dict[letter] = 1
    return alpha_dict

def print_dict(letters):
    for letter in letters:
        print(f"The {letter[0]} appeared {letter[1]} times.")
        if None:
            return print("-- End of report --")
main()