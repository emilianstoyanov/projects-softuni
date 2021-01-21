# *args

def some_func(*args):
    print(args)


some_func(1, 2, 3)
some_func("peter", "george")
some_func(True, False)


def f(*args):
    current_min = args[0]
    for x in args:
        if x < current_min:
            current_min = x
    print(current_min)


f(1, 2, 3, 4, 5, 6)  # 1
f(1, 2, 3, 4, 5, 6, -4)  # -4

# всички стойности отиват в *args  / tuple /


def f_kwargs(**kwargs):
    print(kwargs)


f_kwargs(name="Pesho", age=11)
# {'name': 'Pesho', 'age': 11}


def my_min(x, *args):
    current_min = x
    for x in args:
        if x < current_min:
            current_min = x
    print(current_min)


my_min(10, 1)
# Задължително се подават данни, иначе хвърля грешка.
# Намираме най-малкото число.


def f(x, **kwargs):
    print(x)
    print(kwargs)
f(3, name = " Pesho", age = 11)
# 3
# {'name': ' Pesho', 'age': 11}


def f2(*args, **kwargs):
    print(args)
    print(kwargs)


f2(3, name=" Pesho", age=11)
# (3,)
# {'name': ' Pesho', 'age': 11}




def f3(x, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)

f3(3, name=" Pesho", age=11)



