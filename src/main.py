import time



def print_board(b):
	s=""
	for i,k in enumerate(b):
		s+=("." if k==0 else str(k))+("\n" if i%9==8 else " ")
	print(s,end="")



def solve(b):
	a=(0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,3,4,4,5,4,5,5,6,4,5,5,6,5,6,6,7,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,3,4,4,5,4,5,5,6,4,5,5,6,5,6,6,7,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,3,4,4,5,4,5,5,6,4,5,5,6,5,6,6,7,3,4,4,5,4,5,5,6,4,5,5,6,5,6,6,7,4,5,5,6,5,6,6,7,5,6,6,7,6,7,7,8,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,3,4,4,5,4,5,5,6,4,5,5,6,5,6,6,7,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,3,4,4,5,4,5,5,6,4,5,5,6,5,6,6,7,3,4,4,5,4,5,5,6,4,5,5,6,5,6,6,7,4,5,5,6,5,6,6,7,5,6,6,7,6,7,7,8,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,3,4,4,5,4,5,5,6,4,5,5,6,5,6,6,7,3,4,4,5,4,5,5,6,4,5,5,6,5,6,6,7,4,5,5,6,5,6,6,7,5,6,6,7,6,7,7,8,3,4,4,5,4,5,5,6,4,5,5,6,5,6,6,7,4,5,5,6,5,6,6,7,5,6,6,7,6,7,7,8,4,5,5,6,5,6,6,7,5,6,6,7,6,7,7,8,5,6,6,7,6,7,7,8,6,7,7,8,7,8,8,9)
	dt=[0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff,0x1ff]
	for i,e in enumerate(b):
		if (e!=0):
			m=~(1<<(e-1))
			j,k=divmod(i,9)
			k+=9
			dt[j]&=m
			dt[k]&=m
			dt[j//3*3+k//3+15]&=m
	def _solve(b,dt):
		while (True):
			msl=10
			msi=0
			mss=0
			mv=False
			for i,e in enumerate(b):
				if (e==0):
					j,k=divmod(i,9)
					k+=9
					l=j//3*3+k//3+15
					s=dt[j]&dt[k]&dt[l]
					if (s==0):
						return None
					elif (not (s&(s-1))):
						b[i]=s.bit_length()
						m=~(1<<(b[i]-1))
						dt[j]&=m
						dt[k]&=m
						dt[l]&=m
						mv=True
					elif (a[s]<msl):
						msl=a[s]
						msi=i
						mss=s
			if (mv==False):
				if (msl!=10):
					j,k=divmod(msi,9)
					k+=9
					l=j//3*3+k//3+15
					for i in range(0,9):
						m=1<<i
						if (mss&m):
							m=~m
							nb=b[:]
							ndt=dt[:]
							nb[msi]=i+1
							ndt[j]&=m
							ndt[k]&=m
							ndt[l]&=m
							nb=_solve(nb,ndt)
							if (nb is not None):
								return nb
					return None
				return b
	return _solve(b,dt)



# b=[5,1,7,6,0,0,0,3,4,2,8,9,0,0,4,0,0,0,3,4,6,2,0,5,0,9,0,6,0,2,0,0,0,0,1,0,0,3,8,0,0,6,0,4,7,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,7,8,7,0,3,4,0,0,5,6,0,0,0,0,0,0,0,0,0,0]
# b=[0,0,0,0,0,0,0,1,2,0,0,0,0,3,5,0,0,0,0,0,0,6,0,0,0,7,0,7,0,0,0,0,0,3,0,0,0,0,0,4,0,0,8,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,8,0,0,0,0,0,4,0,0,5,0,0,0,0,6,0,0]
# b=[8,0,0,0,0,0,0,0,0,0,0,3,6,0,0,0,0,0,0,7,0,0,9,0,2,0,0,0,5,0,0,0,7,0,0,0,0,0,0,0,4,5,7,0,0,0,0,0,1,0,0,0,3,0,0,0,1,0,0,0,0,6,8,0,0,8,5,0,0,0,1,0,0,9,0,0,0,0,4,0,0]
b=[6,0,3,1,0,0,2,0,0,0,0,0,0,4,0,0,0,7,0,2,0,0,0,8,9,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,4,0,2,5,0,0,0,0,0,0,1,0,0,0,6,0,0,0,0,0,5,9,8,0,3,0,0,0,2,0,0,4,2,0,0,0,3,0]
print_board(b)
s=time.time()
b=solve(b)
print(f"{time.time()-s:.6f}s")
print_board(b)
