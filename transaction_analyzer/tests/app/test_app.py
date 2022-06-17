from configuration.configuration import TestConfig


def test_app_is_created(app):
    assert app.name == 'app'


def test_debug_is_equal_configuration(app):
    assert app.config['DEBUG'] == TestConfig.DEBUG


def test_host_is_equal_configuration(app):
    assert app.config['HOST'] == TestConfig.HOST


def test_port_is_equal_configuration(app):
    assert app.config['PORT'] == TestConfig.PORT


def test_template_reload_is_true(app):
    assert (
        app.config['TEMPLATES_AUTO_RELOAD'] == TestConfig.TEMPLATES_AUTO_RELOAD
    )


def test_secret_key_is_equal_configuration(app):
    assert app.config['SECRET_KEY'] == TestConfig.SECRET_KEY


def test_root_dir_is_equal_configuration(app):
    assert app.config['ROOT_DIR'] == TestConfig.ROOT_DIR


def test_admin_user_id_is_equal_configuration(app):
    assert app.config['ADMIN_USER_ID'] == TestConfig.ADMIN_USER_ID


def test_admin_user_name_is_equal_configuration(app):
    assert app.config['ADMIN_USER_NAME'] == TestConfig.ADMIN_USER_NAME


def test_admin_user_password_is_equal_configuration(app):
    assert app.config['ADMIN_PASSWORD'] == TestConfig.ADMIN_PASSWORD


def test_admin_user_email_is_equal_configuration(app):
    assert app.config['ADMIN_EMAIL'] == TestConfig.ADMIN_EMAIL


def test_admin_user_status_is_equal_configuration(app):
    assert app.config['ADMIN_STATUS'] == TestConfig.ADMIN_STATUS


def test_admin_user_is_equal_configuration(app):
    assert app.config['ADMIN_USER_ID'] == TestConfig.ADMIN_USER_ID


def test_token_name_is_equal_configuration(app):
    assert app.config['TOKEN_NAME'] == TestConfig.TOKEN_NAME


def test_time_expire_token_is_equal_configuration(app):
    assert app.config['TIME_EXP_TOKEN'] == TestConfig.TIME_EXP_TOKEN


def test_limit_time_expire_token_is_equal_configuration(app):
    assert app.config['LIMIT_EXP_TOKEN'] == TestConfig.LIMIT_EXP_TOKEN


def test_mail_server_is_equal_configuration(app):
    assert app.config['MAIL_SERVER'] == TestConfig.MAIL_SERVER


def test_mail_port_is_equal_configuration(app):
    assert app.config['MAIL_PORT'] == TestConfig.MAIL_PORT


def test_mail_user_tls_is_equal_configuration(app):
    assert app.config['MAIL_USE_TLS'] == TestConfig.MAIL_USE_TLS


def test_mail_user_ssl_is_equal_configuration(app):
    assert app.config['MAIL_USE_SSL'] == TestConfig.MAIL_USE_SSL


def test_mail_user_name_is_equal_configuration(app):
    assert app.config['MAIL_USERNAME'] == TestConfig.MAIL_USERNAME


def test_mail_password_is_equal_configuration(app):
    assert app.config['MAIL_PASSWORD'] == TestConfig.MAIL_PASSWORD
