l1=[5,6,1,2,3]
l2=['abc','def','xyz']
d={}
d1={}
for i in l1:
    print(i**2)
for i in l1:
    print(i**3)
for i in range(len(l1)):
    d[i]=(l1[i]**2)
print(d)
for i in range(len(l1)):
    d1[i]=(l1[i]**3)
print(d1)
print(l1)


