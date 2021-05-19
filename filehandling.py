####Reading file line by line####
# f=open('myfile.txt','r')
# firstline=f.readline()
# secondline=f.readline()
# print(firstline)
# print(secondline)
# f.close()
##############Reading and writing to a file##################
# 
# f = open('myfile.txt','r') #opening in read mode
# fw = open('myfile.txt','a') #opening in append mode
# fw.write('\nThis sentence will get appended') #writing to a file
# fw.write('\nPython is fun') #writing to a file
# 
# for line in f:
#     print(line,end="")
# 
# fw.close()
# f.close()

###opening and reading text file by buffer size###
# inputfile= open("myfile.txt",'r')
# outputfile= open("myoutfile.txt",'w')
#
# msg=inputfile.read(10)
# while len(msg):
#     outputfile.write(msg+'\n') #adding enter after every buffer size 10
#     msg=inputfile.read(10)
#
# inputfile.close()
# outputfile.close()
#######Reading Binary files #########
inputfile=open('myimage.bmp','rb')
outputfile=open('myoutputfile.bmp','wb')
inputfile.close()
outputfile.close()

import os
os.remove('myoutputfile.bmp') #remove file
os.rename('myfile.txt','mynewfile.txt') #rename file