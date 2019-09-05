import argparse

parser=argparse.ArgumentParser()

parser.add_argument("set", help="set", type=int)
set3={5, 10, 15, 20, 25}
print(set3)
min=min(set3)
max=max(set3)
print("min:", min)
print("max:", max)
args=parser.parse_args()
print(args.set > min and args.set < max)





