import random

i=[random.randint(1,10) in range(10)]
print(i)


name='shashank'

for i in name:
    if i=='s':
        print('g')
    else:
        print(i)


colors=['red','green ']
for color in colors:
    print(color)
    for i in color:
        print(i)


for k in range(5):
    print(k)

for k in range(1,9,2):
    print(k)


import random

step=2

number=random.randint(1,100)*step
print(number)

number=[random.randrange(1,50,1) for _ in range(10)]
print(number)


for i in range(3):
    print(i)

i=0
while(i<3):
    print(i)
    i =i+1

count=5

while(count>0):
    print(count)
    count= count-1