x = int(input())

if x % 3 == 0 and x %5 == 0:
    print("fizzbuzz")
elif x%5 == 0:
    print("buzz")
elif x %3 == 0:
    print("flizz")
else:
    print(x)
    