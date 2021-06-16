def prod(a,b,bound):
	m = a*b
	
	if(m<=bound):
		return m
	else:
		raise ValueError(f'multiplication of {a} and {b} not possible with bound {bound}') 

    
if __name__ == 'main':
  prod(4,3,9)
  prod(2,3,7)
