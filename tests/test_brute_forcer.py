import sys
import os
import argparse
import unittest
from unittest.mock import patch, mock_open

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.brute_forcer import brute_force

class TestBruteForcer(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='admin\nuser\ntest')
    @patch('requests.get')
    def test_brute_force(self, mock_get, mock_file):
        # Simulate a 200 OK response for all paths
        mock_get.return_value.status_code = 200
        
        result = []
        def print_found(url):
            result.append(url)
        
        with patch('builtins.print', print_found):
            brute_force('https://example.com', 'wordlist.txt')
        
        expected_results = [
            'Found: https://example.com/admin',
            'Found: https://example.com/user',
            'Found: https://example.com/test',
        ]
        self.assertEqual(result, expected_results)

def main():
    parser = argparse.ArgumentParser(description="Luper: Ferramenta de força bruta para páginas web.")
    parser.add_argument('-u', '--url', required=True, help="A URL base para força bruta")
    parser.add_argument('-w', '--wordlist', required=True, help="O arquivo de wordlist a ser usado")

    args = parser.parse_args()
    brute_force(args.url, args.wordlist)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
    else:
        unittest.main()
