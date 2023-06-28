import atexit
import sys

from Repository import Repository

# arguments1 = ["/users/studs/bsc/2022/daniarov/Desktop/Spl Assignment 4/assignment 4/208163709_315809376/config.txt","/users/studs/bsc/2022/daniarov/Desktop/Spl Assignment 4/assignment 4/208163709_315809376/orders.txt","/users/studs/bsc/2022/daniarov/Desktop/Spl Assignment 4/assignment 4/208163709_315809376/output.txt","database.db"]
# args = ["/users/studs/bsc/2022/daniarov/Desktop/Spl Assignment 4/test_code/output.txt","/users/studs/bsc/2022/daniarov/Desktop/Spl Assignment 4/test_code/true_output.txt"]
arguments = sys.argv[1:]


# config = arguments1[0]
# order = arguments1[1]
# output = arguments1[2]
# db_path = arguments1[3]
config = arguments[0]
order = arguments[1]
output = arguments[2]
db_path = arguments[3]
repo = Repository(db_path)
repo.createTables()
repo.configPath(config)
repo.parseOrders(order)
repo.output(output)
repo.close()
# repo.hats.selectAll()


# def compareString(a,b):
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             print(a[i])
#             print(len(a))
#             print(len(a[i]))
#             print(b[i])
#             print(len(b))
#             print(len(b[i]))
#             print(False)
#
#
# file = open(args[0],'r')
# content = file.read()
# lines = content.split("\n")
# file2 = open(args[1],'r')
# content2 = file2.read()
# lines2 = content2.split("\n")
# compareString(lines,lines2)
