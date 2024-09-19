


# Read the file print content 
# reading = open('fil1.txt','r')
# b=reading.readline()
# print(b)
# reading.close()


#Use the append mode to add in existing file 
# writign=open("fil1.txt","a")
# writign.write("Welcome to Python ") 
# writign.close()


# check the file is preesent or not 
# import os
# file='fil1.txt'
# # print("Current Directory:", os.getcwd())
# if os.path.isfile(file):
#     print(f"{file } existes")
# else:
#     print(f"{file} does not existes")


# # count the lines 

# counting = open("fil1.txt","r")
# count=counting.readline()
# print(len(count))


# read first lines
# count=open('fil1.txt','r')
# first_line=count.readline()
# print(first_line)


# Read the lines separate it and agin stor in the list 

# file1='fil1.txt'
# read = open(file1,'r')
# b=list(line)
# print(b)

#stor arr  value into the file 
# arr=[1,2,3,4,5,6,7,8]
# file='fil1.txt'

# add= open(file,"w")
# for i in arr:
#     add.write(f"{i} \n")
# print(f"number of line in {file}")



#copy the content in new file 
# add=open("fil1.txt","r")
# copy=add.read()
# add2=open("merges.txt","w")
# c=add2.write(copy)
# print("content copieds ")

#cound particular word 

word = open("fil1.txt","r")
wording=word.readlines()

for i in word:
    if i == "error":
        print(i)

print(word)
