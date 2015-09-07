def hammingdistance(string1, string2):
    hamming = 0
    for i in range(0, len(string1)):
        if (string1[i] != string2[i]):
            hamming = hamming+1

    return hamming

##
##with open ("dataset_9_3.txt", "r") as myfile:
##    data=myfile.read()#.replace('\n', '')
####print data
##print hammingdistance(data.split('\n')[0], data.split('\n')[1])
