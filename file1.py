from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier)
# print(sk.__version__)

# import sys
# print(sys.path)
import file2
print(file2.a)
#use this for safety as it is more accurate
#
# from file2 import a
# print(a)
#dont use this if more than one file contains a there will be a problem

file2.printjoke("This is me")