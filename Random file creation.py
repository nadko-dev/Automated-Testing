# In this project I tried to create a list with file names
# I wanted python to create files using names inside a list
# After each creation the used file name should be deleted from the list to avoid duplication
# Also, the file names should be chosen randomly

import random # imported random for random number generation

fileNames = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt", "file6.txt"]
# create list with file names
i = len(fileNames) - 1
# assigned i variable the maximum index of the list

# creating loop to continue until we have all the files created from the list
while i != -1:
    randomNumber = random.randint(0, i)
    # created variable that holds random number between 0 and i
    with open(fileNames[randomNumber], 'w') as file:
        file.close()
    # creating files using list elements
    print(fileNames[randomNumber], " has been created")
    # print which file has been generated
    del fileNames[randomNumber]
    # deleting used file name
    print(fileNames)
    # print which file names are remaining inside list
    i = i - 1
    # reduce the maximum index number since list has less elements

print("All files have been created")
# print a message to show all files have been created

