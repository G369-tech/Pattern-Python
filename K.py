for i in range(1,9):
	for j in range(1,9):
		if j==1:
			if i==8:
				print(" ",end=" ")
			else:
				print("*",end=" ")
		if j==2:
			if i==5:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		if j==3:
			if i==4:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		if j==4:
			if i==3 or i==5:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		if j==5:
			if i==2 or i==6:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		if j==6:
			if i==1 or i==7:
				print("*",end=" ")
			else:
				print(" ",end=" ")
	print()