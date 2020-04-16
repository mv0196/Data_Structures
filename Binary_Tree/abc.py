n=input()
num=0
z=3
for i in n:
    num+=int(i)*(2**z)
    z-=1
print(num)
