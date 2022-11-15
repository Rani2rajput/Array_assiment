list=[5,8,9,4,0,8,6,0,9]
i=0
array=[]
while i<len(list):
    if list[i] not in array:
        array.append(list[i])
    i=i+1
print(array)
