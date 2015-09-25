from sys import path
import string
import os
import itertools


class Palindrome(object):

    """builder palindromes of the text specified in the console "
    "or in a text file and output together palindromes in the "
    "console or to a text file"""

    def __init__(self, text):
        super(Palindrome, self).__init__()
        self.text = text
        self.list_word = self._preparation_text(self.text)

    def create_list_pal(self):
        """creates a list of all the plaintext palindromic"""
        prefix_list = list(map(lambda x: [x], self.list_word))
        suffix_list = list(map(lambda x: [], self.list_word))

        combinations_list = list(map(lambda x: list(x), itertools.combinations(
            self.list_word, len(self.list_word) - 1)))[::-1]

        list_pal = []
        for prefix, suffix, combination in zip(
                prefix_list, suffix_list, combinations_list):
            prefix_str = ''.join(prefix)
            suffix_str = ''.join(suffix[::-1])
            len_prefix_str = len(prefix_str)
            len_suffix_str = len(suffix_str)

            if len_prefix_str >= len_suffix_str:
                prefix_rev = prefix_str[len_suffix_str:][::-1]
                for word_combination in combination:
                    if word_combination.endswith(prefix_rev) or\
                            prefix_rev.endswith(word_combination):
                        suffix_list.append(suffix + [word_combination])
                        prefix_list.append(prefix)
                        new_combination = combination.copy()
                        new_combination.remove(word_combination)
                        combinations_list.append(new_combination)
            else:
                suffix_rev = suffix_str[:len_suffix_str - len_prefix_str][::-1]
                for word_combination in combination:
                    if word_combination.startswith(suffix_rev) or\
                            suffix_rev.startswith(word_combination):
                        prefix_list.append(prefix + [word_combination])
                        suffix_list.append(suffix)
                        new_combination = combination.copy()
                        new_combination.remove(word_combination)
                        combinations_list.append(new_combination)

            pre_and_suf = prefix_str + suffix_str
            if pre_and_suf == pre_and_suf[::-1]:
                list_pal.append(
                    " ".join(prefix) + " " + " ".join(suffix[::-1]))

        return list_pal

    def _preparation_text(self, text):
        """prepares the text and deletes from unnecessary characters"""
        for symbol in string.punctuation:
            text = text.replace(symbol, "")
        text = text.lower()
        list_word = text.split(" ")
        return list_word

    @staticmethod
    def test():
        """testing method"""
        lever = False

        with open(os.path.join(path[0], "test", "input1.txt")) as file_in:
            with open(os.path.join(path[0], "test", "check1.txt")) as check:
                string = file_in.read()
                check_string = check.read()
                palindrome = Palindrome(string)
                pal = palindrome.create_list_pal()
                pal = '\n'.join(pal)
                if pal == check_string:
                    print(
                        'Verification was successful. Function: '
                        'createListPal, language: english')
                else:
                    print(
                        'Validation fails.\nExpected:\n{0}'
                        '\nObtained:\n{1}'.format(check_string, pal))
                    lever = True

        with open(os.path.join(path[0], "test", "input2.txt")) as file_in:
            with open(os.path.join(path[0], "test", "check2.txt")) as check:
                string = file_in.read()
                check_string = check.read()
                palindrome = Palindrome(string)
                pal = palindrome.create_list_pal()
                pal = '\n'.join(pal)
                if pal == check_string:
                    print(
                        'Verification was successful. Function: '
                        'createListPal, language: russian')
                else:
                    print(
                        'Validation fails.\nExpected:\n{0}'
                        '\nObtained:\n{1}'.format(check_string, pal))
                    lever = True
        print("Complete test")

        return lever
