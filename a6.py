a=[60,80,70,30,50,10]
i=0
attemp=0
while i<len(a):
	j=0
	while j<len(a):
		if a[i]<a[j]:
			attemp=a[j]
			a[j]=a[i]
			a[i]=attemp
		j=j+1
	i=i+1
print(a)


