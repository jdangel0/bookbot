def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    character_counts = character_count(text)
    print(character_counts)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def word_count(text):
    words = text.split()
    return len(words)


def character_count(text):
    characters = {}
    for c in text:
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1

    return characters

main()