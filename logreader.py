__author__ = 'Pascal Papot'
import argparse


parser = argparse.ArgumentParser(prog='logreader')

parser.add_argument("-K", "--token",help="Token used to authenticate the log.",required = True, type = str, )
parser.add_argument("-H", "--html", help="Specifies output to be in HTML",  dest='output_type', action='store_const', const = "html", default= "text")
parser.add_argument("log", help= "The path to the file containing the event log.")
subparsers = parser.add_subparsers()

parser_status = subparsers.add_parser("-S")
parser_status.add_argument("-S", help="print current status of the log")

parser_rooms =  subparsers.add_parser("-R", help="Give the list of all teh room enter by a person")
group1 = parser_rooms.add_mutually_exclusive_group()
group1.add_argument("-E", "--employee-name",help="Name of employee",dest = 'employee',  type = str)
group1.add_argument("-G", "--guest-name",help="Name of guest.", dest = 'guest',  type = str)

parser_time =  subparsers.add_parser("-T", help="Give the total time spent in the gallery by a person")
group2 = parser_time.add_mutually_exclusive_group()
group2.add_argument("-E", "--employee-name",help="Name of employee",dest = 'employee',  type = str)
group2.add_argument("-G", "--guest-name",help="Name of guest.", dest = 'guest',  type = str)


#
# group2 = parser.add_mutually_exclusive_group()
# group2.add_argument("-A",help="Specify that the current event is an arrival", dest='event_type', action='store_const', const = "arrival")
# group2.add_argument("-L",help="Specify that the current event is a departure",dest='event_type',action='store_const', const = "departure")
#
# parser.add_argument("-R", "--room-id",help="Specifies the room ID for an event.", type = int)


args = parser.parse_args()


print(args.employee)
