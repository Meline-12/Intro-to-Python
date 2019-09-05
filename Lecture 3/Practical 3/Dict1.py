import argparse

parser=argparse.ArgumentParser()

parser.add_argument("key", help="key", type=str)
parser.add_argument("value", help="value", type=str)
args=parser.parse_args()
dict1={args.key: args.value}
print(dict1)