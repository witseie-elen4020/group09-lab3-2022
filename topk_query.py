import mrs
import string

class WordCount(mrs.MapReduce):
    def map(self, line_number, line_text):
    	#defined new stop words
        stop_words = ["for", "as", "the" ,"is", "at", "which", "to","or","it","had", ""] 
        open('SortedWords.txt', 'w').close()
        
        #Map words in textfile
        for word in line_text.split():
            word = word.strip(string.punctuation).lower()

            if word not in stop_words and not word.isdigit():
                yield (word, 1)
	
    #Reduce words	
    def reduce(self,word, count):  
        self.Sort(word, sum(count))
        yield sum(count)

    #Sort words from highest frequency to smallest frquency
    def Sort(self,word, count):
        words = open("SortedWords.txt", "a+")
        words.write(word + " " + str(count) + "\n")
        words.close()

        with open("SortedWords.txt") as textFile:
            lines = [line.split() for line in textFile]
            lines.sort(key = lambda x: x[1], reverse=True)
           
        self.TopKQuery(lines)
        words.close()
     
    #Select top 10 or 20 most occuring words
    def TopKQuery(self, lines):
	
        top10kquery = open("./outputDocs/top10_kquery.txt", "w")
        top20kquery = open("./outputDocs/top20_kquery.txt", "w")
        count = 0
	 
        for line in lines :
            if count <20:   
                if count <10:
                    top10kquery.write(line[0] +" "+ line[1] + "\n")
                
                top20kquery.write(line[0] +" "+ line[1] + "\n")
                count = count + 1
            if count == 20:
                break
       
        top10kquery.close() 
        top20kquery.close()
   
if __name__ == '__main__':
    mrs.main(WordCount)
   


    
