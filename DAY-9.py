for i in range(12):
    if(i==10):
        break
    print('6 X ',i , '=',6*i)



for i in range(1,101,1):
    print(i)
    if(i==50):
        break
    else:
        print('dfhdbff')
print('thankyou')


print('hello', end='')
print('world')

print("Hello", end="")
print("World")
# Output: HelloWorld

print("Hello", end="***")
print("World")
# Output: Hello***World


print("apple", "banana", "cherry")
# Output: apple banana cherry

print("apple", "banana", "cherry", sep=", ")
# Output: apple, banana, cherry

print("one", "two", "three", sep="-")
# Output: one-two-three

print(1, 2, 3, 4, 5, sep=" | ")
# Output: 1 | 2 | 3 | 4 | 5

#'The continue statement is used inside loops to skip the rest of the code inside the\loop for the current iteration and continue with the next iteration.'
#When Python encounters a continue statement, it immediately stops executing the remaining code in the loop body for the current iteration and jumps to the next iteration.

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)


