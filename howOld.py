from datetime import datetime

now = datetime.now()
yearNow = now.year

age = input("Tell me how old you are: ")
NewAge = int(age) + 100
print(f"You will be {NewAge} in 100 years")

yearWhenHundred = now.year - int(age) + 100

print(f"year is now: {yearNow}")

print(f"year you will be 100 in year: {yearWhenHundred} will be: ")