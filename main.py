def main():
    book_path = "books/frankestein.txt"
    text = get_text(book_path)
    split = split_text(text)
    count = count_text(split)
    print(count)

def get_text(path):
    with open(path) as f:
        return f.read()

def split_text(texts):
    text = texts.split()
    return text

def count_text(texts):
    i = 0
    for text in texts:
        i += 1
    return i


main()