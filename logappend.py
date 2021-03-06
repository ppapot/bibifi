__author__ = 'Pascal Papot'
import argparse


parser = argparse.ArgumentParser(prog='logappend')
parser.add_argument("-T", "--timestamp",help="Time the event is recorded.", type = int)
parser.add_argument("-K", "--token",help="Token used to authenticate the log.", type = str)

group1 = parser.add_mutually_exclusive_group()
group1.add_argument("-E", "--employee-name",help="Name of employee",dest = 'employee',  type = str)
group1.add_argument("-G", "--guest-name",help="Name of guest.", dest = 'guest',  type = str)

group2 = parser.add_mutually_exclusive_group()
group2.add_argument("-A",help="Specify that the current event is an arrival", dest='event_type', action='store_const', const = "arrival")
group2.add_argument("-L",help="Specify that the current event is a departure",dest='event_type',action='store_const', const = "departure")

parser.add_argument("-R", "--room-id",help="Specifies the room ID for an event.", type = int)

parser.add_argument("log", help= "The path to the file containing the event log.")
args = parser.parse_args()


print(args.employee)
