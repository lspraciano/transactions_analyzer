# Imports Native
import random
import re


# Created Imports


def generate_password(length: int = 8) -> str:
    """
    Esta função gera uma senha com número X de caracteres. Caso não informado durante a chamada da função
    o número inicial será de 8. Se o parametro length for passado no formato incorreto, a função irá considerar
    length=8

    :param length: número de caracteres que se deseja a senha
    :return: senha
    """
    if type(length) is not int or length is None:
        length = 8

    char_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
    password = ''

    for i in range(length):
        random_char = random.choice(char_seq)
        password += random_char

    list_pass = list(password)
    random.shuffle(list_pass)
    final_password = ''.join(list_pass)
    return final_password


def validate_password(password: str) -> bool:
    """
    Função para validar o password de acordo com uma regex

    :param password: password
    :return: [True, False]
    """
    if not password or type(password) is not str:
        return False

    regex = re.compile(
        r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}$'
    )
    result = re.fullmatch(regex, password)
    if result:
        return True
    else:
        return False
