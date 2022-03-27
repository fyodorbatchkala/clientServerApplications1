import sys
import logging
import logs.config_server_log
import logs.config_client_log
import traceback
import inspect

if sys.argv[0].find('client.py') == -1:
    LOGGER = logging.getLogger('server')
else:
    LOGGER = logging.getLogger('client')


def log(func_to_log):
    def log_saver(*args, **kwargs):
        ret = func_to_log(*args, **kwargs)
        LOGGER.debug(f'Была вызвана функция {func_to_log.__name__} c параметрами {args}, {kwargs}.'
                     f'Вызов из модуля {func_to_log.__module__}.'
                     f'Вызов из функции {traceback.format_stack()[0].strip().split()[-1]}.'
                     f'Вызов из функции {inspect.stack()[1][3]}'
                     f'@@@Вызов из функции {sys._getframe().f_back.f_code.co_name}'
                     f'@@@вызов из модуля {sys._getframe().f_back.f_code.co_filename.split("/")[-1]}')
        return ret
    return log_saver
