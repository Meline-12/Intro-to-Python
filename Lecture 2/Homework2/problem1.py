import argparse

import datetime

parser=argparse.ArgumentParser()
parser.add_argument("--num_y", help="Given years", type=int)
parser.add_argument("--num_d", help="Given days", type=int)
current_date=datetime.datetime.now()
final_date=datetime.datetime
args=parser.parse_args()

print("Current date:", current_date)
if args.num_y:
    print("Given years:", args.num_y)
    final_date=datetime.datetime(current_date.year + args.num_y, current_date.month, current_date.day)
else:
    print("Given years: not given")
    final_date=current_date
if args.num_d:
    print("Given days:", args.num_d)
    final_date=datetime.datetime(current_date.year, current_date.month, current_date.day + args.num_d)
else:
    print("Given days: not given")
    final_date=current_date

print("Final date:", final_date)


