#Day 2: 30 Days of python programming
first_name = 'Glender'
last_name = 'Miranda'
full_name = 'Glender Miranda'
country = 'Ecuador'
city = 'my_city'
age = 23
year = 2024
is_married = False
is_true = True
is_light_on = False
one, two, three = 1,2,3


#Data Types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(one))
print(type(two))
print(type(three))

#len()
print(len(first_name))
print(len(last_name))

#4
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

#5
radius = 30
area_of_circle = 3.14 * radius**2
circum_of_circle = 3.14 * 2 * radius

user_radius = float(input('Ingrese el radio: '))
area_of_circle = 3.14 * user_radius**2

#6
#Note: Do not forget to cast variables
first_name = input('first name:')
last_name = input('last name:')
full_name = input('full name:')
country = input('country:')
city = input('city:')
age = int(input('age:'))
year = int(input('year:'))
is_married = bool(input('is married:'))
is_true = bool(input('is true:'))
is_light_on = bool(input('is light on:'))


#Verifying variable types are the same
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#7
help('keywords')