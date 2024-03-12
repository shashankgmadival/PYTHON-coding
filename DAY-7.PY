l='shasha'
l.upper()

l.capitalize()

l='i am good boy'
print(l.title())
l.swapcase()


i=int(input('enter the number'))

if i<0:
    print('number is negative')
elif i>0:
    if i>100:
        print('no is greater than 100')
    elif i<100:
        print('number is less than 100')
elif i == 0:
    print('number is zero')
else :
    print('number is above 100')



 
if i<0:
    print('number is negative')
elif i in range(0,100):
    print('number is in range of 100')
elif i == 0:
    print('number is zero')
else :
    print('number is above 100')

    
import time

timestap=time.strftime('%H:%M:%S')
print(timestap)