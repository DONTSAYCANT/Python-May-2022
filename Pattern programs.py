
#Links for reference

https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/
https://www.programiz.com/python-programming/examples/pyramid-patterns
https://www.edureka.co/blog/python-pattern-programs/




#Program 1: printing stars in pyramid pattern
def starpyr(n):
	
	# outer loop to handle number of rows
	# n in this case
	for i in range(0, n):
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("*",end="")  #have fun playing around with the "" usage here to increase or decrease the number of spaces between each star
	
		# ending line after each row
		print("\r")  #here |n is also a valid option if you choose to use it. I will switch between |r and |n to show the difference but they will give you similar output in the end


n = 5
starpyr(n)




#Program 2: printing stars in reverse pyramid pattern

n=5;i=0
while(i<=n):
    print(" " * (n - i) +"*" * i)
    i=i+1




#Program 3: printing stars in triangle pattern


def str_tri(n):
	
	# number of spaces
	k = n - 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces
		# values changing acc. to requirement
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k after each loop
		k = k - 1
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ", end="")
	
		# ending line after each row
		print("\n")

n = 5
str_tri(n)




#Program 4: printing numbers in pyramid pattern



def numpat(n):
	
	# initialising starting number
	num = 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# re assigning num
		num = 1
	
		# inner loop to handle number of columns
			# values changing acc. to outer loop
		for j in range(0, i+1):
		
				# printing number
			print(num, end=" ")
		
			# incrementing number at each column
			num = num + 1
	
		# ending line after each row
		print("\n")

n = 5
numpat(n)



# Program 5: printing numbers in a pyramid pattern without recurrence
def contnum(n):
	
	# initializing starting number
	num = 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# The difference between program 4 and 5 is that we do not re assign num

	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing number
			print(num, end=" ")
		
			# incrementing number at each column
			num = num + 1
	
		# ending line after each row
		print("\r")

n = 5
contnum(n)




# Program 6: printing alphabet in a pyramid pattern
def alpat(n):
	
	# initializing value corresponding to 'A'
	# ASCII value
	num = 65 #65 is the ASCII value for A 

	# outer loop to declare number of rows
	# 5 in this case
	for i in range(0, n):
	
		# inner loop to declare number of columns
		# values changing according to outer loop
		for j in range(0, i+1):
		
			#converting ASCII number to char
			ch = chr(num)
		
			print(ch, end="   ")   
	
		# incrementing number, ASCII values come in order, so ASCII value of A is 65, B is 66 and so on
		num = num + 1
	
		# ending line after each row
		print("\n")

n = 5
alpat(n)




# Program 7: printing alphabet in a pyramid pattern without recurrence

def contalpat(n):

# initializing value corresponding to 'A'
        # ASCII value
    num = 65


# outer loop to handle number of rows
    for i in range(0, n):

# inner loop to handle number of columns
# values changing acc. to outer loop
        for j in range(0, i+1):

# explicitly converting to char
            ch = chr(num)

# printing char value
            print(ch, end="   ")

# incrementing at each column
            num = num + 1

# ending line after each row
        print("\r")

n = 5
contalpat(n)




#Program 8:printing stars in a inverted pyramid pattern

rows = int(input("Enter number of rows: ")) #changed to a user-input-based code to make it more user-friendly but it has the same end-result

for i in range(rows, 0, -1):   #decreasing number of i in each loop means number of stars in each line decreases
    for j in range(0, i):
        print("* ", end="   ")
    
    print("\n") 



