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
            
