for i in range(1,7):
	for j in range(1,7):
		if i==1:
			print("*",end=" ")
		elif i==2:
			if j==5:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		elif i==3:
			if j==4:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		elif i==4:
			if j==3:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		elif i==5:
			if j==2:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		elif i==6:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()