import os


fo = open('./data1.txt', "r")
stat = os.stat('./data1.txt')
content = fo.read(stat.st_size)
fo.close()
content = content.split(" ")
for elem in content:
    print(elem)
