# AI Günlüğü

## Oturum 1 - 24 Mayıs 2026 - 21:00-24:00

### Hedef
Github repo kurulumu, projenin ana hatlarının belirlenmesi, to-do list oluşturulması ve proje analizi (Biyonik Pankreas Projesi).

### Kullandığım Mod ve Model
- **Mod**: Plan
- **Model**: Gemini 3.1 Pro
- **Görünüm**: Manager / Editor

### Verdiğim Promptlar
1. Proje ana hatlarını çıkarmak ve Antigravity'nin nasıl kullanılacağını öğrenmek için genel konsept analizi istedim.

### Ajanın Önerdiği Plan
Biyonik Pankreas web uygulaması için genel bir geliştirme planı sundu, ancak frontend/simülasyon tarafı için Java tabanlı çözümler önerdi.

### Plan'da Sorguladıklarım ve Düzelttiklerim
- Konum sağlıkla alakalı olduğu için yasal sınırları ve feragatname (disclaimer) zorunluluğum olup olmadığını ajana sorgulattım.
- Çıkarılan to-do list'in "Vibe Coding" mantığına ve Flask Mega-Tutorial kapsamına uygunluğunu tartıştım.
- **Kritik Müdahale**: Ajan simülasyon için Java önerdi. Bunun Flask ve Python tabanlı bir backend projesi olduğunu, Java'nın mimariye uyumsuz olacağını belirterek ajanı reddettim ve planı Python/Web teknolojileri yönüne çevirmesini sağladım.

### Bu Oturumdan Öğrendiğim
Başlangıçta geleneksel alışkanlıklarla proje notlarımı bir Google Docs dosyasına almıştım. Ancak yönergeyi analiz edince sürecin "Vibe Coding" mantığıyla tamamen AI ajanının yönettiği bir `ai-gunlugu.md` dosyasında belgelenmesi gerektiğini öğrendim ve şeffaflık adına notlarımı buraya aktardım. Ayrıca ajanın temel proje gereksinimini unutup Java önerecek kadar halüsinasyon görebildiğini, bu yüzden planlarını körü körüne onaylamamam gerektiğini tecrübe ettim.

---

## Oturum 2 - 25 Mayıs 2026 - 19:30-24:00

### Hedef
Git/GitHub altyapısının kurulması, projenin anayasası niteliğindeki README.md (kısıtlamalar ve görev listesi) dosyasının oluşturulması, Görev 1.1 (Klasör Yapısı), 1.2 (requirements.txt), 1.3 (config.py) ve 1.4 (Application Factory) adımlarının tamamlanması.

### Kullandığım Mod ve Model
•	Mod: Plan ve Fast (Kademeli ilerleme için)
•	Model: Gemini 3.5 Flash (Başlangıç), Gemini 3.1 Pro (Mimari kuralları belirleme), Claude Opus 4.6 (Kod ve dosya üretimi)
•	Görünüm: Antigravity IDE - Agent Chat (Editor View)

### Verdiğim Promptlar
1.	Proje dizininde docs klasörü oluşturulması ve dokümantasyonun başlatılması.
2.	Hazırladığım 18 maddelik "Proje Anayasası ve AI Kısıtlamaları" metninin tam olarak README.md dosyasına yazdırılması ve .gitignore dosyasının oluşturulması.
3.	Claude Opus 4.6'ya geçiş: "README.md dosyasını oku ve Görev 1.1'i (Klasör yapısını) çift alt çizgili __init__.py kurallarına dikkat ederek oluştur."
4.	"Harika. Şimdi Görev 1.2'yi yap ve requirements.txt içine belirttiğim paketleri (Flask==3.1.0 vb.) sürüm numaralarıyla sabitleyerek ekle."

