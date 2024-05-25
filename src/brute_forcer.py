import requests
import time

logo = '''
\033[95m||      ||    || |/|/|/|/|| |/|/|/|/| |/|/|/|/|
\033[95m||      ||    || |/|      | ||_______ ||______|      \033[97m v0.07
\033[95m||      ||    || |/|/|/|/|| ||        ||  \\
\033[95m||_____ ||____|| ||         |/|/|/|/| ||   \\
'''

print(logo + "\n")

def brute_force(base_url, wordlist_path):
    with open(wordlist_path, 'r') as wordlist:
        lines = wordlist.readlines()
        total_lines = len(lines)
        print(f"\033[97m| target:\033[93m {base_url} \033[97m| wordlist:\033[93m {wordlist_path} \033[97m| wordlist size:\033[93m {total_lines} \033[97m|")
        progress = 0
        for line in lines:
            path = line.strip()
            url = f"{base_url}/{path}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print()
                    print(f"\033[0mFound:\033[93m {url}")
            except requests.RequestException as e:
                print(f"Error accessing {url}: {e}")

            progress += 1
            display_progress_bar("\r" + str(progress), str(total_lines))

def display_progress_bar(current, total, bar_length=20):
    fraction = int(current) / int(total)
    arrow = '\\' * int(round(fraction * bar_length))
    padding = '-' * (bar_length - len(arrow))
    percent = round(fraction * 100, 1)
    progress_message = f'\rProgress: [{arrow}{padding}] {percent}% ({current}/{total})'
    print(progress_message, end='', flush=True)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="\033[97mLuper: Discovery Enumeration.")
    parser.add_argument('\033[97m-u', '--url', required=True, help="A URL base para força bruta")
    parser.add_argument('\033[97m-w', '--wordlist', required=True, help="O arquivo de wordlist a ser usado")

    args = parser.parse_args()
    brute_force(args.url, args.wordlist)

if __name__ == '__main__':
    main()