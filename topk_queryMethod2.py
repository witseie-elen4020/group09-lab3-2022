import sys
import os
import string
import mrs


def sortList(text):
    return sorted(text, key= lambda x: x[1], reverse=True)

def top_Kquery(text, k):
    return text[:k]

def process():
    cur_ = os.getcwd()
    dir_ = os.path.join(cur_, "outputdocs")
    fname = os.path.join(dir_,"source_0_split_0_.mtxt")
    with open(fname, "r") as f:
        text = f.readlines()

    for i in text:
        text[text.index(i)] = tuple(i.split())
        

    return text


if __name__ == '__main__':

    sorted_txt = sortList(process())
    query = [10,20]
    for k in query:
        topkquery = open("./outputdocs/top"+ str(k) + "_kquery.txt", "w")
        topkquery.write("Top: "+ str(k) + " occuring words\n")
        for i in top_Kquery(sorted_txt,k):
                 topkquery.write(i[0] + " " + i[1] + "\n")

        topkquery.close()