### Ajanın Önerdiği Plan ve Müdahalelerim
•	Git ve GitHub Entegrasyon Krizi: Terminal üzerinden ilk commit'leri atarken MacOS'un "akıllı tırnak" özelliği yüzünden terminalde dquote> hatası (askıda kalma durumu) yaşadım. Ajanın doğrudan müdahale edemediği bu donanım/işletim sistemi sorununu, Ctrl+C ile işlemi iptal edip, commit mesajlarında çift tırnak yerine tek tırnak (') kullanarak kendim çözdüm.
•	Kritik Müdahale (Ajanın Adım Adım İlerlemesi): Görev 1.1'i verdiğimde, ajan (Claude 4.6) terminalde sadece mkdir komutu ile boş klasörleri oluşturmak için izin istedi. İlk başta eksik yaptığını (çünkü içindeki .py ve .html dosyalarını oluşturmadığını) düşündüm. Ancak Antigravity'nin Request Review (Sandbox onayı) özelliği sayesinde ajanın planını incelediğimde, bunun bir hata olmadığını, ajanın önce iskeleti kurup sonra dosyaları içine yerleştirme stratejisi izlediğini fark ettim. İlk adıma onay verdim ve hemen ardından dosyaları yaratmasını bekleyerek süreci kontrol altında tuttum.

### Üretilen Kodda Düzelttiklerim / Belirlediklerim
•	Sürüm Çakışması Önlemi: Ajanın requirements.txt dosyasını kendi inisiyatifiyle doldurmasına izin vermedim. İleride dağıtım (deployment) aşamasında veya farklı bir ortamda uyumsuzluk çıkmaması için Flask, SQLAlchemy ve diğer bağımlılıkların versiyonlarını teker teker ben belirleyip (örn: Flask==3.1.0) ajana dikte ettim.

### Bu Oturumdan Öğrendiğim
"Terminal Command Auto Execution: Request Review" ayarının hayat kurtarıcı olduğunu bizzat tecrübe ettim. README.md dosyasını bir "sabit hafıza" olarak kullandığımda, modeli Gemini'den Claude'a geçirsem bile yeni modelin README'yi okuyarak hiçbir context (bağlam) kaybı yaşamadan aynı kurallarla yola devam edebildiğini öğrendim.

---

## Oturum 3 - 26 Mayıs 2026 - 12:30-14:10

### Hedef
Projenin veritabanı modellerinin (Görev 2.1) SQLAlchemy 2.x standartlarına (Mapped, mapped_column) uygun olarak oluşturulması ve iş mantığı (business logic) hatalarının giderilmesi.

### Kullandığım Mod ve Model
•	Mod: Plan ve Fast
•	Model: Gemini 3.1 Pro, Claude Opus 4.6 (Kod Üretimi) ve DeepSeek (Code Review / Çapraz Sorgu)
•	Görünüm: Antigravity IDE - Agent Chat / Editor View

### Verdiğim Promptlar
1.	İlk Komut: "Görev 2.1 — models.py oluştur. Kesinlikle SQLAlchemy 2.x kullan. User, SimulationLog, MealPreset modellerini tanımla ve User ile MealPreset arasında ilişki kur."
2.	Revize Komutu (Claude'a): "MealPreset ortak kütüphanedir, user_id ilişkisini tamamen sil. Ekstra alanları ekle."
3.	Manuel Müdahale (Reject Sonrası): "Teknik notunu okudum ancak mimariyi değiştirdik. İlk verdiğim 'ilişki kur' kuralını İPTAL EDİYORUZ. User_id'yi tamamen sil ve şu alanları koy..."
4.	Anayasa (README) Güncellemesi: "models.py'de yaptığımız mimari güncellemeyi README'ye işle. MealPreset'in global bir kütüphane olduğunu anayasaya ekle."

### Ajanın Önerdiği Plan ve Müdahalelerim
•	DeepSeek ile Çapraz Sorgu (Cross-Validation): Ajan ilk başta mükemmel bir SQLAlchemy 2.x kodu üretti ancak verdiğim eksik prompt yüzünden MealPreset'i User tablosuna bağladı. Kodu DeepSeek'e denetlettiğimde hayati bir uyarı aldım: "Yemek kütüphanesi kullanıcıya özel olamaz, global olmalı. Ayrıca README'deki dil, telegram_id gibi alanlar eksik."
•	Yapay Zeka İnadı (Hallucination/Stubbornness) ve Override: Hatayı düzeltmesi için Claude'a yeni komut verdim. Ancak Claude eski bağlama (context) takılı kalarak "User ile ilişki kurmamı istemiştiniz, user_id zorunlu" diyerek ukalalık yaptı ve negatif promptları görmezden geldi. Kodu "Reject" (Reddet) yaparak çöpe attım ve mimari karar değişikliğini sert ve net bir dille ifade eden manuel bir prompt ile otoriteyi sağladım.
•	Anayasa (README) Senkronizasyonu: Kodda yaptığımız bu radikal mimari değişikliği anında README.md dosyasına yansıttım. İleriki görevlerde (örneğin formlar oluşturulurken) ajanın tekrar eski kurallara bakıp hata yapmasının (hallucination) önüne geçtim.

### Üretilen Kodda Düzelttiklerim / Belirlediklerim
•	Sadece Mapped[float] yazılan yerlerin Alembic (Flask-Migrate) tarafından hata vermemesi için sonlarına = mapped_column(Float) atamalarını kendim ekleterek kodu göçmelere karşı zırhlı hale getirdim. Ayrıca glucose_after gibi bazı alanların her senaryoda dolu olamayacağını öngörerek onları Optional bıraktım.

### Bu Oturumdan Öğrendiğim
Vibe Coding kesinlikle "kodu kopyala-yapıştır" demek değildir. Ajanlar bazen ilk verilen talimatlara körü körüne saplanıp kalabiliyor. Böyle durumlarda kod üzerinde inatlaşmak yerine, "iş mantığını (business logic) değiştirdiğimizi" açıkça belirterek direksiyonu ele almanın şart olduğunu öğrendim. En büyük ders ise: Kodda mimari bir karar değiştiğinde, yapay zekanın tek hafızası olan README anayasasını güncellemek zorunludur.

•	Ek Not (Ajanın Unutkanlığı): Ajan büyük mimari değişikliklere odaklandığı için README'deki 2.1 numaralı göreve 'Tamamlandı' tikini atmayı unuttu. Kendisini uyararak anayasayı tekrar güncellettirdim. Vibe coding yaparken ajanın karmaşık işleri çözerken en basit idari adımları (checkbox işaretlemek gibi) atlayabildiğini tecrübe ettim.

•	🚨 Ek Not: Migration Öncesi Hayat Kurtaran Code Review
Veritabanını kurmadan hemen önce `app/__init__.py` dosyamı DeepSeek'e denetlettim ve uygulamanın çökmesini önleyen 3 kritik müdahale yaptım:
	1.	Kayıp Modeller: `from app import models` importu eksikti. Eğer fark etmeseydim, Flask-Migrate tablolarımızı göremeyip boş bir veritabanı kuracaktı.
	2.	Hatalı Telegram Rotası: Arka planda çalışacak bot için gereksiz yere Blueprint açılmıştı, ImportError vermemesi için sildim.
	3.	Login Yönlendirmesi: Giriş yapmayan kullanıcılar için `login_view` ayarını ekledim.
Ders: Ana ajanın kodlarını çalıştırmadan önce farklı bir yapay zekaya (Auditor) denetletmek, saatlerce sürecek hata ayıklama (debugging) çilesini önlüyor.

---

## Oturum 4 - 26 Mayıs 2026 - 14:40-16:15

### Hedef
1. Görev 2.2 (Flask-Migrate yapılandırması) adımıyla modellerin fiziksel SQLite veritabanına dönüştürülmesi.
2. Görev 2.3 (Seed Sistemi) ile başlangıç verilerinin (test kullanıcısı ve örnek yemekler) eklenmesi.
3. Görev 3.1 (forms.py - Kimlik Doğrulama Formları) adımının tamamlanması.
4. Görev 3.2 ve 3.3 ile Auth rotalarının (login/register/logout) güvenlik standartlarına uygun şekilde oluşturulup LoginManager'ın yapılandırılması.

### Kullandığım Mod ve Model
•	Mod: Plan ve Fast (Kademeli ilerleme için)
•	Model: Gemini 3.5 Flash / Claude Opus 4.6 (Kod Üretimi) / GPT-OSS 120B (Kod Üretimi) ve DeepSeek (Code Review)
•	Görünüm: Antigravity IDE - Agent Chat / Editor View

### Ajanın Önerdiği Plan ve Müdahalelerim
•	AI Halüsinasyonu ve Görev Sırası İhlali (Görev 2.2): Ajan, FLASK_APP ortam değişkenini atayabilmek için run.py dosyasına ihtiyacı olduğunu iddia ederek Görev 13.4'e atlamaya kalkıştı. Bir yazılım mimarı olarak bu isteği "Reject" ettim. Ajana projede "Application Factory" deseni kullandığımızı, Flask CLI'ın export FLASK_APP=app komutuyla create_app fonksiyonunu otomatik tanıyacağını belirttim.
•	Eksik Paket Tuzağı (Görev 3.1): Ajan WTForms içindeki Email() validator'ını doğrudan yazıp geçmeye çalıştı. Ancak bu validator'ın arka planda email-validator paketini gerektirdiğini, aksi halde runtime'da sistemin çökeceğini fark ettim. Kod üretilmeden önce ajana pip install email-validator komutunu çalıştırıp bağımlılığı requirements.txt'ye eklettim.
•	Siber Güvenlik ve Mimari Kalkanlar (Görev 3.1 & 3.2): Form içi dinamik kontrollerde circular import'u engellemek için from app import db aktarımını yerel metot scope'larına taşıttım. Ayrıca /login rotasında "Open Redirect" zafiyeti oluşabileceğini fark edip urlsplit(next_page).netloc != '' kalkanını zorunlu tuttum. Son olarak, Blueprint rotalarının uygulamayı çökertmemesi için routes importunu app/auth/__init__.py dosyasının en sonuna taşıttım.

### Üretilen Kodda Düzelttiklerim / Belirlediklerim
•	Ajanın oluşturmaya yeltendiği run.py dosyası silindi; doğrudan flask db init, migrate ve upgrade komutlarıyla bionic_pancreas.db başarıyla oluşturuldu. seed.py ile test verileri basıldı.
•	app/forms.py dosyası eksiksiz dolduruldu; requirements.txt güncellendi.
•	app/auth/routes.py dosyası güvenli yönlendirmeler ve SQLAlchemy 2.x standardı (db.select) ile kusursuz entegre edildi.

### Bu Oturumdan Öğrendiğim
•	Yapay zeka araçlarının "bu olmadan şu çalışmaz" şeklindeki kesin yargılarına (hallucination) her zaman güvenmemek gerektiğini öğrendim. Framework'ün (Flask) derin çalışma mantığını bilmek, beni proje anayasasını ihlal etmekten kurtardı.
•	Kriz Yönetimi (Git Temizliği): Projede .gitignore eksikliği yüzünden venv (sanal ortam) klasörünün Git takibine alındığını fark ettim. Binlerce kütüphane dosyasının repoyu şişirmesini önlemek için git rm -r --cached venv ile acil müdahale edip .gitignore kalkanını oluşturdum.
•	AI ajanlarının sadece "çalışan" bir kod üretmesinin yeterli olmadığını, üretilen rotaların siber güvenlik (Open Redirect) ve bağımlılık (Peer Dependencies) perspektifiyle mimar tarafından denetlenmesi gerektiğini tecrübe ettim.

### Sonraki Oturum İçin Notlar
Kısa bir molanın ardından ana web sayfalarının (main blueprint) ve frontend'in kalbi olacak Jinja2 base.html şablonunun (Görev 4 serisi) inşasına başlanacak.

---

## Oturum 5 - 26 Mayıs 2026 - 18:45-20:00

### Hedef
1. Görev 3.3'ün (LoginManager Yapılandırması) teknik olarak eksik kaldığının tespiti ve Flask-Login için zorunlu olan user_loader fonksiyonunun mimariye uygun şekilde projeye entegre edilmesi.
2. Uygulamanın ana sayfa rotalarının (Görev 4.1), Jinja2 tabanlı tasarım iskeletinin (base.html - Görev 4.2) ve yasal sorumluluk reddi uyarı penceresinin (Disclaimer Modal - Görev 4.3) projeye eklenmesi.

### Kullandığım Mod ve Model
•	Mod: Fast
•	Model: GPT-OSS 120B (Medium) ve DeepSeek (Code Review)
•	Görünüm: Antigravity IDE - Agent Chat / Editor View

### Ajanın Önerdiği Plan ve Müdahalelerim
•	Gözden Kaçan Görev ve Anayasa (README) Denetimi: Bir önceki oturumda backend'i bitirdiğimizi düşünsek de, projenin "sabit hafızası" olan README.md dosyasını kontrol ettiğimde Görev 3.3'ün (LoginManager yapılandırması) hala beklemede olduğunu fark ettim. Gerçekten de app/__init__.py içine ayarları girmiş olsak da, Flask-Login'in kalbi olan @login.user_loader fonksiyonunu yazmayı unutmuştuk.
•	Mimari Konumlandırma Koruması: Ajanın inisiyatif alıp bu fonksiyonu routes.py veya __init__.py gibi yanlış yerlere koyarak "Spagetti Kod" yaratmasını engellemek için fonksiyonun kesinlikle app/models.py dosyasının en altına yazılması gerektiğini net bir prompt ile dikte ettim.
•	Döngüsel İçe Aktarım (Circular Import) Tuzağı: Fonksiyonu models.py içine yazarken, dosyanın en üstünde login ve db importlarının projeyi kilitlediği bilinen bir Flask tuzağıdır. Ajana from app import db satırını "Geç İçe Aktarım" (Late Import) tekniğiyle doğrudan load_user fonksiyonunun içine yazmasını emrettim.
•	Görev Sırası (Mimari) İhlali: Ajan, Görev 4.1 (main blueprint routes) adımını atlayıp doğrudan Görev 4.2'deki (base.html) frontend kodlarını yazmaya kalkıştı. Henüz rotalar ortada yokken navbar'a link koyması BuildError ile uygulamayı çökertecekti. Ajanın bu adımına "Reject" (Reddet) vererek sırayı bozmamasını ve önce rotayı yazmasını sağladım.
•	Sinsi UX Hatası ve Vibe Coding ile Bug Çözümü: Ajan Görev 4.3'te yasal uyarı modalını her sayfa yenilemesinde açılacak şekilde kurguladı. UX faciasını önlemek için ajana localStorage mantığını kurdurttum. Ancak butona basılınca modalın kapanmaması bug'ı ortaya çıktı. Kodu manuel değiştirip bozma riskine girmek yerine, "acceptDisclaimerBtn'e tıklanınca myModal.hide() çağır" şeklinde spesifik bir komutla (Vibe Coding ruhuna uygun olarak) bug'ı ajana yamalattırdım.

### Üretilen Kodda Düzelttiklerim / Belirlediklerim
•	app/models.py dosyasına load_user fonksiyonu SQLAlchemy 2.x standardı olan db.session.get(User, int(id)) ile eklendi. Çökme testi için chat üzerinden "Evet" komutuyla terminalde flask run onayı verildi.
•	app/main/__init__.py dosyasına blueprint importu (circular import korumasıyla) eklendi.
•	app/templates/base.html dosyası Bootstrap 5, Flash mesajları (get_flashed_messages) ve {% block content %} Jinja2 mimarisiyle sıfırdan yaratıldı. Statik Disclaimer Modal'ı başarılı şekilde sisteme gömüldü.

### Bu Oturumdan Öğrendiğim
•	Proje geliştirirken insan (mimar) veya yapay zeka hafızasının yanılabileceğini, bu yüzden README.md gibi statik "Görev Takip Listesi" dosyalarının ne kadar hayati bir "Gerçeklik Kaynağı" (Source of Truth) olduğunu yaşayarak öğrendim.
•	Yapay zeka asistanlarının sadece "işlevi yerine getiren" kodlar yazdığını, "Kullanıcı Deneyimi (UX)" gibi insani faktörlerde tamamen kör olabildiğini tecrübe ettim.
•	Kodu elle değiştirmek yerine ajana "Neyi, nereye ve nasıl düzeltmesi gerektiğini" anlatan noktasal promptlar vermenin (Vibe Coding), projeyi bozma riskini minimize ettiğini yaşayarak gördüm.

### Sonraki Oturum İçin Notlar
Uygulamanın tasarım iskeleti ve rotaları hazır. Bir sonraki aşamada Çoklu Dil Sistemi (Görev 5.1, 5.2, 5.3) veya ana simülasyon motorunun inşasına (Görev 6 serisi) geçiş yapılacak.

---

## Oturum 6 - 26 Mayıs 2026 - 20:10-21:30

### Hedef
1. Uygulamanın çoklu dil desteği (i18n) altyapısının kurulması ve optimize edilmesi. (Görev 5.1)
2. Projenin kalbi olan saf (pure) İş Mantığı (Business Logic) katmanının, yani Simülasyon Motorunun (Simulation Engine) inşa edilmesi. (Görev 6.1)
3. Simülasyon motorunun kullanıcı arayüzü ile konuşabilmesi için gerekli Blueprint rotalarının (Görev 6.2) ve WTForms tabanlı veri giriş formlarının (Görev 6.3) sisteme entegre edilmesi.

### Kullandığım Mod ve Model
•	Mod: Thinking
•	Model: Gemini 3.1 Pro (Mimari Yönlendirme), Claude 4.6 (Kod Üretimi), DeepSeek (Code Review)
•	Görünüm: Antigravity IDE - Agent Chat / Editor View

### Ajanın Önerdiği Plan ve Müdahalelerim
•	Görev Konsolidasyonu (Anayasa Müdahalesi): README dosyasında üçe bölünmüş olan dil sistemi görevlerini Vibe Coding sürecini bölmemek adına git status teyidi ile "Görev 5.1" altında birleştirdim.
•	Performans (Cache) ve Encoding Koruması: DeepSeek'in tavsiyesiyle dil motoruna müdahale ettim. _cache = {} sözlüğü ile önbellek mekanizması kurdurttum ve okuma işlemine zorunlu encoding='utf-8' parametresini eklettim.
•	Çoklu Model (Multi-Agent) Çapraz Denetimi (Görev 6.1): Simülasyon motorunu Claude modeline yazdırırken, tıbbi limitleri belirlerken DeepSeek'in (Code Reviewer) anayasadaki config ayarlarını hatırlatmasıyla tıbbi bir mantık hatasının (hiperglisemi sınırının 140'tan 180'e çekilmesi) önüne geçtim. Ayrıca motorun Türkçe metin döndürmesini engelleyip, i18n çeviri sistemine uygun İngilizce anahtarlar döndürmesini sağladım.
•	Rota ve Form Bütünlüğü Koruma (Görev 6.2 & 6.3): Flask mimarisinde formsuz bir POST rotasının ImportError vereceğini öngörerek, ajanın "Sadece rota yaz" emriyle sistemi çökertmesini engelledim. İşlemi iki aşamaya böldüm: Önce sadece GET isteği karşılayan güvenli rotayı yazdırdım, ardından Bootstrap 5 ve CSRF korumalı formları güvenle rotaya monte ettirdim.

### Üretilen Kodda Düzelttiklerim / Belirlediklerim
•	app/translations/__init__.py içerisine güvenli yol bulma, utf-8 koruması, önbellekleme ve çökmeye karşı exception zırhı eklendi.
•	app/simulation/engine.py dosyasına tıbbi limitler (20-600), ve ondalık yuvarlama (round) içeren sektörel bir hesaplama motoru eklendi.
•	app/simulation/forms.py dosyası WTForms zırhıyla (DataRequired, NumberRange) oluşturuldu.
•	app/simulation/routes.py içine POST sonrası mükerrer form gönderimini engelleyen PRG (Post/Redirect/Get) paterni başarıyla kuruldu ve hatalı girişlerde kullanıcıyı uyaran Bootstrap 5 tabanlı hata mesajı döngüleri sisteme eklendi.

### Bu Oturumdan Öğrendiğim
•	Farklı yapay zeka modellerini birbirini denetleyecek şekilde (Claude'u kod yazarı, DeepSeek'i Code Reviewer, Gemini'ı Mimar olarak) kullanmanın, oluşabilecek tıbbi ve mimari mantık hatalarını nasıl sıfıra indirdiğini tecrübe ettim.
•	Kullanıcıdan veri alırken (Form), sadece HTML tarafında değil, Backend tarafında da (WTForms validators) sınırların belirlenmesinin siber güvenlik ve veri bütünlüğü (Data Integrity) açısından ne kadar kritik olduğunu öğrendim.

### Sonraki Oturum İçin Notlar
Dil motoru, simülasyon hesaplama altyapısı ve simülasyon arayüzü tamamen hazır. Bir sonraki adımda, kullanıcının yediği öğünleri veritabanına kaydedip listeleyebileceği "Meals (Öğünler)" sistemine (Görev 7 serisi) geçiş yapılacaktır.
