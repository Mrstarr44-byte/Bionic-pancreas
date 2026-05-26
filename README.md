# 🩸 Diyabetik Hücre Simülasyonu
## AI Agent Project Specification & Progress Tracker

---

# 1. Proje Tanımı

Bu proje, diyabetik hücrelerin:
- yüksek glukoz,
- insülin uygulaması,
- yemek tüketimi,
- egzersiz,
- stres

gibi olaylara verdiği tepkileri simüle eden Flask tabanlı bir web uygulamasıdır.

Sistem:
- Manuel Mod
- Yarı Otonom Mod
- Tam Otonom Mod

olmak üzere 3 farklı çalışma modu destekler.

Kullanıcı:
- yemek tüketebilir,
- insülin uygulayabilir,
- simülasyon başlatabilir,
- geçmiş kayıtları görebilir,
- Telegram bildirimleri alabilir,
- glukoz grafiklerini inceleyebilir.

⚠️ ÖNEMLİ:
Bu proje eğitim amaçlıdır.
Gerçek tıbbi kullanım için tasarlanmamıştır.
Tüm hesaplamalar basitleştirilmiş simülasyon modelleridir.

---

# 2. Zorunlu Teknik Mimari

## Backend
- Flask
- Application Factory Pattern
- Blueprint mimarisi

## ORM
- SQLAlchemy 2.x
- `Mapped`
- `mapped_column`

## Veritabanı
Minimum modeller:
- User
- SimulationLog
- MealPreset

⚠️ KURAL: MealPreset global ve ortak bir yemek kütüphanesidir. User modeli ile hiçbir ilişkisi (Foreign Key veya relationship) YOKTUR.

## Migration
- Flask-Migrate

## Form Sistemi
- Flask-WTF
- CSRF koruması zorunlu

## Authentication
- Flask-Login
- bcrypt ile hashlenmiş şifreler

## Frontend
- Jinja2 template engine
- `base.html` inheritance sistemi
- Minimum 4 farklı sayfa

## UI
- Bootstrap veya Tailwind
- Responsive tasarım
- Mobil uyumluluk

## Grafikler
- Chart.js

## Hücre Animasyonları
Duruma göre emoji kullanılmalı:
- 😊 NORMAL
- 😓 HYPERGLYCEMIA
- 🥶 HYPOGLYCEMIA

## Hata Yönetimi
- Özel 404 sayfası
- Özel 500 sayfası

## Çoklu Dil Sistemi
- Türkçe
- İngilizce
- JSON tabanlı çeviri sistemi

## Yasal Uyarılar
- Açılış disclaimer modalı
- Kalıcı footer uyarısı
- About sayfası

## API
Endpoint:
```http
GET /api/v1/simulations
```

JSON response dönmelidir.

## Deployment
Desteklenmeli:
- Docker
- docker-compose
- Render
- Railway
- Fly.io

---

# 3. Simülasyon Sistemi

## Genel Mantık

Sistem gerçek zamanlı sürekli çalışan bir simülasyon değildir.

Olay güdümlü çalışır:
1. Kullanıcı işlem yapar
2. Simülasyon motoru hesaplama yapar
3. Sonuç üretilir
4. Grafik güncellenir

---

## config.py Parametreleri

```python
CARB_FACTOR = 4.0
INSULIN_FACTOR = 40.0
EXERCISE_FACTOR = 20.0

GLUCOSE_INITIAL = 100
GLUCOSE_LOW = 70
GLUCOSE_HIGH = 180
```

---

## Hücre Durumları

| Durum | Koşul |
|---|---|
| NORMAL | 70-180 |
| HYPOGLYCEMIA | <70 |
| HYPERGLYCEMIA | >180 |

---

## Modlar

### Manuel Mod
Kullanıcı insülini kendi uygular.

### Yarı Otonom Mod
Sistem öneriler verir.
Telegram uyarıları gönderilir.

### Tam Otonom Mod
AI otomatik insülin ayarı yapar.
Telegram özet raporları gönderilir.

---

# 4. Telegram Bot Sistemi

## Kullanılacak Yapı
- Polling yöntemi kullanılacaktır.
- Webhook kullanılmayacaktır.

## Kullanılacak Kütüphane
```python
python-telegram-bot
```

## Environment Variables

```env
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=
```

## Bildirim Türleri
- Hipoglisemi uyarısı
- Hiperglisemi uyarısı
- Stabilite mesajı
- Günlük özet raporu
- Motivasyon mesajı

