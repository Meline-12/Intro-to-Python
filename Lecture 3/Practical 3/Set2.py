import argparse

parser=argparse.ArgumentParser()

parser.add_argument("set", help="set", type=int)
set2={10, 11, 12, 13, 14}
print(set2)
args=parser.parse_args()
set2.discard(args.set)
print(set2)



