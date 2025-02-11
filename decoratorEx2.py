def my_decorator(func):
    def wrapper(*args):
        result = args[0];
        result /= 2
        func(result)
        result -= 1
        print("The number after is ", end='')
        return result
    return wrapper


@my_decorator
def say_hello(number):
    print("The current number is " + str(number))

# Call the function
print(say_hello(int(input("Please give a number to be modified: "))))