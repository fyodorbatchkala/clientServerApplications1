import socket
import sys
import json
import logging
import argparse
from errors import *
from common.variables import DEFAULT_PORT, DEFAULT_IP_ADDRESS, MAX_CONNECTIONS, MAX_PACKAGE_LENGTH, ENCODING, ACTION,\
    TIME, USER, ACCOUNT_NAME, PRESENCE, RESPONSE, ERROR, RESPONDEFAULT_IP_ADDRESSSE
from common.utils import get_message, send_message
import time


CLIENT_LOGGER = logging.getLogger('client')


def create_presence(account_name='Guest'):
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    CLIENT_LOGGER.debug(f'Сформировано {PRESENCE} сообщение для пользователя {account_name}')
    return out


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default=DEFAULT_IP_ADDRESS, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
    return parser


def process_ans(message):
    CLIENT_LOGGER.debug(f'Разбор сообщения от сервера {message}')
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ReqFieldMissingError(RESPONSE)


def main():
    parser = create_arg_parser()
    namespace = parser.parse_args(sys.argv[1:])
    server_address = namespace.addr
    server_port = namespace.port

    if not 1023 < server_port < 65536:
        CLIENT_LOGGER.critical(f'Попытка запуска клиента с указанием неподходящего порта '
                               f'{server_port}. Допустимы адреса с 1024 до 65535. Клиент завершается.')
        sys.exit(1)

    CLIENT_LOGGER.info(f'Запущен клиент с параметрами: '
                       f'Адрес сервера: {server_address}, порт: {server_port}.')

    try:
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.connect((server_address, server_port))
        message_to_server = create_presence()
        send_message(transport, message_to_server)
        answer = process_ans(get_message(transport))
        CLIENT_LOGGER.info(f'Принят ответ от сервера {answer}')
    except json.JSONDecodeError:
        CLIENT_LOGGER.error('Не удалось декодировать полученную JSON строку.')
    except ConnectionRefusedError:
        CLIENT_LOGGER.critical(f'Не удалось подключиться к серверу {server_address}: {server_port},'
                               f'конечный компьютер отверг запрос на подключение.')
    except ReqFieldMissingError as missing_error:
        CLIENT_LOGGER.error(f'В ответе сервера отсутствует необходимое поле {missing_error.missing_field}.')


    # try:
    #     server_address = sys.argv[1]
    #     server_port = int(sys.argv[2])
    #     if server_port < 1024 or server_port > 65535:
    #         raise ValueError
    # except IndexError:
    #     server_address = DEFAULT_IP_ADDRESS
    #     server_port = DEFAULT_PORT
    # except ValueError:
    #     print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
    #     sys.exit(1)
    #
    # transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # transport.connect((server_address, server_port))
    # message_to_server = create_presence()
    # send_message(transport, message_to_server)
    #
    # try:
    #     answer = process_ans(get_message(transport))
    #     print(answer)
    # except (ValueError, json.JSONDecodeError):
    #     print('Не удалось декодировать сообщение сервара.')


if __name__ == '__main__':
    main()
