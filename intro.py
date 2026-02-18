dic = {}
dic["name"] = "kasper"

age = int(input("Give me your age: "))

dic["age"] = age

for key, value in dic.items():
    with open ("file.txt", 'w') as file:
        file.write(str(value))
        print(value)

print(dic)