from app import db


def test_register_get(client):
    """Kayıt sayfasının GET isteği 200 döner."""
    resp = client.get('/auth/register')
    assert resp.status_code == 200


def test_register_post_success(client, db_session):
    """Geçerli veri ile kayıt başarılı olur."""
    data = {
        'username': 'newuser',
        'email': 'new@example.com',
        'password': 'securepass',
        'password_confirm': 'securepass'
    }
    resp = client.post('/auth/register', data=data, follow_redirects=True)
    # Başarıyla kayıt oldunuz
    assert b'Ba\xc5\x9far\xc4\xb1yla kay\xc4\xb1t oldunuz' in resp.data
    # Kullanıcı DB'de olmalı
    from app.models import User
    user = db_session.scalar(db.select(User).filter_by(username='newuser'))
    assert user is not None


def test_register_post_invalid(client, db_session):
    """Eksik/yanlış veri -> form hatası."""
    data = {'username': '', 'email': 'bad', 'password': '1', 'password_confirm': '2'}
    resp = client.post('/auth/register', data=data)
    # Form hataları template içinde render edilir
    assert resp.status_code == 200


def test_login_get(client):
    resp = client.get('/auth/login')
    assert resp.status_code == 200


def test_login_post_success(client, test_user):
    data = {'username': 'testuser', 'password': 'testpassword'}
    resp = client.post('/auth/login', data=data, follow_redirects=True)
    # Simülasyon kelimesi sayfada olmalı
    assert b'Sim\xc3\xbclasyon' in resp.data
    # Oturumun set olduğunu kontrol et
    with client.session_transaction() as sess:
        assert sess['_user_id'] == str(test_user.id)


def test_login_post_failure(client, db_session):
    data = {'username': 'nonexistent', 'password': 'wrong'}
    resp = client.post('/auth/login', data=data, follow_redirects=True)
    # Geçersiz kullanıcı adı veya şifre
    assert b'Ge\xc3\xa7ersiz kullan\xc4\xb1c\xc4\xb1 ad\xc4\xb1 veya \xc5\x9fifre' in resp.data


def test_logout(client, test_user):
    # Önce giriş yap
    client.post('/auth/login', data={'username': 'testuser', 'password': 'testpassword'})
    client.get('/auth/logout', follow_redirects=True)
    with client.session_transaction() as sess:
        assert '_user_id' not in sess


def test_protected_route_requires_login(client):
    resp = client.get('/simulation/', follow_redirects=False)
    # login_required redirect (302) -> /auth/login?next=...
    assert resp.status_code == 302
    assert '/auth/login' in resp.headers.get('Location', '')


def test_protected_route_access_after_login(client, test_user):
    client.post('/auth/login', data={'username': 'testuser', 'password': 'testpassword'})
    resp = client.get('/simulation/')
    assert resp.status_code == 200
