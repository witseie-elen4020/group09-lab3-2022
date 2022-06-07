import os
import sys
import time

print("----------------small.txt----------------\n")

start = time.time()
os.system('python word_count.py ' + './inputDocs/small.txt' + ' outputDocs')
end =time.time()
timeTaken = (end-start)
print("Time Taken for the Word Count: ", timeTaken)

print("")

start = time.time()
os.system('python topk_query.py ' + './inputDocs/small.txt' + ' outputDocs')
end =time.time()
timeTaken = (end-start)
print("Time Taken for the Top 10 and 20 k Query: ", timeTaken)


print("")

start = time.time()
os.system('python inverted_index.py ' + './inputDocs/small.txt' + ' outputDocs')
end =time.time()
timeTaken = (end-start)
print("Time Taken for Inverted Index: ", timeTaken)

print("")

print("----------------large.txt----------------\n")
start = time.time()

os.system('python word_count.py ' + './inputDocs/large.txt' + ' outputDocs')
end =time.time()
timeTaken = (end-start)
print("Time Taken for the Word Count: ", timeTaken)

print("")

start = time.time()
os.system('python inverted_index.py ' + './inputDocs/large.txt' + ' outputDocs')
end =time.time()
timeTaken = (end-start)
print("Time Taken for Inverted Index: ", timeTaken)

print("")
