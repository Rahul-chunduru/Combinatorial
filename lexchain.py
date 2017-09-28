import copy
def chainer(a):
	b = []
	if(a == []):
	 	return b
	else:
		r = a[0]
		c = chainer(a[1:])
		b = copy.deepcopy(c)
		for x in c:
			x.reverse()
			x.append(r)
			x.reverse() 

		c.reverse() ; 	
		c.append([r]);
		c.reverse() ;  
		c.extend(b) ; 
		return c;

def stringer(l):
	j = ''
	for x in l:
		j = j + x ; 
	return j ;

def lister(s):
	if(s == ''):
		return [] ; 
	else:
		a = s[-1]
		c = lister(s[0:-1])
		c.append(a)
		return c;

def printer(l):
	s = ''
	while(l != []):
		print(l[0])
		l = l[1:]	
	

y = int(input())
for z in range(y):
    x = input()
    x = ''.join(sorted(x))
    K = lister(x)
    printer(list(map(stringer, chainer(K))))