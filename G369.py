for i in range(1,11):
	for j in range(1,9):
		if i==2:
				if j==4 or j==5:
					print("∆",end=" ")
				else:
					print(" ",end="")
		if i==3:
				if j==2:
					print("∆",end="")
				else:
					print(" ",end="")
		if i==4:
				if j==1:
					print("∆",end="")
				else:
					print(" ",end="")
		if i==5:
				if j==1 or j==3 or j==4 or j==5 or j==6:
					print("∆",end=" ")
				else:
					print(" ",end="")
		if i==6:
				if j==2 or j==7:
					print("∆",end="")
				else:
					print(" ",end="")
		if i==7:
				if j==3 or j==7:
					print("∆",end="")
				else:
					print(" ",end="")
		if i==8:
				if j==5 or j==6:
					print("∆",end=" ")
				else:
					print(" ",end="")
	for k in range(1,6):
		if i==2:
			if k==1 or k==2 or k==3:
				print("∆",end=" ")
			else:
				print(" ",end=" ")
		if i==3:
			if k==5:
				print("∆",end=" ")
			else:
				print(" ",end=" ")
		if i==4:
			if k==5:
				print("∆",end=" ")
			else:
				print(" ",end=" ")
		if i==5:
			if k==1 or k==2 or k==4 or k==5:
				print("∆",end=" ")
			else:
				print(" ",end=" ")
		if i==6:
			if k==5:
				print("∆",end=" ")
			else:
				print(" ",end=" ")
		if i==7:
			if k==5:
				print("∆",end=" ")
			else:
				print(" ",end=" ")
		if i==8:
			if k==1 or k==2 or k==3:
				print("∆",end=" ")
			else:
				print(" ",end=" ")
	for p in range(1,7):
		if i==2:
			if p==3 or p==4:
				print("∆",end=" ")
			else:
				print(" ",end=" ")
		if i==3:
			if p==3:
				print("∆",end=" ")
			else:
				print(" ",end=" ")
		if i==4:
			if p==2:
				print("∆",end=" ")
			else:
				print(" ",end=" ")
		if i==5:
			if p==1 or p==2 or p==3 or p==6 or p==5:
				print("∆",end=" ")
			else:
				print(" ",end=" ")
		if i==6:
			if p==2 or p==6:
				print("∆",end=" ")
			else:
				print(" ",end=" ")
		if i==7:
			if p==3 or p==6:
				print("∆",end=" ")
			else:
				print(" ",end=" ")
		if i==8:
			if p==3 or p==4:
				print("∆",end=" ")
			else:
				print(" ",end=" ")
	for h in range(1,9):
		if i==2:
			if h==2 or h==1:
				print("∆",end=" ")
			else:
				print(" ",end=" ")
		if i==3:
			if h==1 or h==4:
				print("∆",end=" ")
			else:
				print(" ",end=" ")	
		if i==4:
			if h==1 or h==4:
				print("∆",end=" ")
			else:
				print(" ",end=" ")
		if i==5:
			if h==2 or h==1:
				print("∆",end="")
			else:
				print(" ",end="")
		if i==6:
			if h==4:
				print("∆",end=" ")
			else:
				print(" ",end=" ")
		if i==7:
			if h==4 or h==1:
				print("∆",end=" ")
			else:
				print(" ",end=" ")
		if i==8:
			if h==2 or h==1:
				print("∆",end=" ")
			else:
				print(" ",end=" ")
	print()