arr=[2,4,3,54,8]
arr1=[9,0,1,5,6]

array=arr+arr1
# print(array)
i=0
attemp=0
while i<len(array):
    j=0
    while j<len(array):
        if array[i]<array[j]:
            attemp=array[j]
            array[j]=array[i]
            array[i]=attemp
         
        j=j+1
    i=i+1
print(array)
    
            