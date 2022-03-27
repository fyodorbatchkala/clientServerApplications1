import json
import sys
from project_folder.common.variables import MAX_PACKAGE_LENGTH, ENCODING

sys.path.append('../')
from project_folder.decos import log
from project_folder.errors import IncorrectDataReceivedError, NonDictInputError


@log
def get_message(client):
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise IncorrectDataReceivedError
    raise IncorrectDataReceivedError


@log
def send_message(sock, message):
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)
