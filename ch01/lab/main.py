import random

# Part A
weeks = 16
print(weeks, type(weeks))
classes = 5
print(classes, type(classes))
tuition = 6000
print(tuition, type(tuition))
cost_per_week = ((tuition/classes)/weeks)
print ("Cost per week:", cost_per_week, (type(cost_per_week)))
classes_per_week = 3
print ("Classes per week:", classes_per_week, type(classes_per_week))
cost_per_class = (cost_per_week/classes_per_week)
print ("Cost per class:",cost_per_class, type(cost_per_class))

# Part B
mylist = [1,2,3,4,5,6,7,8,9,10]
print("Your random number is:", random.choice(mylist))

