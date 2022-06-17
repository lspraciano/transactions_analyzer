# Native Imports
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.future.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import create_database, database_exists

# Created Imports
from werkzeug.security import generate_password_hash
from configuration.configuration import (
    app_configuration,
    app_active,
    Configuration,
)

__engine = None
ModelBase = declarative_base()


def create_engine() -> Engine:
    """
    Função para configurar a conexão ao banco de dados.

    :return: engine
    """
    global __engine

    configuration = app_configuration[app_active]
    conn_str = configuration.SQLALCHEMY_DATABASE_URI
    __engine = sa.create_engine(url=conn_str, echo=False)

    return __engine


def create_session() -> Session:
    """
    Função para criar sessão de conexão ao banco de dados.

    :return: Session()
    """
    global __engine

    if not __engine:
        create_engine()

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)

    session = __session()

    return session


def create_db(app) -> None:
    """
    Função destinada para criação do banco de dados requisitado pela aplicação. Caso não existe database criada,
    ela será gerada para criação das tabelas. No caso de a aplicação ser rodada no modo de test, o banco de
    test será criado, caso não exista, e as tabelas do banco de test serão recriadas.

    :return: None
    """

    from modules.transaction.models import (
        transaction_model,
        transaction_logs_model,
    )
    from modules.users.models import user_model
    from modules.users.models import user_audit_model

    global __engine

    if not __engine:
        create_engine()

    if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        create_database(app.config['SQLALCHEMY_DATABASE_URI'])

    if 'test' in app.config['SQLALCHEMY_DATABASE_URI']:
        ModelBase.metadata.drop_all(__engine)

    ModelBase.metadata.create_all(__engine)
    create_admin_user(user_model)


def create_admin_user(user_model) -> None:
    """
    Esta função é destinada a criar o usuário inicial da aplicação, ou seja, o usuário administrador. Caso ele já
    exista, não será gerado um novo usuário administrador.

    :return: None
    """
    session = create_session()

    user = (
        session.query(user_model.User)
        .filter_by(user_name=Configuration.ADMIN_USER_NAME)
        .first()
    )

    if not user:
        user = user_model.User(
            user_name=Configuration.ADMIN_USER_NAME,
            user_password=generate_password_hash(
                Configuration.ADMIN_PASSWORD, method='sha256'
            ),
            user_email=Configuration.ADMIN_EMAIL,
            user_status=Configuration.ADMIN_STATUS,
            user_last_modification_user_id=Configuration.ADMIN_USER_ID,
        )

        session.add(user)
        session.commit()

    session.close()
