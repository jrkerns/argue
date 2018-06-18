import functools
import inspect


def options(**option_values):

    def decorator(func):

        sig = inspect.signature(func)
        parameter_options = sig.bind_partial(**option_values).arguments

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            passed_values = sig.bind(*args, **kwargs).arguments
            for name, value in passed_values.items():
                if name in parameter_options:
                    if value not in parameter_options[name]:
                        raise ValueError("Argument '{}' passed to '{}' was not one of the allowed options: {}".format(
                            value, func.__name__, parameter_options[name]))
            return func(*args, **kwargs)
        return wrapper
    return decorator


def bounds(**range_ends):
    for key, values in range_ends.items():
        if len(values) != 2:
            raise ValueError("There must only be two items per argument to define an option range")
        for value in values:
            if not isinstance(value, (int, float)):
                raise TypeError("The range values passed ({}) are not ints or floats".format(values))

    def decorator(func):

        sig = inspect.signature(func)
        start_stop = sig.bind_partial(**range_ends).arguments

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            passed_values = sig.bind(*args, **kwargs).arguments
            for name, value in passed_values.items():
                if name in start_stop:
                    start = start_stop[name][0]
                    stop = start_stop[name][1]
                    if start > value or value > stop:
                        raise ValueError("Argument '{}' passed to '{}' was not in the range: ({}, {})".format(
                            value, func.__name__, start, stop))
            return func(*args, **kwargs)
        return wrapper
    return decorator


def conditional(**conditions):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for key, value in conditions.items():
                if getattr(args[0], key) != value:
                    raise ValueError("Condition self.{} != {} which is required to continue".format(key, value))
            return func(*args, **kwargs)
        return wrapper
    return decorator
