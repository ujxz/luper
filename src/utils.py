# luper/utils.py

def read_wordlist(wordlist_path):
    with open(wordlist_path, 'r') as file:
        return [line.strip() for line in file]
