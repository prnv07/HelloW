n = int(input("Enter no. of strings to be entered\n"))
lis = []
for i in range(n):
    s = input()
    s=[x for x in s]
    num = int(len(s)/3)
    for i in range(1, num):
        s.insert(-1*(i*3)-(i-1), ",")

    lis.append("".join(s))

for s in lis:
    print(s)
