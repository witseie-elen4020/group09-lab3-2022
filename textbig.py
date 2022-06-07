import os
import sys
import time

print("")

print("----------------large.txt----------------\n")
start = time.time()

os.system('python3 wordcount.py ' + './inputdocs/big.txt' + ' outputdocs')
end =time.time()
timeTaken = (end-start)
print("Time Taken for the Word Count: ", timeTaken)

print("")

start = time.time()

os.system('python3 topk_queryMethod2.py ' + './inputdocs/big.txt' + ' outputdocs')
end =time.time()
timeTaken = (end-start)
print("Time Taken for the Top 10 and 20 k Query: ", timeTaken)

print("")

start = time.time()
os.system('python3 inverted_index.py ' + './inputdocs/big.txt' + ' outputdocs')
end =time.time()
timeTaken = (end-start)
print("Time Taken for Inverted Index: ", timeTaken)

print("")
