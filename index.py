def print_board(b):
	s=""
	for r in b:
		for c in r:
			if (c==0):
				s+=". "
			else:
				s+=str(c)+" "
		s=s[:len(s)-1]+"\n"
	print(s)



def solve(_b):
	def list_and(a,b):
		c=[]
		for e in a:
			if (e in b):
				c.append(e)
		for e in b:
			if (e in a and e not in c):
				c.append(e)
		return c
	def list_equals(a,b):
		for e in a:
			if (e not in b):
				return False
		for e in b:
			if (e not in a):
				return False
		return True
	def list_copy(a):
		b=[]
		for e in a:
			b.append(e)
		return b
	b=[]
	for y in range(len(_b)):
		l=[]
		for x in range(len(_b[0])):
			l.append(_b[y][x])
		b.append(l)
	while True:
		moved=False
		for y in range(len(b)):
			for x in range(len(b[0])):
				if (b[y][x]==0 or type(b[y][x])==list):
					b[y][x]=[i for i in range(1,10)]
		for y in range(len(b)):
			l=[i for i in range(1,10)]
			for x in range(0,len(b[0])):
				if (type(b[y][x])!=list):
					l.remove(b[y][x])
			for x in range(0,len(b[0])):
				if (type(b[y][x])==list):
					b[y][x]=list_and(b[y][x],l)
		for x in range(len(b[0])):
			l=[i for i in range(1,10)]
			for y in range(0,len(b)):
				if (type(b[y][x])!=list):
					l.remove(b[y][x])
			for y in range(0,len(b)):
				if (type(b[y][x])==list):
					b[y][x]=list_and(b[y][x],l)
		for i in range(3):
			for j in range(3):
				l=[i for i in range(1,10)]
				for x in range(i*3,i*3+3):
					for y in range(j*3,j*3+3):
						if (type(b[y][x])!=list):
							l.remove(b[y][x])
				for x in range(i*3,i*3+3):
					for y in range(j*3,j*3+3):
						if (type(b[y][x])==list):
							b[y][x]=list_and(b[y][x],l)
		ml,mp=10,[-1,-1]
		for y in range(len(b)):
			for x in range(len(b[0])):
				if (type(b[y][x])==list and len(b[y][x])<ml):
					ml=len(b[y][x])
					if (ml==0):
						return (b,False,-1)
					if (ml==1):
						b[y][x]=b[y][x][0]
						moved=True
						break
					else:
						mp=[x,y]
		if (moved==False and ml<10):
			x,y=tuple(mp)
			l=list_copy(b[y][x])
			for v in l:
				b[y][x]=v
				_,s,p=solve(b)
				if (p==100):
					return (b,True,100)
				if (s==True):
					moved=True
					break
			if (moved==False):
				return (b,False,-1)
		end=True
		d=0
		for y in range(len(b)):
			for x in range(len(b[0])):
				if (type(b[y][x])==list):
					end=False
				else:
					d+=1
		p=int(d/81*100)
		if (end==True):
			for y in range(len(b)):
				l=[i for i in range(1,10)]
				for x in range(0,len(b[0])):
					if (type(b[y][x])!=list):
						if (b[y][x] not in l):
							end=False
							break
						l.remove(b[y][x])
				if (len(l)>0 or end==False):
					end=False
					break
			if (end==False):
				continue
			for x in range(len(b[0])):
				l=[i for i in range(1,10)]
				for y in range(0,len(b)):
					if (type(b[y][x])!=list):
						if (b[y][x] not in l):
							end=False
							break
						l.remove(b[y][x])
				if (len(l)>0 or end==False):
					end=False
					break
			if (end==False):
				continue
			for i in range(3):
				for j in range(3):
					l=[i for i in range(1,10)]
					for x in range(i*3,i*3+3):
						for y in range(j*3,j*3+3):
							if (type(b[y][x])!=list):
								if (b[y][x] not in l):
									end=False
									break
								l.remove(b[y][x])
						if (end==False):
							break
					if (len(l)>0 or end==False):
						end=False
						break
				if (end==False):
					break
		print(str(p)+"%")
		if (moved==False or end==True):
			return (b,end,p)



b=[[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
# b=[[0,0,0,0,0,0,0,1,2],[0,0,0,0,3,5,0,0,0],[0,0,0,6,0,0,0,7,0],[7,0,0,0,0,0,3,0,0],[0,0,0,4,0,0,8,0,0],[1,0,0,0,0,0,0,0,0],[0,0,0,1,2,0,0,0,0],[0,8,0,0,0,0,0,4,0],[0,5,0,0,0,0,6,0,0]]
print_board(b)
b,_,_=solve(b)
print_board(b)