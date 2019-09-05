import argparse

parser=argparse.ArgumentParser()

parser.add_argument("list", help="list", type=int)
list2=[1, 1, 2, 4, 4, 3]
args=parser.parse_args()
number=list2.count(args.list)
print(number)




