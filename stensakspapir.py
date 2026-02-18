sten = "sten"
papir = "papir"
saks = "saks"

first = input("first, vælg sten/saks/papir: ")
second = input("second, vælg sten/saks/papir: ")

if first == sten and second == papir:
    print("second win!!")
elif first == papir and second == saks:
    print ("second win!!")
elif first == saks and second == sten:
    print ("second win!!")
elif first == sten and second == sten or first == papir and second == papir or first == saks and second == saks:
    print("It's a draw!!")         
else:
    print ("first win!!")