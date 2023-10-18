import os

#Read contents from a file
file = open("C:/Users/Administrator/OneDrive/Pictures/Documents/Custom Project Designs/FHIP/First.txt","r")
print(file.read())
file.close()

#Read contents up to index 7 from file
file = open("C:/Users/Administrator/OneDrive/Pictures/Documents/Custom Project Designs/FHIP/First.txt","r")
print(file.read(7))
file.close()

#Read contents line by line
file = open("C:/Users/Administrator/OneDrive/Pictures/Documents/Custom Project Designs/FHIP/First.txt","r")
print(file.readline())
file.close()


#Read contents line by line in an array view
file = open("C:/Users/Administrator/OneDrive/Pictures/Documents/Custom Project Designs/FHIP/First.txt","r")
print(file.readlines())
file.close()