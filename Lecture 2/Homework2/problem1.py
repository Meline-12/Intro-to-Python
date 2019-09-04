import argparse

parser=argparse.ArgumentParser()

parser.add_argument("--num_y", help="Given years", type=str)
parser.add_argument("--num_d", help="Given days", type=str)
import datetime
current_time=datetime.datetime.now()
print("Current time:", current_time)
args=parser.parse_args()
if args.num_y:
    print(args.num_y)
if args.num_d:
    print(args.num_d)
final_date=current_time + args.num_y
print(final_date)

