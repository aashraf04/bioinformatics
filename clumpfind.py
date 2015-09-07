# k-mer appears at least t times in a length L of the genome

from frequentwords import FrequentWords
from patterncount import PatternCount
def clumpfind(genome, k, L, t):
    k = int(k)
    L = int(L)
    t = int(t)
    clumps = ""

    
    
    for i in range (0, len(genome)-L):
        genomeblock = genome[i:i+L]
        
        s = FrequentWords(genomeblock, k)

        freqwords = s.split(' ')
        
        
        for j in range(0, len(freqwords)):
            if (PatternCount(genomeblock, freqwords[j])>=t):
                clumps+=freqwords[j]
                clumps+=" "
                
    return ' '.join(set(clumps.split()))

##import numpy as np
##import collections
##compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
##
##def clumpfind(genome, k, L, t):
##    k = int(k)
##    L = int(L)
##    t = int(t)
##    Lgenome = len(genome)
##    Ngenome = np.zeros(Lgenome)
##    for i in range (0, Lgenome-1):
##        if (genome[i] == 'A'):
##            Ngenome[i] = int(0)
##        if (genome[i] == 'C'):
##            Ngenome[i] = int(1)
##        if (genome[i] == 'G'):
##            Ngenome[i] = int(2)
##        if (genome[i] == 'T'):
##            Ngenome[i] = int(3)
##
##
##    clumps = []
##
##    for i in range (0, Lgenome-L):
##        
##        genomeblock = Ngenome[i:i+L]
##        Lgb = len(genomeblock)
##        s = []
##        count = np.zeros(Lgb-k)
##        for i in range (0, Lgb-k):
##            pattern = genomeblock[i:i+k]
##
##            c = 0
##            for i in range (0, Lgb-len(pattern)):
##                if (compare(genomeblock[i:i+len(pattern)], pattern)):
##                    c = c +1
##            
##            count[i] = c
##
##        maxCount = max(count)
##        
##        for i in range (0, Lgb-k):
##            if (count[i] == maxCount):
##                s.append (genomeblock[i:i+k])
##                
##        #gets rid of duplicates:
##        s =  list(set(s[0]))
##        print s
##        for j in range(0, len(s)):
##            c = 0
##            sj = s[j]
##            for i in range (0, Lgb-len(sj)):
##                if (genomeblock [i:i+len(sj)] == sj):
##                    c = c +1
##            
##            if (c>=t):
##                clumps.append(sj)
##
##    clumps =  list(set(clumps))
##
##    
##
##    for i in range (0, len(clumps)):
##        for j in clumps[i]:
##            if (clumps[i][j] == 0):
##                clumps[i][j] = 'A'
##            if (clumps[i][j] == 1):
##                clumps[i][j] = 'C'
##            if (clumps[i][j] == 2):
##                clumps[i][j] = 'G'
##            if (clumps[i][j] == 3):
##                clumps[i][j] = 'T'
##    
##    return clumps


with open ("dataset_4_4.txt", "r") as myfile:
    data=myfile.read()#.replace('\n', '')
##print data
print clumpfind(data.split('\n')[0], data.split('\n')[1].split(' ')[0], data.split('\n')[1].split(' ')[1], data.split('\n')[1].split(' ')[2])
             
##            
