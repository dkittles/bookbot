def main():
    book_path = "books/frankestein.txt"
    text = get_text(book_path)
    print(text)

def get_text(path):
    with open(path) as f:
        return f.read()

main()