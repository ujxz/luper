# tests/test_brute_forcer.py

import unittest
from luper.brute_forcer import brute_force
from unittest.mock import patch, mock_open

class TestBruteForcer(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='admin\nuser\ntest')
    @patch('requests.get')
    def test_brute_force(self, mock_get, mock_file):
        # Simulate a 200 OK response
        mock_get.return_value.status_code = 200

        result = []
        def print_found(url):
            result.append(url)

        with patch('builtins.print', print_found):
            brute_force('http://example.com', 'dummy_wordlist.txt')

        self.assertEqual(result, [
            'Found: http://example.com/admin',
            'Found: http://example.com/user',
            'Found: http://example.com/test',
        ])

if __name__ == '__main__':
    unittest.main()
