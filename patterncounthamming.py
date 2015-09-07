from hammingdistance import hammingdistance

def PatternCountHamming(text, pattern, d):
    count = 0
    d = int(d)
    for i in range (0, len(text)-len(pattern)+1):
##        print text [i:i+len(pattern)]
        if (hammingdistance(text [i:i+len(pattern)] , pattern)<=d):
            count = count + 1
    return (count)
##with open ("dataset_9_6.txt", "r") as myfile:
##    data=myfile.read()#.replace('\n', '')
####print data
##print PatternCountHamming(data.split('\n')[0], data.split('\n')[1], data.split('\n')[2])
