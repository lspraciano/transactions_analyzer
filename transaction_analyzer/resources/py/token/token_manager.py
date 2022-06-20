# Imports Native
from functools import wraps
import jwt
import datetime
from flask import request, make_response
from random import *

# Created Imports
from transaction_analyzer.configuration.configuration import Configuration


def token_generator(user_id: int) -> dict:
    """
    Função geradora do TOKEN JWT de acesso do usuário. Este TOKEN deve ser armazenado nos cookies como local
    padrão

    :param user_id: ID - identificação do usuário
    :return: dicionário contendo TOKEN de acesso no formato {"token": foo}
    """

    if type(user_id) is not int or not user_id:
        return {'error': 'user_id must to be int type'}

    payload = {
        'id': user_id,
        'exp': datetime.datetime.utcnow()
        + datetime.timedelta(minutes=Configuration.TIME_EXP_TOKEN),
    }
    token = jwt.encode(payload, Configuration.SECRET_KEY)
    return {'token': token}


def token_authentication(function):
    """
    Esta função faz a proteção de uma rota através da validação do TOKEN JWT de acesso.

    :param function: função da rota de acesso que deseja proteger
    :return: Function() ou Diconário com erro encontrado na validação
    """

    @wraps(function)
    def wrapper(*args, **kwargs):

        if 'Authorization' not in request.headers:
            return make_response({'error': 'unauthorized'}, 401)

        token_from_headers = request.headers['Authorization']

        try:
            token_no_bearer = token_from_headers[7:]
            decode = jwt.decode(
                token_no_bearer, Configuration.SECRET_KEY, algorithms=['HS256']
            )
        except:
            return make_response({'error': 'unauthorized'}, 401)
        return function()

    return wrapper


def user_id_from_token() -> dict:
    """
    Esta função retorna o ID do usuário que esta solicitando alguma requisição através do seu TOKEN JWT

    :return: em caso de sucesso {'user_id': user_id} ou em caso de NÃO SUCESSO {'error': 'unauthorized'}
    """

    if 'Authorization' not in request.headers:
        return {'error': 'unauthorized'}

    token_from_headers = request.headers['Authorization']

    try:
        token_no_bearer = token_from_headers[7:]
        decode = jwt.decode(
            token_no_bearer, Configuration.SECRET_KEY, algorithms=['HS256']
        )
        user_id = decode['id']
        return {'user_id': user_id}
    except:
        return {'error': 'unauthorized'}


def mail_token_generate() -> int:
    """
    Esta função gera uma sequência aleatória de 6 números que pode variar entre 100000 e 999999. Não é necessário
    passar nenhum parâmentro

    :return: número
    """
    token = randrange(100000, 999999, 2)
    return token
