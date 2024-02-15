# list

food=['dosa','idli','sambar','ice-cream']

food[0]='sushi'

food

food.append('dosa') # it will add the item in last position
food

food.remove('dosa')
food

food.pop() # it will remove the last variable
food

food.insert(0,'pizza') #it will insert pizza in index 0
food

food.sort()
food

food
food.insert(2,'ice-cream')
food

# insert 10 in between 3 and 4 
list=[1,2,3,4,5,6]
list.insert(3,10)
list

for i in list:
    print(i)


# 2D-LIST
    
drinks=['coffee','soda','tea']
dinner=['pizza','hamburger','hotdog']
dessert=['cake','ice-cream']

food=[drinks,dinner,dessert]

print(food)

print(food[0][2])
print(food[2][1])


# Tuple

student=('shasha',20,'male')
print(student.count('shasha')) # it counts how many times "shasha" is repeated
print(student.index('male'))

for i in student :
    print(i)

if "shasha" in student:
    print('yes')
else:
    print('no')


# set
    
utensile={'fork','knife','spoon'}

for x in utensile:
    print(x)

utensile.add('napkin')
utensile
utensile.remove('knife')
utensile


dish={'bowl','plate','cup'}
utensile.update(dish) # it will update the utensiles with dish elements
utensile

