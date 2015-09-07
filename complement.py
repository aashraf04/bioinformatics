def complement(text):
    s = ""
    for i in text:
        if (i == "A"):
            s+="T"
        if (i == "C"):
            s+="G"
        if (i == "G"):
            s+="C"
        if (i == "T"):
            s+="A"
    return s[::-1]

with open ("dataset_3_2.txt", "r") as myfile:
    data=myfile.read()#.replace('\n', '')

##print data
print complement(data)
