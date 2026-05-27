from pathlib import Path


def count_words(path):
    """Conte o número aproximado de palavras em um arquivo."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Conte o número aproximado de palavras no arquivo:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


path = Path('alice.txt')
count_words(path)