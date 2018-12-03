import numpy as np
import re
read = open("train-balanced-sarcasm-copy-copy.csv", "r")
write = open("commas-fixed.csv", "w")

for x in read:
    split = x.split('"')
    print(split)
    
    if (len(split) > 1):
        split[0] = split[0].replace(",", "|")
        split[2] = split[2].replace(",", "|")
    else:
        split[0] = split[0].replace(",", "|")
        
    if (len(split) == 3 or len(split) == 1):
        write.write(''.join(split))

write.close()
read.close()



DATA = np.genfromtxt("commas-fixed.csv", delimiter='|', skip_header=1, dtype='S')
X = DATA[:,:1]
y = DATA[:,1:]
# print(X)
print(y)
# print(DATA)