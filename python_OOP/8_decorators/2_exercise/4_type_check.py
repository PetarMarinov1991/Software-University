def type_check(type):

    def decorator(func):

        def wrapper(el):
            if isinstance(el, type):
                return func(el)
            return f'Bad Type'
        return wrapper

    return decorator
