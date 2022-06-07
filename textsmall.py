import os
import sys
import time

print("\n")
print("----------------small.txt----------------\n")

start = time.time()
os.system('python3 wordcount.py ' + './inputdocs/small.txt' + ' outputdocs')
end =time.time()
timeTaken = (end-start)
print("Time Taken for the Word Count: ", timeTaken)

print("")

start = time.time()
os.system('python3 topk_queryMethod2.py ' + './inputdocs/small.txt' + ' outputdocs')
end =time.time()
timeTaken = (end-start)
print("Time Taken for the Top 10 and 20 k Query: ", timeTaken)

print("")

start = time.time()
os.system('python3 inverted_index.py ' + './inputdocs/small.txt' + ' outputdocs')
end =time.time()
timeTaken = (end-start)
print("Time Taken for Inverted Index: ", timeTaken)
print("\n")

