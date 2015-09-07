def PatternMatch(pattern, text):
    s = ""
    for i in range (0, len(text)-len(pattern)):
        if (text [i:i+len(pattern)] == pattern):
            s+= str(i)
            s+=" "
    return s

with open ("eg.txt", "r") as myfile:
    data=myfile.read()#.replace('\n', '')
##print data
##print PatternMatch(data.split('\n')[0], data.split('\n')[1])
print PatternMatch("CTTGATCAT",data)

            
