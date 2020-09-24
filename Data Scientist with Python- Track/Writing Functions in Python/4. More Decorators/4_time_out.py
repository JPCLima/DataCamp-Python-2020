# Tag your functions
def tag(*tags):
    # Define a new decorator, named "decorator", to return
    def decorator(func):
        # Ensure the decorated function keeps its metadata
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Call the function being decorated and return the result
            return func(*args, **kwargs)
        wrapper.tags = tags
        return wrapper
    # Return the new decorator
    return decorator


@tag('test', 'this is a tag')
def foo():
    pass


print(foo.tags)

# Check the return type


def returns(return_type):
    # Write a decorator that raises an AssertionError if the
    # decorated function returns a value that is not return_type
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            assert(type(result) == return_type)
            return result
        return wrapper
    return decorator


@returns(dict)
def foo(value):
    return value


try:
    print(foo([1, 2, 3]))
except AssertionError:
    print('foo() did not return a dict!')
