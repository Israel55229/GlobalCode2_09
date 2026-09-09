names = ['Kojo', 'Daniel', 'Ama', 'Gloria', 'Phile']
for bettle in names:
    print(bettle)

# looping using the range function
for i in range(6):
    print(i)

# Checking if a fruit exists in a list of fruits
fruits = ['Apple', 'Orange', 'Mango', 'Grape']

for fruit in fruits:
    if fruit == 'Orange':
        print(f"Yep we found the fruit {fruit}")
    else: 
        print('we do not have that fruit')


price = []
total = 0

for x in range(3):
    price.append(float(input("Enter price: ")))

for i in price:
    total += i
print(f"Total price: {total}")


