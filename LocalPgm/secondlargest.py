
arr=[10,20,30,40,50,60,70,80,90]

largest=0

secondlarget=0
for i in arr:
    if largest < i:
        secondlarget -= largest    
print(secondlarget)