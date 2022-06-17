import sys
import traceback


def get_error_msg() -> dict:
    """
    Esta função retorna o erro tratado de forma resumida para facilitar o tratamento dos erros e evitar
    a parada da aplicação

    :return: É retornado um diconário com tipo do erro, onde começou o script e onde ocorreu o erro
    """

    exc_type, exc_value, exc_traceback = sys.exc_info()
    error_type = str(exc_value)
    called_by = str(
        repr(traceback.extract_tb(exc_traceback).__getitem__(0)).split(',')[-1]
    )
    called_by = called_by.replace('>', '')
    line_and_function = str(
        repr(traceback.extract_tb(exc_traceback).__getitem__(-1)).split(',')[
            -1
        ]
    )
    line_and_function = line_and_function.replace('>', '')

    return {
        'error': {
            'type': error_type,
            'ended': line_and_function,
            'started': called_by,
        }
    }
