#recursive function 

## to get a factorial of a number 

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return (n * factorial(n-1))
    
print(factorial(3))




## to get fibonacci sequence 

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(3))



# sets

s={2,3,4,5,6,3,2}
print(s)

#output={2, 3, 4, 5, 6}  sets doesn't contain duplkicate value


# to get every value use for loop 
s={2,3,4,5,6,3,2,10}
for i in s:
    print(i)