a=[1,2,3,4,5]
b=[6,3,8,9,4]
i=0
li=[]
union=0
while i<len(a):
        if a[i]  not in b:
                li.append(a[i])
        if b[i] in a:
                li.append(b[i])
        else:
                li.append(b[i])
        i=i+1

print(li)
j=0
list=[]
while j<len(b):
    if b[j] in a:
        list.append(b[j])
    j=j+1
print(list)


