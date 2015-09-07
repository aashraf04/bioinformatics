
def PatternCount(text, pattern):
    count = 0
    for i in range (0, len(text)-len(pattern)):
        
        if (text [i:i+len(pattern)]  == pattern):
            count = count + 1
    return (count)

##with open ("dataset_9_6.txt", "r") as myfile:
##    data=myfile.read()#.replace('\n', '')
####print data
##print PatternCountHamming(data.split('\n')[0], data.split('\n')[1], data.split('\n')[2])
