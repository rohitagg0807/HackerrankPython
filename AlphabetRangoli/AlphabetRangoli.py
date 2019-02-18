import string
N = int(input("Enter the size of Rangoli to make:"))
mid = N-1
for i in range (N-1,0,-1):
	row = ['-']*(2*N-1)
	for j in range(N-1,-1,-1):
		if not((i+j >=N)):
			row[mid-j]=row[mid+j]=string.ascii_lowercase[i+j]
	print('-'.join(row))

for i in range(0,N):
	row = ['-']*(2*N-1)
	for j in range(0,N):
		if not((i+j >=N)):
			row[mid-j]=row[mid+j]=string.ascii_lowercase[i+j]
	print('-'.join(row))