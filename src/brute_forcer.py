import requests
import time

def brute_force(base_url, wordlist_path):
    with open(wordlist_path, 'r') as wordlist:
        lines = wordlist.readlines()
        total_lines = len(lines)
        progress = 0

        for line in lines:
            path = line.strip()
            url = f"{base_url}/{path}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print('''
\033[95m|\|         |\|     |\| |\|\|\|\|\|\| |\|\|\|\|\| |\|\|\|\|\|
\033[95m|\|         |\|     |\| |\|       |\| |\|         |\|     |\|
\033[95m|\|         |\|     |\| |\|       |\| |\|         |\|     |\|
\033[95m|\|         |\|     |\| |\|\|\|\|\|\| |\|\|\|\|\| |\|\|\|\|\|
\033[95m|\|         |\|     |\| |\|           |\|         |\|   |\|
\033[95m|\|\|\|\|\| |\|\|\|\|\| |\|           |\|\|\|\|\| |\|     |\|    \033[97m v0.07
                          ''') 
                    print(f"Found: {url}")
            except requests.RequestException as e:
                print(f"Error accessing {url}: {e}")

            progress += 1
            display_progress_bar(progress, total_lines)

def display_progress_bar(current, total, bar_length=20):
    fraction = current / total
    arrow = '\\' * int(round(fraction * bar_length))
    padding = '-' * (bar_length - len(arrow))
    percent = round(fraction * 100, 1)
    print(f'Progress: [{arrow}{padding}] {percent}% ({current}/{total})', end='\r')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Luper: Ferramenta de força bruta para páginas web.")
    parser.add_argument('-u', '--url', required=True, help="A URL base para força bruta")
    parser.add_argument('-w', '--wordlist', required=True, help="O arquivo de wordlist a ser usado")

    args = parser.parse_args()
    brute_force(args.url, args.wordlist)
