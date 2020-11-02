def age_assignment(*args, **kwargs):
    result = {}
    for n in args:
        result[n] = kwargs[n[0]]
    return result
