# Native Imports
from flask import make_response
from werkzeug.security import check_password_hash, generate_password_hash

# Created Imports
from configuration.configuration import Configuration
from database.database import create_session
from error.error import get_error_msg
from modules.users.controllers.user_audit_controller import (
    user_token_modification_count,
)
from modules.users.json_schema.user_authentication_json import (
    json_validate_user_authentication,
)
from modules.users.json_schema.user_create_json import (
    json_validate_create_user,
)
from modules.users.json_schema.user_update_json import (
    json_validate_update_user,
)
from modules.users.json_schema.user_update_password import (
    json_validate_user_password_update,
)
from modules.users.models.user_model import User
from modules.users.serializers.user_seriallizer import UserBasicSchema
from resources.py.password.password_manager import (
    generate_password,
    validate_password,
)
from resources.py.token import token_manager
from resources.py.email.email_manager import (
    validate_email,
    send_email_password_new_user,
    send_email_token_reset_password,
)
from resources.py.token.token_manager import (
    user_id_from_token,
    mail_token_generate,
)

session = create_session()

UserBasicSchema = UserBasicSchema(many=True)


def get_user_by_id(user_id: int) -> User:
    """
    Esta função retorna um usuário do banco sql através do seu ID

    :param user_id: ID do usuário
    :return: objeto usuário contendo as informações do usuário consultado
    """

    user = session.query(User).filter_by(user_id=user_id).first()
    session.close()
    return user


def get_user_by_username(username: str) -> User:
    """
    Esta função retorna um usuário do banco sql através do seu nome

    :param username: nome do usuário
    :return: objeto usuário contendo as informações do usuário consultado
    """

    user = session.query(User).filter_by(user_name=username).first()
    session.close()
    return user


def get_user_by_email(email: str) -> User:
    """
    Esta função retorna um usuário do banco sql através do seu email

    :param email: Email do usuário
    :return: objeto usuário contendo as informações do usuário consultado
    """

    user = session.query(User).filter_by(user_email=email).first()
    session.close()
    return user


def check_login_password(user_dict: dict) -> make_response:
    """
    Função para autenticar o usuário e caso ele seja aceito será retornado um diconário contendo um token JWT que
    deverá ser usado para atenticar as transações da aplicação.

    :param user_dict: { "user_name": "type": "string", "user_email": "type": "string" }
    :return: em caso de sucesso será retornado { 'TOKEN': foo } e em caso de NÃO sucesso será retornado
     { 'error': foo }
    """
    try:

        if not json_validate_user_authentication(user_dict):
            return make_response({'error': 'invalid json'}, 415)

        username = user_dict['user_name'].upper()
        password = user_dict['user_password']

        user = get_user_by_username(username)

        if user is None:
            return make_response({'error': 'access denied'}, 401)

        if user.user_status == 0:
            return make_response({'error': 'access denied'}, 401)

        if not check_password_hash(user.user_password, password):
            return make_response({'error': 'access denied'}, 401)

        user_id = token_manager.token_generator(user.user_id)

        if 'error' in user_id:
            return make_response(user_id['error'], 401)

        return make_response(user_id, 200)

    except:
        return get_error_msg()


def get_all_users() -> make_response:
    """
    Esta função retorna todos os usuários do banco sql com exceção do usuário administrador

    :return: { 'user': [ { user }, ] }
    """

    user = (
        session.query(User)
        .filter(User.user_id != Configuration.ADMIN_USER_ID)
        .all()
    )
    session.close()

    return make_response({'users': UserBasicSchema.dump(user)}, 200)


