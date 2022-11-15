
a=[4,34,67,12,3,10,5,2,78]
i=0
while i <len(a):
	j=0
	min=i
	while j <len(a):
		if a[min]<a[j]:
			min=j
		j=j+1
		a[i],a[min]=a[min],a[i]
	i=i+1
print(a)
