# New If statement Challenge
# A Traffic Light Challenge
print("====================")
print("|  Traffic Light   |")
print("====================")

#Taking input from the user 


light_color = input("Enter the light color: ")
light_color = light_color.upper()

if light_color == 'RED':
    print("Stop!!!")
elif light_color == 'YELLOW':
    print("Get Ready!")
elif light_color == 'GREEN':
    print("Go!!!")
else:
    print("Just keep driving")