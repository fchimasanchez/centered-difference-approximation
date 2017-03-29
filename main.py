# This script demonstrates the centered-difference approximation to the derivative of a function. Specifically, while
# test $f(x) = sin^2 x$ at the point $x = 1$. The step size is set at $h = 1$ and with each iteration, reduced by a factor
# of 10. Algorithm is iterated until the error in approximation is less than $10^{-8}$

import math

p = 1 # Evaluate functions at $x = 1$
h = 1 # Initial step size
error = 1 # Set error artificially high to initialize
j = 0 # Initial number of iterations

# Actual algorithm part
while error > 1e-8:
  Df = ((math.sin(p+h))**2-(math.sin(p-h))**2)/(2*h) # Centered-difference formula
  error = abs(Df - math.sin(2*p)) # Error made in approximation
  h = 0.1 * h # Reduce step size by factor of 10
  j = j + 1
  
print(j,"iterations needed for convergence")
