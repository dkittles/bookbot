def main():
    book_path = "books/frankestein.txt"
    text = get_text(book_path)
    split = split_text(text)
    words = count_letters(split)
    print(words)

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
            if not letter in alpha_dict:
                alpha_dict[letter] = 1
            else:
                alpha_dict[letter] += 1
    return alpha_dict
main()