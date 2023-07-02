for i in range(1,8):
	for j in range(1,8):
			if i==1:
				if j==1 or j==2 or j==3:
					print("*",end=" ")
				else:
					print(" ",end=" ")
			if i==2:
				if j==1 or j==4:
					print("*",end="")
				else:
					print(" ",end=" ")
			if i==3:
				if j==1 or j==3 or j==2:
					print("*",end=" ")
				else:
					print(" ",end=" ")
			if i==4:
				if j==1 or j==4:
					print("*",end="")
				else:
					print(" ",end=" ")
			if i==5:
				if j==1 or j==2 or j==3:
					print("*",end=" ")
				else:
					print(" ",end=" ")
	print()