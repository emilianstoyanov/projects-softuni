def even_parameters(function):
    def wrapper(*args):
        if any([n for n in args if type(n) != int or n % 2 != 0]):
            return "Please use only even numbers!"
        return function(*args)
    return wrapper
