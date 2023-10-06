import numpy 
#function to print polynomial equation
def printPoly(poly, n):
	for i in range(n):
		print(poly[i], end = "")
		if (i != 0):
			print("x^", i, end = "")
		if (i != n - 1):
			print(" + ", end = "")

# Declare Two Polynomials
P1 = ([4,1,6])
P2 = ([2,5,3])
m = len(P1)
n = len(P2)

print("First polynomial is")
printPoly(P1, m)
print("\n", end = "")
print("Second polynomial is")
printPoly(P2, n)

rx = numpy.polynomial.polynomial.polymul(P1, P2)
  
print("\nProduct polynomial is "); 
k=len(rx)
printPoly(rx,k)
