# luper/brute_forcer.py

import requests

def brute_force(url, wordlist):
    with open(wordlist, 'r') as file:
        for line in file:
            word = line.strip()
            test_url = f"{url}/{word}"
            response = requests.get(test_url)
            if response.status_code == 200:
                print(f"Found: {test_url}")

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Luper: A web page brute-force tool.")
    parser.add_argument("url", help="The base URL to brute-force")
    parser.add_argument("wordlist", help="The wordlist file to use")

    args = parser.parse_args()
    brute_force(args.url, args.wordlist)
