X =[[1,2,3],[4,5,6],[7,8,9]]
Y=[[10,11,12],[13,14,15],[16,17,18]]
Z=[[0,0,0],[0,0,0],[0,0,0]]

for a in range(len(X)):
	for b in range(len(Y)):
		Z[a][b] = X[a][b]+Y[a][b]

# for i in Z:
print(Z)