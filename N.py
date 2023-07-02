for i in range(1,7):
	for j in range(1,i):
			if j==1:
				print("*",end=" ")
			elif j==2:
				if i==3:
					print("*",end=" ")
				else:
					print(" ",end=" ")
			elif j==3:
				if i==4:
					print("*",end=" ")
				else:
					print(" ",end=" ")
			elif j==4:
				if i==5:
					print("*",end=" ")
				else:
					print(" ",end=" ")
			elif j==5:
				if i==6:
					print("*",end=" ")
				else:
					print(" ",end=" ")
			elif j==6:
				if i==7:
					print("*",end=" ")
				else:
					print(" ",end=" ")
			else:
				print(" ",end=" ")
	for k in range(1,7):
		if k==2:
			if i==5:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		if k==3:
			if i==4:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		if k==4:
			if i==3:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		if k==5:
			if i==2:
				print("*",end=" ")
			else:
				print(" ",end=" ")
	print()