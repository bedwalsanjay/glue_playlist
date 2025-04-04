import sys
from awsglue.utils import getResolvedOptions

print(sys.argv)
args_list=["fname","lname"]

args = getResolvedOptions(sys.argv,args_list)
print(type(args))
print(args)

print(args["fname"])
print(args["lname"])

