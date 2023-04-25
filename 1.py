def recursive_sum(*args):
    print(type(args))
    if len(args) == 0:
        return 0
    else:
        return args[0] + recursive_sum(*args[1:])

numbers = [1,2,3,4,5]
print(type(numbers))
print(recursive_sum(*numbers))


