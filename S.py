for i in range(1,9):
	for j in range(1,9):
		if i==2:
			if j==1 or j==5:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		if i==1:
			if j==2 or j==4 or j==3:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		if i==3:
			if j==2:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		if i==4:
			if j==3:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		if i==5:
			if j==4:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		if i==6:
			if j==1 or j==7:
				print("*",end=" ")
			else:
				print("",end=" ")
		if i==7:
			if j==2 or j==4 or j==3:
				print("*",end=" ")
			else:
				print(" ",end=" ")
	print()