from patterncount import PatternCountHamming
import numpy as np

def reversecomplement(pattern):
    patternr = ""
    pattern = pattern[::-1]
    for i in range(0, len(pattern)):
        if (pattern[i]=="A"):
            patternr+="T"
        if (pattern[i]=="T"):
            patternr+="A"
        if (pattern[i]=="G"):
            patternr+="C"
        if (pattern[i]=="C"):
            patternr+="G"
    return patternr


def FrequentWordsHammingReverse(text, k, d):
    k = int(k)
    d = int(d)
    s = ""
    count = np.zeros(len(text)-k+1)
    countr = np.zeros(len(text)-k+1)
    for i in range (0, len(text)-k+1):
        pattern = text[i:i+k]
        count[i] = PatternCountHamming(text, pattern, d)
        countr[i] = PatternCountHamming(text, reversecomplement(pattern), d)
    maxCount = max(count+countr)
    for i in range (0, len(text)-k+1):
        if (count[i] + countr[i] == maxCount):
            s += text[i:i+k]
            s+= " "
            s+= reversecomplement(text[i:i+k])
            s+= " "
    #gets rid of duplicates:
    return ' '.join(set(s.split()))

with open ("dataset_9_8.txt", "r") as myfile:
    data=myfile.read()#.replace('\n', '')
##print data
print FrequentWordsHammingReverse(data.split('\n')[0], data.split('\n')[1].split(' ')[0],data.split('\n')[1].split(' ')[1])