---

# 5. Environment Variables

Proje `.env` sistemi ile çalışmalıdır.

## Zorunlu değişkenler

```env
SECRET_KEY=
DATABASE_URL=
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=
FLASK_ENV=
```

## Kurallar
- Hardcoded secret key yasaktır.
- `.env.example` dosyası oluşturulmalıdır.

---

# 6. Docker Standardı

## Base Image

```dockerfile
python:3.12-slim
```

## Docker Gereksinimleri
- requirements.txt install edilmeli
- environment variables desteklenmeli
- Flask production modda çalışmalı
- Port 5000 expose edilmeli

---

# 7. Test ve Kod Kalitesi

## Zorunlu Araçlar
- pytest
- flake8

## Minimum Testler
- auth route testleri
- simulation engine testleri
- API endpoint testleri

## Kod Standartları
- PEP8 uyumu
- flake8 hatasız çalışma

## Opsiyonel
- black
- isort

---

# 8. Simülasyon Kısıtları

Simülasyon:
- gerçek biyolojik doğruluk hedeflemez
- eğitim amaçlıdır
- basitleştirilmiş matematik kullanır
- gerçek medikal karar sistemi değildir

⚠️ Kompleks farmakokinetik model kullanılmayacaktır.

---

# 9. Proje Klasör Yapısı

```text
project/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── forms.py
│   ├── config.py
│   │
│   ├── main/
│   │   ├── routes.py
│   │   └── __init__.py
│   │
│   ├── auth/
│   │   ├── routes.py
│   │   └── __init__.py
│   │
│   ├── simulation/
│   │   ├── engine.py
│   │   ├── routes.py
│   │   └── __init__.py
│   │
│   ├── meals/
│   │   ├── routes.py
│   │   └── __init__.py
│   │
│   ├── api/
│   │   ├── routes.py
│   │   └── __init__.py
│   │
│   ├── telegram_bot/
│   │   ├── bot.py
│   │   └── notifier.py
│   │
│   ├── errors/
│   │   ├── handlers.py
│   │   └── __init__.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── simulation.html
│   │   ├── meals.html
│   │   ├── about.html
│   │   ├── 404.html
│   │   └── 500.html
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── uploads/
│   │
│   └── translations/
│       ├── tr.json
│       └── en.json
│
├── migrations/
├── tests/
├── .env.example
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── run.py
└── README.md
```

---

# 10. requirements.txt Minimum İçeriği

```txt
Flask
Flask-SQLAlchemy
SQLAlchemy
Flask-Migrate
Flask-WTF
Flask-Login
bcrypt
python-dotenv
python-telegram-bot
pytest
flake8
```

---

# 11. Kodlama Kuralları

## Zorunlu Kurallar

- Kod modüler yazılmalı
- Her blueprint ayrı klasörde olmalı
- Tüm route dosyaları blueprint kullanmalı
- SQLAlchemy 2.x syntax kullanılmalı
- Config sınıfları kullanılmalı
- Hardcoded secret key kullanılmamalı
- Environment variable desteği olmalı
- Tüm formlar Flask-WTF kullanmalı
- Tüm POST işlemleri CSRF korumalı olmalı

---

## Kod Stili

- PEP8
- Anlaşılır değişken isimleri
- Küçük fonksiyonlar
- Gereksiz yorum satırlarından kaçınılmalı

---

# 12. AI Agent Yasakları

AI agent:
- proje mimarisini değiştiremez
- görev sırasını değiştiremez
- dependency atlayamaz
- FastAPI kullanamaz
- React frontend'e geçemez
- ORM değiştiremez
- async mimariye geçemez
- placeholder kod bırakamaz

---

# 13. Bir Görevin Tamamlanmış Sayılması İçin

Bir görev ancak şu koşullarda tamamlandı kabul edilir:

- Kod çalışıyorsa
- Import hatası yoksa
- Dosya doğru klasördeyse
- README güncellendiyse
- Mimariye uyuyorsa
- Flask uygulaması crash olmuyorsa
- Görev çıktısı kullanıcıya gösterildiyse

---

# 14. Görev Tamamlama Kuralları

AI agent aşağıdaki kurallara HARFİYEN uymalıdır:

1. Her mesajda yalnızca 1 görev tamamlanacak.
2. Görev sırası değiştirilmeyecek.
3. Dependency kuralları ihlal edilmeyecek.
4. Her görev sonrası:
   - ilgili kod gösterilecek
   - README güncellenecek
