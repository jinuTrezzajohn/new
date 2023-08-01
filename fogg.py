l1=[5,6,1,2,3]
l2=['abc','def','xyz']

for i in l2:
    print(len(i))
c=0
for i in l2:
    c=0
    for j in range(len(i)):
        if i[j] in ['a','e','i','o','u']:
            c+=1
    print(c)
for i in l2:
    c=0
    for j in range(len(i)):
        if i[j] in ['a','e','i','o','u']:
            c+=1
    print(i,c)

            

for i in l1:
    print(i**2)
for i in l1:
    print(i**3)
k={}
vow=[1,1,0]
for i in range(len(l2)):
    k[l2[i]]=vow[i]
print(k)
m={}
length=[3,3,3]
for i in range(len(l2)):
    m[l2[i]]=length[i]
print(m)



