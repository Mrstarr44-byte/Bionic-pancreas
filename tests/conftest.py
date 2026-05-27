import pytest
from app import create_app, db
from app.models import User
from app.config import Config


class TestConfig(Config):
    """Test ortamı için konfigürasyon."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'test-secret-key'


@pytest.fixture(scope='session')
def app():
    """Uygulamayı test config'iyle oluştur."""
    app = create_app(TestConfig)
    yield app


@pytest.fixture(scope='function')
def client(app):
    """Flask test client."""
    return app.test_client()


@pytest.fixture(scope='function')
def db_session(app):
    """Her test için yeni veritabanı oturumu."""
    with app.app_context():
        db.create_all()
        yield db.session
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope='function')
def test_user(db_session):
    """Kayıtlı bir test kullanıcısı oluştur."""
    user = User(username='testuser', email='test@example.com')
    user.set_password('testpassword')
    db_session.add(user)
    db_session.commit()
    return user
