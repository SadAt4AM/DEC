from loggers import logger_f


def flat_generator(list_of_lists):
    for i in list_of_lists:
        for k in i:
            yield k


@logger_f(path='logged_gen.log')
def fg(list_of_lists):
    return tuple(flat_generator(list_of_lists))


list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

if __name__ == '__main__':
    fg(list_of_lists_1)