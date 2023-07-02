for i in range(1,9):
	for j in range(1,9):
		if j==1:
			print("*",end=" ")
		elif i==1:
			if j==6 or j==7 or j==8 or j==5:
				print(" ",end=" ")
			else:
				print("*",end=" ")
		elif i==2:
			if j==5:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		elif i==3:
			if j==5:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		elif i==4:
			if j==6 or j==7 or j==8 or j==5:
				print(" ",end=" ")
			else:
				print("*",end=" ")
		else:
			print(" ",end=" ")
	print()