for i in range(1,7):
	for j in range(1,7):
		if j==1:
			print("*",end=" ")
		elif i==1:
			if j==5 or j==6:
				print(" ",end=" ")
			else:
				print("*",end=" ")
		elif i==3:
			if j==5 or j==6:
				print(" ",end=" ")
			else:
				print("*",end=" ")
		elif i==4:
			if j==5 or j==6:
				print(" ",end=" ")
			else:
				print("*",end=" ")
		elif i==6:
			if j==5 or j==6:
				print(" ",end=" ")
			else:
				print("*",end=" ")
		else:
			print(" ",end=" ")
	print()