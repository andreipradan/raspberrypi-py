from functools import wraps


def logged(prefix=None, message=None):
    def decorate(func):
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            if args[0].verbose:
                if kwargs.get('leds'):
                    if set(args[0].all) != set(kwargs['leds']):
                        print('{}: {}'.format(kwargs['leds'], logmsg))
                    else:
                        print('All Leds: {}'.format(logmsg))
            return func(*args, **kwargs)
        return wrapper
    return decorate
