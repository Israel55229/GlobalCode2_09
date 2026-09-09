# Challenge 3
# The Gradeding system
print("=" * 25)
print("    Grading System    ")
print("=" * 25)
print()

score = int(input("Enter your exams score: "))
if score >= 80:
    print('Grade A')
elif score >= 70:
    print('Grade B')
elif score >= 60:
    print('Grade C')

elif score >= 50:
    print('Grade D')
else:
    print('Grade F')