5. Eksik import bırakılmayacak.
6. Kod çalışabilir durumda olacak.
7. Mimari bütünlük korunacak.

---

# 15. Görev Listesi

| ID | Görev | Bağımlılık | Durum |
|---|---|---|---|
| 1.1 | Klasör yapısını oluştur | - | ✅ Tamamlandı |
| 1.2 | requirements.txt oluştur | 1.1 | ✅ Tamamlandı |
| 1.3 | config.py oluştur | 1.1 | ✅ Tamamlandı |
| 1.4 | app/__init__.py factory sistemi | 1.1, 1.3 | ✅ Tamamlandı |
| 2.1 | models.py oluştur | 1.4 | ✅ Tamamlandı |
| 2.2 | Flask-Migrate yapılandır | 2.1 | ✅ Tamamlandı |
| 2.3 | Seed sistemi ve başlangıç verileri | 2.1 | ✅ Tamamlandı |
| 3.1 | forms.py auth formları | 2.1 | ✅ Tamamlandı |
| 3.2 | auth blueprint routes | 3.1 | ✅ Tamamlandı |
| 3.3 | LoginManager yapılandır | 3.2 | ✅ Tamamlandı |
| 4.1 | main blueprint routes | 1.4 | ✅ Tamamlandı |
| 4.2 | base.html oluştur | 4.1 | ✅ Tamamlandı |
| 4.3 | disclaimer modal ekle | 4.2 | ✅ Tamamlandı |
| 5.1 | Çoklu dil sistemi (tr.json, en.json ve helper) | 1.1 | ✅ Tamamlandı |
| 6.1 | simulation engine yaz | 2.1 | ✅ Tamamlandı |
| 6.2 | simulation routes yaz | 6.1 | ✅ Tamamlandı |
| 6.3 | simulation forms oluştur | 3.1 | ⏳ Bekliyor |
| 7.1 | meals routes + pagination | 2.1 | ⏳ Bekliyor |
| 7.2 | meals.html oluştur | 7.1 | ⏳ Bekliyor |
| 8.1 | API endpoint oluştur | 2.1 | ⏳ Bekliyor |
| 9.1 | Telegram bot sistemi | 1.3 | ⏳ Bekliyor |
| 9.2 | notifier sistemi | 9.1 | ⏳ Bekliyor |
| 10.1 | error handlers yaz | 1.4 | ⏳ Bekliyor |
| 10.2 | 404 ve 500 sayfaları | 10.1 | ⏳ Bekliyor |
| 11.1 | Chart.js entegrasyonu | 6.2 | ⏳ Bekliyor |
| 11.2 | Hücre animasyonları | 11.1 | ⏳ Bekliyor |
| 12.1 | pytest testleri | 3.2, 6.1, 8.1 | ⏳ Bekliyor |
| 12.2 | flake8 yapılandırması | 1.2 | ⏳ Bekliyor |
| 13.1 | Dockerfile yaz | 1.2 | ⏳ Bekliyor |
| 13.2 | docker-compose yaz | 13.1 | ⏳ Bekliyor |
| 13.3 | .env.example oluştur | 1.3 | ⏳ Bekliyor |
| 13.4 | run.py oluştur | 1.4 | ⏳ Bekliyor |

---

# 16. AI Agent Çalışma Formatı

Her görev aşağıdaki formatta tamamlanmalıdır:

## Tamamlanan Görev
Görev ID + açıklama

## Oluşturulan Dosyalar
Liste halinde

## Kod
Tam kod çıktısı

## README Güncellemesi
Güncellenmiş görev satırı

## Sonraki Görev
Bir sonraki görev adı

---

# 17. Gelecekte Eklenebilecek Özellikler

- AI glukoz tahmini
- Time-series analiz
- Redis + Celery
- WebSocket gerçek zamanlı grafik
- Doktor paneli
- Gamification sistemi
- PDF rapor üretimi
- Dexcom API mock
- Google Fit entegrasyonu
- Digital twin yaklaşımı
- Event sourcing sistemi

---

# 18. Başlangıç Talimatı

AI agent aşağıdaki görevden başlamalıdır:
⚠️ Her mesajda yalnızca 1 görev tamamlanmalıdır.
⚠️ Dependency kuralları ihlal edilmemelidir.
⚠️ Mimari değiştirilemez.
