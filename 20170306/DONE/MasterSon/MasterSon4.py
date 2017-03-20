dict = {}
def alphacount(value):
	alp="abcdefghijklmnopqrstuvwxyz"
	vcount=0
	
	for i in alp:
		vcount=value.count(i)
		if(vcount > 0):
			dict[i]=vcount	
	print(dict)	
		
if __name__ == '__main__':
	alphacount("netmarblegames")