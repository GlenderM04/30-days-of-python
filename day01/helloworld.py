# Day 1 - 30DaysOfPython Challenge

print(3 + 4)             # addition(+)
print(3 - 1)             # subtraction(-)
print(3 * 4)             # multiplication(*)
print(3 / 4)             # division(/)
print(3 ** 4)            # exponential(**)
print(3 % 4)             # modulus(%)
print(3 // 4)            # Floor division operator(//)

#Strings
print('Glender :D')
print('Ecuador')
print('I am enjoying 30 days of python')


# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

#Euclidian distance
p1 = 2
p2 = 3
q1 = 10
q2 = 8

dist = (((p1-q1)**2)+((p2-q2)**2))**(1/2)

print("Distancia euclidiana: ")
print(dist)