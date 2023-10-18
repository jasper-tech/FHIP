import os

file = open("C:/Users/Administrator/OneDrive/Pictures/Documents/Custom Project Designs/FHIP/First.txt","r")
print(file.read())
file.close()

file = open("C:/Users/Administrator/OneDrive/Pictures/Documents/Custom Project Designs/FHIP/First.txt","r")
print(file.read(7))
file.close()

file = open("C:/Users/Administrator/OneDrive/Pictures/Documents/Custom Project Designs/FHIP/First.txt","r")
print(file.readline())
file.close()

file = open("C:/Users/Administrator/OneDrive/Pictures/Documents/Custom Project Designs/FHIP/First.txt","r")
print(file.readlines())
file.close()