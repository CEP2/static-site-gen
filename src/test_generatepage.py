import unittest
from generatepage import extract_title

class TestGeneratePage(unittest.TestCase):

    def test_extract_title(self):

        with open("content/index.md", "r") as f:
            content = f.read()
        line_one = content.split('\n')[0]
        line_one_expected = "Tolkien Fan Club"
        print(line_one)
        print(extract_title(line_one))


        #(input, expected)
        success_tests = [
            ("# Hello", "Hello"),
            ("# This has multiple words.", "This has multiple words."),
            ("#    Leading spaces", "Leading spaces"),
            ("# Trailing spaces     ", "Trailing spaces"),
            ("# Tolkien Fan Club\n",line_one_expected),
            (line_one, line_one_expected)

        ]
        for test in success_tests:
            t = test[0]
            expected = test[1]
            actual = extract_title(t)
            self.assertEqual(expected, actual,f"expected: {expected}, actual: {actual}")
        
        fail_tests = [
            "#Too close",
            "No title marker.",
            "# ", # too short
            "", #too short
            " # ", #leading 
        ]

        for test in fail_tests:
            with self.assertRaises(ValueError, msg=f"error not raised input:{test}"):
                extract_title(test)