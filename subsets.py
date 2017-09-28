import copy;
def subsets(l):
	if(l == []):
		return [[]] ; 
	else:
		a = subsets(l[:-1])
		r = l[-1]
		b = copy.deepcopy(a)
		for x in b:
			x.append(r)
		b.extend(a)
		return b ; 

j = int(input())
k = list(range(1,j+1))
print(subsets(k)) ; 				