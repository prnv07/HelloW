s = input("Enter elements of list seperated by --\n")
s = s.split("--")
d={}
for i in s:
    if i not in d:
        d[i] =1
    else:
        d[i]+=1

for i in d:
    print("Frequency of ",i," = ", d[i])
