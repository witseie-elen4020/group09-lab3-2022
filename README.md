# group09-lab3-2022
## MapReduce
Mrs MapReduce has been used to implement the Word Count, Top-K Query and Inverted Index algorithms. 
Mrs MapReduce is a Python framework available on linux. The python scripts used to implement the 
three algorithms are located in the root folder under the names `wordcount.py`, `topk_query.py` and 
`inverted_index.py`. There is also an `textsmall.py`and 'textlarge.py' script which runs all the other 
three scripts automatically. The `inputdocs` folder contains the text files `small.txt`and `big.txt` 
downloaded from the course site on ulwazi and used for performance runs in this lab. The `outputdocs` 
folder is where the results from individual builds of the py files are stored in text files. The build 
instructions below describe to run the python files to get the results.

## Software Requirements
1. The programs have been developed on wits eie cluster accessed using Ubuntu linux version 18.04.2 LTS (Focal Fossa) 
2. Python 3.10.1 has been used to develop the python scripts
3. Mrs-MapReduce library to develop the MapReduce routines

## Build/Execute Instructions
1. Open the root folder and open in terminal.
2. Run the `textsmall.py` script with python **python3 textsmall.py**
3. This execution should automatically test for small txt file, by running the `wordcount.py`, `topk_query.py` and `inverted_index.py`
4. The input text files used in the build process are `small.txt` and `large.txt` taken from the `inputDocs` folder
5. Results of this build process are text files which can be found in the `outputDocs` folder 
6. Open these textfiles to view the results of the build process
7. One file is a word count in formart of `source_0_split_0_.mtxt` containing a list word counts sorted in order (from wordcount.py), 
   two files, top10kQuery.txt and top20kQuery.txt contain the top 10 and top 20 list of most occurring words respectively, 
   the other files in the format of `source_0_split_0_Something.mtxt` contains a word index having a list of words and the line numbers 
   at which their are found.
8. To test for big.txt, first delete the two mtxt files produced in outputdocs to avoid errors and repeat from step 2, run textbig.py script 
   with python **python3 textbig.py** 
9. Note to always delete the output files in the outputdocs except for the two topkquery txt files before running new test
