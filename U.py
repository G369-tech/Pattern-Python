for i in range(1,7):
	for j in range(1,7):
		if j==1:
			if i==5 or i==6:
				print(" ",end="")
			else:
				print("*",end="")
		if j==6:
			if i==5 or i==6:
				print(" ",end="")
			else:
				print("*",end="")
		if j==2:
			if i==5:
				print("*",end="")
			else:
				print(" ",end="")
		if j==3:
			if i==5:
				print("*",end="")
			else:
				print(" ",end="")
		if j==4:
			if i==5:
				print("*",end=" ")
			else:
				print("",end=" ")
		else:
			print(" ",end="")
	print()