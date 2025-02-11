def my_decorator(func):
    def wrapper(*args):
        result = args[0];
        result += 1
        func(result)
        result *= 2
        print("The number after is ", end='')
        return result
    return wrapper


@my_decorator
def say_hello(number):
    print("The current number is " + str(number))

# Call the function
print(say_hello(int(input("Please give a number to be modified: "))))