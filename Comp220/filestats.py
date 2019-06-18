################################################################
# Write a python program that will read your JavaScript syntax program
# as input into your program
# Determine the number of lines in the JavaScript program 
# and display it to the user
# Determine how many “else” statements are in the JavaScript program
# How many characters(total) are in the JavaScript Program?
#################################################################

with open("basic.js", "r") as f:
    #get number of lines in file
    numlines = -1
    numelse = 0
    numchar = 0
    currline = "a"
    while len(currline) > 0:
        currline = f.readline()
        numchar+= len(currline)
        if 'else' in currline:
            numelse+=1
        numlines+=1
print("numlines in file is: ", numlines)
print("number of else in file: ", numelse)
print("number of chars in file: ", numchar)

# Write a python program that will:
# read all the files and their sizes from a directory
# print a nice little report that tells us the number of files and the total size of the directory

from pathlib import Path

p = Path('.')
totalsize = 0
totalfiles = 0
for currFile in p.iterdir():
    totalfiles+=1
    totalsize += currFile.stat().st_size

print("In the Current Directory\n")
print("  Total number of files: ", totalfiles)
print("  Total size of files:   ", totalsize, "bytes")

# use a dictionary (don’t use“if” statements) to total “res_cnt” by
# CLASS
# SECTOR
# count the number of lines
# print a nice little report at the end
# write the report to a file called report.txt.

with open("Census_By_Community_2018.csv", "r") as f:
    #get number of lines in file
    numlines = 1
    numchar = 0
    maxlen = 0
    #ignore first line of file, has data column names
    currline = f.readline()
    
    classes = {}
    sectors = {}
    #read first data line
    currline = f.readline()
    

    while len(currline) > 0:
        
        splitline = currline.split(",")
        currclass = splitline[0]
        currsector = splitline[4]
        currrescount = int(splitline[9])

        oldclassrescount = classes.get(currclass, 0)
        newclassrescount = oldclassrescount+currrescount
        classes[currclass] =  newclassrescount

        oldsectorrescount = sectors.get(currsector, 0)
        newsectorrescount = oldsectorrescount+currrescount
        sectors[currsector] = newsectorrescount
        maxlen = max(maxlen, len(currclass), len(currsector))
        numlines+=1

        currline = f.readline()

with open("report.txt", "w+") as f:
    nextline = f'Class{" " * (maxlen - 3)}Residents'
    print(nextline)
    f.write(nextline+'\n')
    nextline = f'{"-" * (maxlen+11)} '
    print(nextline)
    f.write(nextline+'\n')
    for key in classes:
        nextline = f'{key}{" " * (maxlen-len(key)+1)}{format(classes[key]," 10,")}'
        print(nextline)
        f.write(nextline+'\n')

    nextline = f'\nSector{" " * (maxlen - 4)}Residents'
    print(nextline)
    f.write(nextline+'\n')
    nextline = f'{"-" * (maxlen+11)} '
    print(nextline)
    f.write(nextline+'\n')

    for key in sectors:
    
        nextline = f'{key}{" " * (maxlen-len(key)+1)}{format(sectors[key]," 10,")}'
        print(nextline)
        f.write(nextline+'\n')


    nextline = f'Number of lines in file is: {numlines}'
    print(nextline)
    f.write(nextline+'\n')
