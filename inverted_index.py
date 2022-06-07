import mrs
import string
import sys

class WordIndex(mrs.MapReduce):
    def map(self,line_num,line_text):

        stop_words = open('./parameters/stopwords.txt','r').read().split()
        punctuations = ['--', '...', '\'']
        for word in line_text.split():
            if any(punct in word for punct in punctuations):
                for punct in punctuations:
                    word = word.replace(punct,' ')
                word = word.split()
                for the_word in word:
                    the_word = the_word.strip(string.punctuation).lower()
                    if the_word and the_word not in stop_words and not the_word[0].isdigit():
                        yield (the_word,line_num + 1)
            else:
                word = word.strip(string.punctuation).lower()
                if word and word not in stop_words and not word[0].isdigit():
                    yield (word,line_num + 1)

    def reduce(self,word,line_num):
        lineNumbers = []
        for i in line_num:
            if len(lineNumbers) >= 50:
                break
            if i not in lineNumbers:
                lineNumbers.append(i)
        yield lineNumbers

if __name__ == '__main__':
     hold  =  mrs.main(WordIndex)

