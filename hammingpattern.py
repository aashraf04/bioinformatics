from hammingdistance import hammingdistance
def hammingpattern(pattern, text, hamming):
    s = ""
    hamming = int(hamming)
    for i in range (0, len(text)-len(pattern)+1):
        if (hammingdistance(text [i:i+len(pattern)], pattern)<=hamming):
            s+= str(i)
            s+=" "
    return s

with open ("dataset_9_4.txt", "r") as myfile:
    data=myfile.read()#.replace('\n', '')
##print data
print hammingpattern(data.split('\n')[0], data.split('\n')[1], data.split('\n')[2])

            