def check_username_email(user_name: str = None, email: str = None) -> dict:
    """
    Esta função realiza a validação do username e email, verificando no banco de dados se já estão previamente
    cadastrados, bem como, realiza a validação do email através de uma REGEX. Caso deseje validdar apenas um dos
    dois, você deverá informar apenas a opção desejada (user_name ou email)

    :param user_name: nome do usuário
    :param email: email do usuário
    :return: em caso de sucesso será retornado { 'success': 'ok' } e em caso de não sucesso será retornado
     { 'error': foo }
    """

    if user_name == '' or email == '':
        return {'error': 'invalid username or email'}

    if email:
        user_by_email = get_user_by_email(email)
        if user_by_email or not validate_email(email):
            return {'error': 'invalid email'}

    if user_name:
        user_by_username = get_user_by_username(user_name)
        if user_by_username:
            return {'error': 'invalid username'}

    return {'success': 'ok'}


def create_new_user(user_dict: dict) -> make_response:
    """
    Esta função insere no banco SQL um usuário. Antes de inserir é verificado a existência do email ou username
    no banco para evitar duplicidade nos cadastros. Será gerada uma senha com 8 carácteres para este usuário e
    enviada automaticamente para o email informado

    :param user_dict: { "user_name": "type": "string", "user_email": "type": "string" }
    :return: em caso de sucesso será retornado { 'user': {user} } ou em caso de não sucesso { 'error': foo }
    """

    if not json_validate_create_user(user_dict):
        return make_response({'error': 'invalid json'}, 415)

    validate_username_and_email = check_username_email(
        user_name=user_dict['user_name'], email=user_dict['user_email']
    )

    if 'error' in validate_username_and_email.keys():
        return make_response(validate_username_and_email, 400)

    user_password = generate_password()
    user_from_token = user_id_from_token()

    if 'user_id' not in user_from_token:
        return make_response(user_from_token, 400)

    user = User(
        user_name=user_dict['user_name'].upper(),
        user_password=generate_password_hash(user_password, method='sha256'),
        user_email=user_dict['user_email'].upper(),
        user_status=1,
        user_last_modification_user_id=user_from_token['user_id'],
    )

    session.add(user)
    session.commit()
    session.close()

    validate_send_email = send_email_password_new_user(
        email=user_dict['user_email'], password=user_password
    )

    if 'error' in validate_send_email.keys():
        return make_response(validate_send_email, 400)

    return make_response({'user': UserBasicSchema.dump([user])}, 201)


def update_user(user_dict: dict) -> make_response:
    """
    Esta função atualiza um registro de usuário no banco de dados através do seu ID que deverá ser informado dentro
    do dicionário com os outros dados que se deseja atualizar. Todos os campos do dicionário de entrada são
    obrogatórios, porém caso não deseje atualizar algum dos campos, este campos deve ser nulo. ATENÇÃO
    Esta função não permite atualizar password ou token

    :param user_dict: { "user_id": "type": "integer", "user_name": "type": ["string" ou "null"],
     "user_email": "type": ["string" ou "null"], "user_status": "type": "integer" }
    :return: em caso de sucesso será retornado { 'user': {user} } ou em caso de NÃO sucesso { 'error': foo }
    """

    if not json_validate_update_user(user_dict):
        return make_response({'error': 'invalid json'}, 415)

    if not user_dict['user_id']:
        return make_response({'error': 'invalid user id'}, 400)

    user = get_user_by_id(user_dict['user_id'])

    if not user:
        return make_response({'error': 'non-existing user'}, 400)

    user_from_token = user_id_from_token()

    if 'user_id' not in user_from_token:
        return make_response(user_from_token, 400)

    if (
        user_dict['user_id'] == user_from_token['user_id']
        and user_dict['user_status'] == 0
    ):
        return make_response({'error': 'you cannot disable your access'}, 400)

    if user.user_name != user_dict['user_name'] and user_dict['user_name']:
        validate_username = check_username_email(
            user_name=user_dict['user_name']
        )
        if 'error' in validate_username.keys():
            return make_response(validate_username, 400)
        user.user_name = user_dict['user_name'].upper()

    if user.user_email != user_dict['user_email'] and user_dict['user_email']:
        validate_user_email = check_username_email(
            email=user_dict['user_email']
        )
        if 'error' in validate_user_email.keys():
            return make_response(validate_user_email, 400)
        user.user_email = user_dict['user_email']

    if user_dict['user_status'] in [0, 1]:
        user.user_status = user_dict['user_status']
    else:
        return make_response({'error': 'invalid status'}, 400)

    user.user_last_modification_user_id = user_from_token['user_id']

    session.add(user)
    session.commit()
    session.close()

    return make_response({'user': UserBasicSchema.dump([user])}, 200)


