import argparse

parser = argparse.ArgumentParser()
parser.add_argument("str", help="number of string 7 and more", type=str)
args = parser.parse_args()
print("The old string:", args.str)
print("Middle 3 characters:", args.str[6:9])
print("The new string:", args.str.upper())