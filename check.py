import os

#To check if file exist or not
if os.path.exists("C:/Users/Administrator/OneDrive/Pictures/Documents/Custom Project Designs/FHIP/Third.txt"):
    os.remove("C:/Users/Administrator/OneDrive/Pictures/Documents/Custom Project Designs/FHIP/Third.txt")
else:
    print("There is no file with name Third.txt")