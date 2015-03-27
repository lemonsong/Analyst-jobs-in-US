import re
file = open("data.txt")
writer = open("empdata.txt",'w')

for line in file:
    line=line.strip()
    line = line.split('\t')
    for n in range(0,len(line)):
        if line[n][0]=='"':
            line[n]=line[n][1:-1]
        print  line[n]
    
    writer.write('[' + line[0]+','+line[1]+','+str(line[2])+','+str(line[3])+ '],'+'\n')