def main():
    book_path = "books/frankestein.txt"
    text = get_text(book_path)
    split = split_text(text)

    print(len(split))

def get_text(path):
    with open(path) as f:
        return f.read()

def split_text(texts):
    text = texts.split()
    return text


main()