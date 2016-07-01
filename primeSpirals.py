#! /usr/bin/env

import sys, bitmap

"""
	Author: Sam Scheding

	The following program constructs prime spirals, which are anti-clockwise square spirals that highlight the
	tendency for prime numbers to follow the quadratic 4x^2+bx+c. 

	Although this is just a quick script, it provides some challenging logical problems, such as how to print 
	numbers from left to right so they form a spiral. My solution(definitely not the only solution) 
	is to split the square into four triangles (top, bottom left, and right) that grow from the centre. 
	The top and bottom triangles are easier to construct as each horizontal line consists of a contiguous set 
	of numbers. For each line in the top and bottom triangles, the first and last values of each line determine
	the corrosponding line values for the left and right triangles. eg: if the current line is:

	5 4 3

	Then the next lines left triangle will start with 5+1 and the right triangle will start with 3-1. These
	are pushed and appended to the right and left triangle lists respectively and used for constructing the 
	next line. Similarly, we can mirror this logic to construct the bottom half of the pattern.

	To run the file:

	 	python primeSpirals.py <width>

	 TODO:
	 	- Make a better isPrime() function, maybe add a prime sieve?
	 	- Rather than print, render a BMP from the data so the patterns can be seen for larger values

"""

primesBool = True
image = []

def main():

	width = int(sys.argv[1])
	leftTriangle = []
	rightTriangle = []

	if width < 0: 
		sys.exit("Needs to be positive")
	if width % 2 == 0:
		sys.exit("Needs to be an odd number")

	cellWidth = len(str(width**2)) #cell width for all numbers needs to be as large as the largest number

	constructTopHalf(leftTriangle, rightTriangle, width, cellWidth)
	constructBottomHalf(leftTriangle, rightTriangle, 1, cellWidth, width)	

	bitmap.bmp(image, width)
# Recursively called for each line in the top half
# Divides the line up into top, left, and right triangles
def constructTopHalf(leftTriangle, rightTriangle, lineWidth, cellWidth):

	if(lineWidth == 1):
		return

	x = 0	
	while x < len(leftTriangle): # print left triangle
		leftTriangle[x]+=1
		formattedPrint(leftTriangle[x], cellWidth)
		x+=1

	leftTriangle.append(getTopLeftCorner(lineWidth))
	topLeftCorner = leftTriangle[len(leftTriangle)-1]

	x=lineWidth
	while x > 0:

		formattedPrint(topLeftCorner, cellWidth)
		topLeftCorner-=1
		x-=1

	x=0
	while x < len(rightTriangle):
		formattedPrint(rightTriangle[x], cellWidth)
		rightTriangle[x]-=1
		x+=1

	print '\n'
	rightTriangle.insert(0, topLeftCorner)
	constructTopHalf(leftTriangle, rightTriangle, lineWidth-2, cellWidth)

# Recursively called for each line in the bottom half
# Divides the line up into top, left, and right triangles
def constructBottomHalf(leftTriangle, rightTriangle, lineWidth, cellWidth, width):
	
	if(lineWidth >= width+1):
		return

	currentBottomLeft = getBottomLeftCorner(lineWidth)
	x = 0
	while x < len(leftTriangle):
		leftTriangle[x]+=1
		formattedPrint(leftTriangle[x], cellWidth)
		x+=1

	if len(leftTriangle) !=0: leftTriangle.pop()

	x=0
	while x < lineWidth:

		x+=1
		formattedPrint(currentBottomLeft, cellWidth)
		currentBottomLeft+=1

	x=0
	while x < len(rightTriangle):

		formattedPrint(rightTriangle[x], cellWidth)
		rightTriangle[x]+=1
		x+=1

	if len(rightTriangle) !=0: rightTriangle.pop(0)

	print '\n'
	constructBottomHalf(leftTriangle, rightTriangle, lineWidth+2, cellWidth, width) # Do the same for the next line

def getTopLeftCorner(lineWidth):
	return (getBottomRightCorner(lineWidth) - ((lineWidth-1)*2)) 

# The spiral is also a square, and as such the bottom right corner lines up to the square of the width
def getBottomRightCorner(lineWidth): 
	return lineWidth**2

# Since for each square in the spiral the bottom row is an ascending set of numbers, we can leverage getBottomRightCorner()
# to calculate the bottomLeftCorner
def getBottomLeftCorner(lineWidth): 
	return (getBottomRightCorner(lineWidth)-lineWidth+1)

def formattedPrint(number, cellWidth):

# Print to bitmap
	# if isPrime(number):
	# 	image.append([0xFF])

# Print to console

	if primesBool == True:
		if(isPrime(number)):
		 	print "%*s" % (cellWidth, number),
		else:
			print "%*s" % (cellWidth, " "),
	else:
		 print "%*s" % (cellWidth, number),

def isPrime(n):

    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False    

    return True

if __name__ == '__main__':
	main()