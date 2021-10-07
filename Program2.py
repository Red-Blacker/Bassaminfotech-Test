string=input("Enter String:")
substring=input("Enter substring:")
count=0
for i in range(len(string)):
    for j in range(len(substring)):
        if string[i+j]==substring[j] and j==(len(substring)-1):
            count=count+1  
        if string[i+j]!=substring[j]:
            break  
        if i==len(string)-len(substring):
            break
print(count)           