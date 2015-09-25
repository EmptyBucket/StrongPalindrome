import sys
import argparse
from palindrome import Palindrome


def normal():
    try:
        if args.in_file:
            with open(args.in_file) as file_in:
                text = file_in.read()
        else:
            text = input('Enter the text for constructing palindromes:\n')

        palindrome = Palindrome(text)
        list_pal = palindrome.create_list_pal()

        if args.out_file:
            with open(args.out_file, 'w') as file_out:
                file_out.write('\n'.join(list_pal))
        else:
            print('Constructed palindromes:')
            for i in list_pal:
                print(i)
    except Exception as e:
        sys.exit("Error: {0}".format(e))


def test():
    lever = Palindrome.test()
    if not lever:
        print("Test is passed")
    else:
        print("Test fails")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Palindrome",
        description="purpose tools - building palindromes of the text "
        "specified in the console or in a text file and output together "
        "palindromes in the console or to a text file",
        epilog="Copyright (C) 2015 Politov Alexey Version 1.0")
    sub_parsers = parser.add_subparsers(title="use normal or test mode")

    normal_parser = sub_parsers.add_parser("normal")
    normal_parser.add_argument(
        "-i", "--in_file", action="store", type=str,
        help="Input file to create palindromes")
    normal_parser.add_argument(
        "-o", "--out_file", action="store", type=str,
        help="File for output palindromes")
    normal_parser.set_defaults(func=normal)

    test_parser = sub_parsers.add_parser("test")
    test_parser.set_defaults(func=test)

    args = parser.parse_args()
    try:
        args.func()
    except AttributeError:
        parser.parse_args(["-h"])
