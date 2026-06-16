import unittest
from generatepage import extract_title

class TestGeneratePage(unittest.TestCase):

    def test_extract_title(self):
        #(input, expected)
        success_tests = [
            ("# Hello", "Hello"),
            ("# This has multiple words.", "This has multiple words."),
            ("#    Leading spaces", "Leading spaces"),
            ("# Trailing spaces     ", "Trailing spaces"),

        ]
        for test in success_tests:
            t = test[0]
            expected = test[1]
            actual = extract_title(t)
            self.assertEqual(expected, actual)
        
        fail_tests = [
            "#Too close",
            "No title marker.",
            "# ", # too short
            "", #too short
            " # ", #leading 
        ]

        for test in fail_tests:
            with self.assertRaises(ValueError):
                extract_title(test)