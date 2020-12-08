import time



def print_board(b):
	s=""
	for r in b:
		for c in r:
			if (c==0):
				s+=". "
			else:
				s+=str(c)+" "
		s=s[:len(s)-1]+"\n"
	print(s,end="")



def solve(b):
	dt=({1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9})
	sl=set()
	for i,k in enumerate(b):
		for j,e in enumerate(k):
			if (e!=0):
				dt[i].remove(e)
				dt[j+9].remove(e)
				dt[i//3*3+(j//3)+18].remove(e)
			else:
				sl.add(i*9+j)
	def _solve(b,dt,sl):
		while (True):
			msl=10
			ms=None
			mv=False
			for i,k in enumerate(b):
				for j,e in enumerate(k):
					if (e==0):
						s=dt[i]&dt[j+9]&dt[i//3*3+(j//3)+18]
						if (len(s)==0):
							return (None,False)
						elif (len(s)==1):
							b[i][j]=s.pop()
							dt[i].remove(b[i][j])
							dt[j+9].remove(b[i][j])
							dt[i//3*3+(j//3)+18].remove(b[i][j])
							sl.remove(i*9+j)
							mv=True
						elif (len(s)<msl):
							msl=len(s)
							ms=(i,j,s)
			if (mv==False):
				if (len(sl)!=0):
					for e in ms[2]:
						nb=[m.copy() for m in b]
						ndt=[m.copy() for m in dt]
						nsl=sl.copy()
						nb[ms[0]][ms[1]]=e
						ndt[ms[0]].remove(e)
						ndt[ms[1]+9].remove(e)
						ndt[ms[0]//3*3+(ms[1]//3)+18].remove(e)
						nsl.remove(ms[0]*9+ms[1])
						nb,nbs=_solve(nb,ndt,nsl)
						if (nbs==True):
							return (nb,True)
					return (None,False)
				return (b,len(sl)==0)
	return _solve(b,dt,sl)[0]



def solve2(b):
	r=[{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9}]
	c=[{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9}]
	sq=[{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9},{1,2,3,4,5,6,7,8,9}]
	sl=set()
	for i,k in enumerate(b):
		for j,e in enumerate(k):
			if (e!=0):
				r[i].remove(e)
				c[j].remove(e)
				sq[i//3*3+(j//3)].remove(e)
			else:
				sl.add(i*9+j)
	def _solve(b,r,c,sq,sl):
		while (True):
			msl=10
			ms=None
			mv=False
			for i,k in enumerate(b):
				for j,e in enumerate(k):
					if (e==0):
						s=r[i]&c[j]&sq[i//3*3+(j//3)]
						if (len(s)==0):
							return (None,False)
						elif (len(s)==1):
							b[i][j]=s.pop()
							r[i].remove(b[i][j])
							c[j].remove(b[i][j])
							sq[i//3*3+(j//3)].remove(b[i][j])
							sl.remove(i*9+j)
							mv=True
						elif (len(s)<msl):
							msl=len(s)
							ms=(i,j,s)
			if (mv==False):
				if (len(sl)!=0):
					for e in ms[2]:
						nb=[m.copy() for m in b]
						nr=[m.copy() for m in r]
						nc=[m.copy() for m in c]
						nsq=[m.copy() for m in sq]
						nsl=sl.copy()
						nb[ms[0]][ms[1]]=e
						nr[ms[0]].remove(e)
						nc[ms[1]].remove(e)
						nsq[ms[0]//3*3+(ms[1]//3)].remove(e)
						nsl.remove(ms[0]*9+ms[1])
						nb,nbs=_solve(nb,nr,nc,nsq,nsl)
						if (nbs==True):
							return (nb,True)
					return (None,False)
				return (b,len(sl)==0)
	return _solve(b,r,c,sq,sl)[0]



b=[[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
b=[[0,0,0,0,0,0,0,1,2],[0,0,0,0,3,5,0,0,0],[0,0,0,6,0,0,0,7,0],[7,0,0,0,0,0,3,0,0],[0,0,0,4,0,0,8,0,0],[1,0,0,0,0,0,0,0,0],[0,0,0,1,2,0,0,0,0],[0,8,0,0,0,0,0,4,0],[0,5,0,0,0,0,6,0,0]]
# b=[[8,0,0,0,0,0,0,0,0],[0,0,3,6,0,0,0,0,0],[0,7,0,0,9,0,2,0,0],[0,5,0,0,0,7,0,0,0],[0,0,0,0,4,5,7,0,0],[0,0,0,1,0,0,0,3,0],[0,0,1,0,0,0,0,6,8],[0,0,8,5,0,0,0,1,0],[0,9,0,0,0,0,4,0,0]]
# b=[[6,0,3,1,0,0,2,0,0],[0,0,0,0,4,0,0,0,7],[0,2,0,0,0,8,9,0,0],[0,0,0,0,5,0,0,0,0],[0,0,0,0,0,0,0,4,0],[2,5,0,0,0,0,0,0,1],[0,0,0,6,0,0,0,0,0],[5,9,8,0,3,0,0,0,2],[0,0,4,2,0,0,0,3,0]]
print_board(b)
s=time.time()
b=solve(b)
print(f"{round((time.time()-s)*1000)/1000}s")
print_board(b)
