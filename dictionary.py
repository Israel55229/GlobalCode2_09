# Dictionary In Python
people = {
    'John': 40,
    'Phil': 50,
    'Sarah': 27
}

users = {
    'James': 'password1',
    'Fred': 'password2',
    'Jane': 'password3',
    'Kobby': 'password4'

}

username = input('Enter the username: ')
password = input("Enter the user password: ")

if users[username] == password:
    print("Login successful!")
else:
    print("Invalid user cridentials!")


