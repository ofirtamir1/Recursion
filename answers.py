#ex1
def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)
#ex2

def Factorial(n):
    if n == 1:
        return 1
    else:
        return n * Factorial(n - 1)

#print(Factorial(5))

#ex3
def x(n):
    if n%2==0:
        if n== 2:
            return 2
        return n+x(n-2)
    else:
        if n==1:
            return 1
        return n + x(n - 2)

#print(x(7))
#ex4

