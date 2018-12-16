print("Enter no. of strings")
n = int(input())
sum = ""
for i in range(n):
    s = input().split()
    s = [x[0] for x in s]
    s = "".join(s)
    sum = sum+s+"\n"

print(sum)
