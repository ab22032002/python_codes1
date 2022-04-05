# matrix multiplication
a = []
c = []
e = []
n=int(input("enter the sizee of the array "))
for i in range(n):
    b=[]
    for j in range(n):
        b.append(int(input()))
    a.append(b)

for i in range(n):
    for j in range(n):
        print(a[i][j],end=" ")
    print()
print("entering the element in decond array use every time the ENTER  to enter")
for i in range(n):
    d=[]
    for j in range(n):
        d.append(int(input()))
    c.append(d)
for i in range(n):
    for j in range(n):
        print(c[i][j],end=" ")
    print()
print("printing the sum of the array ")
f=[[0,0],[0,0]]
for i in range(n):
    for j in range(n):
        f[i][j]=c[i][j]+a[i][j]
    # e.append(f)
for i in range(n):
    for j in range(n):
        print(f[i][j],end=" ")
    print()