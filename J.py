for i in range(1,8):
	for j in range(1,8):
		if j==5:
			if i==6 or i==7:
				print(" ",end="")
			else:
				print("*",end="")
		if j==4:
			if i==6:
				print("*",end="")
			else:
				print(" ",end="")
		if j==3:
			if i==6:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		if j==2:
			if i==5:
				print("*",end="")
			else:
				print(" ",end="")
		else:
			print(" ",end="")
	print()