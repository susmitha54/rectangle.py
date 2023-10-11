#Write code for drawing these patterns.
#Get width and length from the user.
# draw a empty rectangle woth char *
 

l = int(input("Enter the length of rectangular:"))
w = int(input("Enter the width of rectangular:"))
for i in range(0, l) :
	print ("")
	for j in range(0, w) :
		if (i == 0 or i == l-1 or j== 0 or j == w-1) :
			print("*",end=" ")
		else :
			print(" ",end=" ")
print () 






