import numpy as np
def minskew(genome):
    skew = np.zeros(len(genome)+1)
    skew[0] = 0
    for i in range (0, len(genome)):
##        print skew[i]
        if (genome[i] == "G"):
            skew[i+1] = skew[i]+1
        if (genome[i] == "C"):
            skew[i+1] = skew[i]-1
        if ((genome[i] == "A") or (genome[i]=="T")):
            skew[i+1] = skew[i]
        
    return np.where(skew == skew.min())

            
##with open ("dataset_7_6.txt", "r") as myfile:
##    data=myfile.read()#.replace('\n', '')
####print data
##print minskew(data)#.split('\n')[0], data.split('\n')[1])
