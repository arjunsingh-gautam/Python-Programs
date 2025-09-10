# Write a python script to print two given words in dictionary order
word1=(input("Enter word 1:"))
word2=(input("Enter word 2:"))
if word1>word2:
    print("Alphabetical order is %s,%s"%(word2,word1))
else:
    print("Alphabetical order is %s,%s"%(word1,word2))