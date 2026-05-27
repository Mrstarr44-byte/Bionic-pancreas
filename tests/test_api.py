import json
from app.models import SimulationLog


def test_api_requires_login(client):
    resp = client.get('/api/v1/simulations')
    # login_required → redirect (302)
    assert resp.status_code == 302
    assert '/auth/login' in resp.headers.get('Location', '')


def test_api_get_empty(client, test_user):
    # Oturum aç
    client.post('/auth/login', data={'username': 'testuser', 'password': 'testpassword'})
    resp = client.get('/api/v1/simulations')
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert data['status'] == 'success'
    assert isinstance(data['data'], list)
    assert len(data['data']) == 0


def test_api_pagination(client, db_session, test_user):
    # 5 log ekle
    for i in range(5):
        log = SimulationLog(user_id=test_user.id,
                            action_type='manual_simulation',
                            value=100 + i,
                            glucose_before=90,
                            glucose_after=100 + i)
        db_session.add(log)
    db_session.commit()

    client.post('/auth/login', data={'username': 'testuser', 'password': 'testpassword'})
    resp = client.get('/api/v1/simulations?per_page=2&page=2')
    data = json.loads(resp.data)
    assert data['status'] == 'success'
    # Sayfalanmış liste 2 eleman içermeli
    assert len(data['data']) == 2


def test_api_user_isolation(client, db_session):
    # iki kullanıcı oluştur
    from app.models import User
    user_a = User(username='alice', email='a@example.com')
    user_a.set_password('pass')
    user_b = User(username='bob', email='b@example.com')
    user_b.set_password('pass')
    db_session.add_all([user_a, user_b])
    db_session.commit()

    # alice için bir log ekle
    log = SimulationLog(user_id=user_a.id,
                        action_type='manual_simulation',
                        value=120,
                        glucose_before=100,
                        glucose_after=120)
    db_session.add(log)
    db_session.commit()

    # bob olarak giriş yap ve API'i çağır
    client.post('/auth/login', data={'username': 'bob', 'password': 'pass'})
    resp = client.get('/api/v1/simulations')
    data = json.loads(resp.data)
    # bob'un verisi olmamalı (BOB'un hiç logu yok)
    assert len(data['data']) == 0
