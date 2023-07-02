for i in range(1,7):
	for j in range(1,7):
		if j==1 or j==6:
			print("*",end=" ")
		elif i==3:
			print("*",end=" ")
		elif i==4:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	for k in range(1,7):
		if k==3:
			if i==2:
				print(" ",end=" ")
			else:
				print("*",end=" ")
		else:
			print(" ",end=" ")
	print()