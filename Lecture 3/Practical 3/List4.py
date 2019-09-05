import argparse

parser=argparse.ArgumentParser()

parser.add_argument("list", help="list", type=int)
list4=[10, 12, 12, 15, 20]
print(list4)
args=parser.parse_args()
list4.remove(args.list)
print(list4)



