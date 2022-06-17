# Native Imports
from flask_mail import Mail, Message
import re

# Created Imports
from configuration.configuration import Configuration
from error.error import get_error_msg

mail = Mail()


def send_email_password_new_user(email: str, password: str) -> dict:
    """
    Esta função envia um email contendo a senha passada informada.

    :param password: senha do usuário recém cadastrado
    :param email: email do usuário destino
    :return: {'success': 'mail sent'} para sucesso ao enviar ou {'error': 'send mail failed to send'} em caso de error
    """

    try:

        if not validate_email(email) or type(email) is not str:
            return {'error': 'invalid email'}

        if password == '' or password is None or type(password) is not str:
            return {'error': 'invalid password'}

        body = f"""
        
        Esta é sua senha temporária. Você pode troca-la para aumentar sua segurança:
    
       {password}
    
        """

        msg = Message(
            subject='Senha de acesso.',
            sender=Configuration.MAIL_USERNAME,
            recipients=email.split(),
            body=body,
        )

        mail.send(msg)

        return {'success': 'mail sent'}

    except:
        return get_error_msg()


def validate_email(email: str) -> bool:
    """
    Esta função realiza a validação de uma string no formato de email. Caso considerado válido será retornado
    o valor True.

    :param email: email
    :return: True ou False
    """

    if not email or type(email) is not str:
        return False

    regex = re.compile(
        r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])"
    )
    result = re.fullmatch(regex, email)
    if result:
        return True
    else:
        return False


def send_email_token_reset_password(email: str, token: str) -> dict:
    """
    Esta função envia um email contendo a senha passada informada.

    :param token: token para resetar senha
    :param email: email do usuário destino
    :return: {'success': 'mail sent'} para sucesso ao enviar ou {'error': 'send mail failed to send'} em caso de error
    """

    try:

        if not validate_email(email) or type(email) is not str:
            return {'error': 'invalid email'}

        if token == '' or token is None or type(token) is not str:
            return {'error': 'invalid password'}

        body = f"""

        Este é seu TOKEN:

       {token}

        """

        msg = Message(
            subject='Token para resetar password.',
            sender=Configuration.MAIL_USERNAME,
            recipients=email.split(),
            body=body,
        )

        mail.send(msg)

        return {'success': 'mail sent'}

    except:
        return get_error_msg()
