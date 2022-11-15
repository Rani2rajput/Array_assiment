numbers=[10,12,80,43]
numbers2=[90,100,67,78]
i=0
list3=numbers+numbers2
print(list3)	
x=list3
i=0
attemp=0
while i<len(x):
	j=0
	while j<len(x):
		if x[i]<x[j]:
			attemp=x[j]
			x[j]=x[i]
			x[i]=attemp
		j=j+1
	i=i+1
print(x)
