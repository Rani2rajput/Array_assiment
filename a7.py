a=[12,54,67,3,4,58,34]
i=0
while i <len(a):
   r=a[i]
   s=i
   while s>0 and a[s-1]>r:
        a[s]=a[s-1]     
        s=s-1
   a[s]=r
   i=i+1
print(a)


