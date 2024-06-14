import logging
import functools


def put_log_info(filename, f, args, kwargs, result):
    try:
        logger_instance = logging.getLogger("function_details")
        logger_instance.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(filename, mode="a", encoding="utf-8")
        file_handler.setLevel(logging.INFO)
        file_formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
        file_handler.setFormatter(file_formatter)
        logger_instance.addHandler(file_handler)

        log_message_list = []
        log_message_list.append(f'name: {f.__name__}')
        log_message_list.append(f'args: {args.__str__()}')
        log_message_list.append(f'kwargs: {kwargs.__str__()}')
        log_message_list.append(f'result: {result.__str__()}')
        logger_instance.info(' | '.join(log_message_list))
    except Exception as e:
        print(e)
    finally:
        logger_instance.handlers.clear()

#-----------------------------------------------------------------------------------------------------------------------

def logger(old_function):
    @functools.wraps(old_function)
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        put_log_info('main.log', old_function, args, kwargs, result)
        return result
    return new_function


def logger_by_filename(path):
    def __logger(old_function):
        @functools.wraps(old_function)
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            put_log_info(path, old_function, args, kwargs, result)
            return result
        return new_function
    return __logger
