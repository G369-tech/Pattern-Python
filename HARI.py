for i in range(1,8):
	for j in range(1,8):
		if j==1 or j==7:
			print("*",end=" ")
		elif i==4:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	for k in range(1,8):
		if i==7:
			if k==1:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		elif i==6:
			if k==2:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		elif i==5:
			if k==3 or k==4 or k==5 or k==6 or k==7:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		elif i==4:
			if k==4 or k==5 or k==6 or k==7:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		elif i==3:
			if k==5:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		elif i==2:
			if k==6:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		elif i==1:
			if k==7:
				print("*",end=" ")
			else:
				print(" ",end=" ")
	for j in range(1,8):
		if i==2:
			if j==1:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		elif i==1:
			print(" ",end=" ")
		elif i==3:
			if j==2:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		elif i==4:
			if j==3 or j==2 or j==1:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		elif i==5:
			if j==4 or j==3 or j==2 or j==1:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		elif i==6:
			if j==5:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		elif i==7:
			if j==6:
				print("*",end=" ")
			else:
				print(" ",end=" ")
	for j in range(1,9):
		if j==1:
			print("*",end=" ")
		elif i==1:
			if j==5 or j==6 or j==7 or j==8:
				print(" ",end=" ")
			else:
				print("*",end=" ")
		elif i==4:
			if j==5 or j==6 or j==7 or j==8:
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
		elif i==5:
			if j==4 or j==5:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		elif i==6:
			if j==5 or j==6:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		elif i==7:
			if j==6 or j==7:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		elif i==8:
			if j==7 or j==8:
				print("*",end=" ")
			else:
				print(" ",end=" ")
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