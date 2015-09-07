from patterncount import PatternCount
import numpy as np
def FrequentWords(text, k):
    k = int(k)
    s = ""
    count = np.zeros(len(text)-k)
    for i in range (0, len(text)-k):
        pattern = text[i:i+k]
        count[i] = PatternCount(text, pattern)
    maxCount = max(count)
    for i in range (0, len(text)-k):
        if (count[i] == maxCount):
            s += text[i:i+k]
            s+= " "
    #gets rid of duplicates:
    return ' '.join(set(s.split()))

##with open ("dataset_2_9.txt", "r") as myfile:
##    data=myfile.read()#.replace('\n', '')
##print data
##print FrequentWords(data.split('\n')[0], data.split('\n')[1])

            
