def sum(a, b=0, *args, **kwargs):
    print("args value:", args)
    print("kwargs value:", kwargs)
    result = a + b

    if args:
        for arg in args:
            result += arg

    if kwargs:
        for kwarg in kwargs.values():
            result += kwarg

    return result

print(sum(1, 2, 3, 4, number=5))
