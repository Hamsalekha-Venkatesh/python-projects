batman = "bruce wayne"
print(batman[2])
print(batman[-2])

# Slicing of strings
name = "My name is Hamsalekha Venkatesh. I love to program in Python!"

print(name[1:len(name):2])
my_boolean = False
if my_boolean:
    print("I'm true")
else:
    print("I'm not true")

name = None
if name is None:
    print(f"not null {name}")
else:
    print(f"name is numm {name}")

# String concatenation
name1 = "Hamsa"
name2 = "lekha "
print("My full name is : " + name1 + name2)
print("sale" in name1 + name2)

# Complex arithmetic operations
x = 20
y = 5
result1 = (x + True)
print(result1)
result2 = (4 - y * False)
print(result2)

print(result1 / result2)

# Conditional  statements


def check_my_status(num: int):
    if num % 2 == 0 and num % 3 == 0 and num % 4 == 0:
        print(f"this number {num} is divisible by 2,3 & 4")
    elif num % 2 == 0 and num % 3 == 0:
        print(f"this number {num} is ONLY divisible by 2,3 & NOT 4")
    else:
        print(f"this number {num} is NOT divisible by 2,3 & 4")


num = 12
check_my_status(num)
check_my_status(18)


# Conditional Expressions/ Ternary operators
num1 = 45
num2 = 233
ans1 = "Number is < 100" if num1 < 100 else "Number > 100"
print(f"Num1 judgement: {ans1}")

ans2 = "Number < 100" if num2 < 100 else "Number > 100"
print(f"Num2 judgement:  {ans2}")
