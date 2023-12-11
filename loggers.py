from datetime import datetime



def logger(old_function):

    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        log = [
            f'date:{datetime.now()}; '
            f'name:{old_function.__name__}; ',
            f'args:{args}, kwargs:{kwargs}; ',
            f'result:{result}\n',
        ]
        with open('main.log', 'a') as file:
            file.writelines(log)

        return result
    return new_function



def logger_f(path):

    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            log = [
                f'date:{datetime.now()}; '
                f'name:{old_function.__name__}; ',
                f'args:{args}, kwargs:{kwargs}; ',
                f'result:{result}\n',
            ]
            with open(f'{path}', 'a') as file:
                file.writelines(log)

            return result
        return new_function

    return __logger