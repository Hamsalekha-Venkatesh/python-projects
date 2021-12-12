num1 = 100
num2 = 23

print(f"min between num1 & num2 is: {min(num1, num2)}")
print(f"min between num1 & num2 is: {max(num1, num2)}")

# lambdas --> Anonymous functions in Python that returns some value
triple = lambda num: num * num1
print(triple(7))

concat_list = ["my", " age is ", 27, 0.555]
concatinate_string = lambda input: str(input[0]) + str(input[1]) + str(input[2])

print(concatinate_string(concat_list))

# more lambdas...
orig_list = [1, 2, 3, 4, 5]
double_me = map(lambda n: n * 2, orig_list)

print(list(double_me))  # python creates a new list...
print(list(orig_list))  # original list remains unchanged...
