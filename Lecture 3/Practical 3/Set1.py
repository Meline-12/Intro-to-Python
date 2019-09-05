import argparse

parser=argparse.ArgumentParser()

parser.add_argument("set", help="set", type=int)
set1={10, 11, 12, 13, 14}
print(set1)
args=parser.parse_args()
set1.add(args.set)
print(set1)