def send_reset_password_token_to_user(user_request: dict) -> make_response:
    """
    Através do user_name, esta função envia um código de 6 digitos para o email vinculado ao usuário pertecente
    ao user_name. Este código com 6 digitos tabmbém é gravado no banco sql. Para evitar spam ou tentativas
    suspeitas, a função verifica se nos últimos 5 min foram gerados mais de 3 códigos, caso sim, será barrado.

    :param user_request: {'user_name': foo}
    :return: em caso de sucesso {'user_id': foo}, em caso de não sucesso {'error': boo}
    """
    try:

        if 'user_name' not in user_request:
            return make_response({'error': 'invalid json'}, 415)

        if not user_request['user_name'] or user_request['user_name'] == '':
            return make_response({'error': 'invalid json'}, 415)

        user = get_user_by_username(user_request['user_name'].upper())

        if not user:
            return make_response({'error': 'invalid user'}, 400)

        if user_token_modification_count(user.user_id) > 3:
            return make_response(
                {
                    'error': 'you have made more than 3 attempts in the last 5 minutes. Please wait and try agian'
                },
                400,
            )

        token = mail_token_generate()

        user.user_token = token

        session.add(user)
        session.commit()
        session.close()

        send_email_result = send_email_token_reset_password(
            user.user_email, str(token)
        )

        if 'success' not in send_email_result:
            return make_response(send_email_result, 400)

        return make_response({'user_id': user.user_id}, 200)

    except:
        get_error_msg()


def user_update_password_by_token_and_id(user_dict: dict) -> make_response:
    """
    Esta função atualiza o user_password no banco sql. Atrvés do dicionário de entrada, a função busca
    o usuário com id informado e compara se o token informado é igual ao token que esta registrado
    no banco sql. Caso o token informado esteja incorreto, esta função atualiza o campo user_token no banco sql
    para nulo. Todos os campos do dicionário são obrogatórios.

    :param user_dict: {"user_id": "type": "integer" ,"user_password": "type": "string",
     "user_token": "type": "integer"  }
    :return: em caso de sucesso {'user_id': foo}, em caso de não sucesso {'error': boo}
    """
    try:
        if not json_validate_user_password_update(user_dict):
            return make_response({'error': 'invalid json'}, 415)

        if not validate_password(user_dict['user_password']):
            return make_response({'error': 'invalid password'}, 400)

        user = get_user_by_id(user_dict['user_id'])

        if not user:
            return make_response({'error': 'non-existing user'}, 400)

        if not user.user_token:
            return make_response({'error': 'invalid token'}, 400)

        if user_dict['user_token'] != int(user.user_token):
            user_delete_token(user_dict['user_id'])
            return make_response({'error': 'invalid token'}, 400)

        user.user_last_modification_user_id = Configuration.ADMIN_USER_ID
        user.user_password = generate_password_hash(
            user_dict['user_password'], method='sha256'
        )

        session.add(user)
        session.commit()
        session.close()

        user_delete_token(user_dict['user_id'])

        return make_response({'user_id': user.user_id}, 200)

    except:
        get_error_msg()


def user_delete_token(user_id: int) -> bool:
    """
    Esta função atualiza do o user_token no banco sql para NULO. Esta funcionalidade tem como alvo
    o user com id informado na chamda desta função.

    :param user_id: id do usuário
    :return: [True, False]
    """
    try:
        user = get_user_by_id(user_id)
        user.user_token = None
        session.add(user)
        session.commit()
        session.close()
        return True
    except:
        return False
