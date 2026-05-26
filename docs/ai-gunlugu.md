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
•	Model: Gemini 3.5 Flash (Başlangıç), Claude Opus 4.6 (Dosya ağacı üretimi), Gemini 3.1 Pro (Mimari ve Kodlama), DeepSeek (Code Review / Hata Ayıklama)
•	Görünüm: Antigravity IDE - Agent Chat (Editor View)

### Verdiğim Promptlar
1.	Proje dizininde docs klasörü oluşturulması ve dokümantasyonun başlatılması.
2.	Hazırladığım 18 maddelik "Proje Anayasası ve AI Kısıtlamaları" metninin tam olarak README.md dosyasına yazdırılması ve .gitignore dosyasının oluşturulması.
3.	Claude Opus 4.6'ya geçiş: "README.md dosyasını oku ve Görev 1.1'i (Klasör yapısını) çift alt çizgili __init__.py kurallarına dikkat ederek oluştur."
4.	"Harika. Şimdi Görev 1.2'yi yap ve requirements.txt içine belirttiğim paketleri (Flask==3.1.0 vb.) sürüm numaralarıyla sabitleyerek ekle."
5.	Gemini 3.1 Pro'ya geçiş: "Görev 1.3 — app/config.py Yaz. Ortam değişkenlerinden okuyan bir Config sınıfı oluştur."
6.	"Görev 1.4 — app/init.py factory sistemi. create_app fonksiyonunu yaz ve eklentileri bağla, blueprintleri register et."
7.	Gemini 3.1 Pro'ya (Yama Promptu): "app/init.py dosyası harika oldu ancak uygulamanın ImportError verip çökmemesi için 7 adet blueprint klasörünün içindeki boş init.py dosyalarını aç ve her biri için temel Blueprint nesnelerini tanımla."

### Ajanın Önerdiği Plan ve Müdahalelerim
•	Git ve GitHub Entegrasyon Krizi: Terminal üzerinden ilk commit'leri atarken MacOS'un "akıllı tırnak" özelliği yüzünden terminalde dquote> hatası (askıda kalma durumu) yaşadım. Ajanın doğrudan müdahale edemediği bu donanım/işletim sistemi sorununu, Ctrl+C ile işlemi iptal edip, commit mesajlarında çift tırnak yerine tek tırnak (') kullanarak kendim çözdüm.
•	Kritik Müdahale (Ajanın Adım Adım İlerlemesi): Görev 1.1'i verdiğimde, ajan terminalde sadece mkdir komutu ile boş klasörleri oluşturmak için izin istedi. İlk başta eksik yaptığını düşündüm ancak "Request Review" (Sandbox onayı) özelliği sayesinde ajanın önce iskeleti kurup sonra dosyaları içine yerleştirme stratejisi izlediğini fark ettim. İlk adıma onay verip süreci kontrol altında tuttum.
•	Kritik Çapraz Sorgu (Cross-Validation) ve Hata Yakalama: Gemini, Görev 1.4'te create_app fonksiyonunu kusursuz yazdı ve main, auth gibi blueprintleri app/__init__.py içinde import etti. Ancak projenin güvenliğinden emin olmak için yazılan kodu DeepSeek'e incelettim. DeepSeek bana hayati bir uyarı yaptı: Blueprint klasörlerinin içindeki __init__.py dosyaları şu an boş, dolayısıyla from app.main import bp komutu bir ImportError fırlatacak ve uygulama çökecek. Gemini'ye hemen ek bir komut vererek bu durumu düzelttirdim.

### Üretilen Kodda Düzelttiklerim / Belirlediklerim
•	Sürüm Çakışması Önlemi: Ajanın requirements.txt dosyasını kendi inisiyatifiyle doldurmasına izin vermedim. İleride dağıtım (deployment) aşamasında veya farklı ortamda uyumsuzluk çıkmaması için Flask, SQLAlchemy vb. bağımlılıkların versiyonlarını teker teker ben belirleyip ajana dikte ettim.
•	Blueprint Çökme Yaması (Runtime Fix): Gemini'nin 1.4'te yazdığı factory kodu yanlış değildi, sadece Görev 1.1'de dosyaları bilerek boş bıraktırmıştık. Ancak uygulamanın crash olmaması kuralı gereği 7 farklı blueprint'in __init__.py dosyasına sadece temel bp = Blueprint(...) tanımlamalarını yaptırıp projeyi zırhlı hale getirdim.

### Bu Oturumdan Öğrendiğim
"Terminal Command Auto Execution: Request Review" ayarının hayat kurtarıcı olduğunu tecrübe ettim. README.md dosyasını "sabit hafıza" olarak kullandığımda, modeller arası geçiş (Claude -> Gemini) yapsam bile context kaybı yaşanmadığını gördüm. Ayrıca, yapay zekanın yazdığı kod syntax olarak doğru olsa bile, projenin o anki bağlamına göre çalışma zamanı (runtime) hataları verebileceğini öğrendim. Farklı AI modellerini birbirine denetletmek (Gemini'ye yazdırıp DeepSeek'e audit yaptırmak) geleneksel debug sürecini çok daha güvenli hale getiriyor.

---

## Oturum 3 - 26 Mayıs 2026 - 12:30-14:10

### Hedef
Projenin veritabanı modellerinin (Görev 2.1) SQLAlchemy 2.x standartlarına (Mapped, mapped_column) uygun olarak oluşturulması ve iş mantığı (business logic) hatalarının giderilmesi.

### Kullandığım Mod ve Model
•	Mod: Plan ve Fast
•	Model: Gemini 3.1 Pro, Claude Opus 4.6 (Kod Üretimi) ve DeepSeek (Code Review / Çapraz Sorgu)
•	Görünüm: Antigravity IDE - Agent Chat (Editor View)

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

## Oturum 4 - 26 Mayıs 2026 - 14:40-15:50

### Hedef
1. Görev 2.2 (Flask-Migrate yapılandırması) adımıyla modellerin fiziksel SQLite veritabanına dönüştürülmesi.
2. Görev 3.1 (forms.py - Kimlik Doğrulama Formlarının Oluşturulması) adımının tamamlanması.

### Kullandığım Mod ve Model
•	Mod: Plan ve Fast (Kademeli ilerleme için)
•	Model: Gemini 3.5 Flash (Başlangıç), Gemini 3 Pro (High) / Claude Opus 4.6 (Kod Üretimi / Thinking) ve DeepSeek (Code Review)
•	Görünüm: Antigravity IDE - Agent Chat / Editor View

### Ajanın Önerdiği Plan ve Müdahalelerim
•	AI Halüsinasyonu ve Görev Sırası İhlali (Görev 2.2): Ajan, FLASK_APP ortam değişkenini atayabilmek için run.py dosyasına ihtiyacı olduğunu iddia ederek Görev 13.4'e atlamaya ve run.py dosyasını oluşturmaya kalkıştı.
•	Mimari Müdahale (Override): Bir yazılım mimarı olarak bu isteği "Reject" ettim (reddettim). Ajana projede "Application Factory" deseni kullandığımızı, Flask CLI'ın export FLASK_APP=app komutuyla create_app fonksiyonunu otomatik tanıyacağını ve run.py dosyasına şu aşamada kesinlikle ihtiyaç olmadığını belirttim. README anayasamızdaki "Görev sırası değiştirilemez" kuralını hatırlatarak ajanı hizaya soktum.
•	Eksik Paket Tuzağı (Dependency Check - Görev 3.1): Ajan WTForms içindeki `Email()` validator'ını doğrudan yazıp geçmeye çalıştı. Ancak bu validator'ın çalışabilmesi için arka planda `email-validator` harici paketinin kurulu olması gerektiğini, aksi halde runtime'da sistemin çökeceğini fark ettim. Kod üretilmeden önce ajana `pip install email-validator` komutunu çalıştırıp bağımlılığı `requirements.txt` dosyasına eklettim.
•	Mimari Güvenlik Önlemleri: Form içi dinamik veritabanı kontrollerinde döngüsel kilitlenmeyi (circular import) engellemek amacıyla `from app import db` içe aktarımını küresel yerine yerel metot scope'larında (`validate_username`, `validate_email`) çözdürdüm. Model sorgularını ise tamamen SQLAlchemy 2.x (`db.select`) standartlarında yazdırdım.

### Üretilen Kodda Düzelttiklerim / Belirlediklerim
•	Ajanın yanlışlıkla oluşturmaya yeltendiği run.py dosyasını rm -f run.py komutuyla sildirdim. Ardından doğrudan flask db init, migrate ve upgrade komutlarını onaylayarak 3 tablomuzu barındıran bionic_pancreas.db (36 KB) dosyasının başarıyla oluşturulmasını sağladım.
•	`app/forms.py` dosyası `LoginForm` ve `RegistrationForm` sınıflarıyla eksiksiz dolduruldu; `requirements.txt` güncellendi.

### Bu Oturumdan Öğrendiğim
•	Yapay zeka araçlarının "bu olmadan şu çalışmaz" şeklindeki kesin yargılarına (hallucination) her zaman güvenmemek gerektiğini öğrendim. Framework'ün (Flask) derin çalışma mantığını (CLI ve Application Factory) bilmek, beni gereksiz dosyalar oluşturmaktan ve proje anayasasını ihlal etmekten kurtardı.
•	Kriz Yönetimi (Git Geçmişi Temizliği): Projede `.gitignore` dosyasının eksik olduğunu ve `venv` (sanal ortam) klasörünün yanlışlıkla Git takibine alındığını fark ettim. Binlerce kütüphane dosyasının GitHub'a pushlanıp repository'i şişirmesini (ve rubrikten eksi puan almayı) önlemek için acil müdahale ettim. Terminalden `git rm -r --cached venv` komutuyla klasörü takipten çıkardım ve ajana hızlıca standartlara uygun bir `.gitignore` dosyası oluşturttum.
•	Framework bileşenlerinin yerleşik görünen metotlarının arka plandaki gizli bağımlılıklarını (peer dependencies) önceden analiz etmenin, projenin canlıya çıkış (deployment) aşamasındaki kritik hataları henüz lokalde temizlemek adına ne kadar hayati olduğunu öğrendim.

### Sonraki Oturum İçin Notlar
Kullanıcı giriş/çıkış ve kayıt rotalarını canlandıracağımız Görev 3.2 (auth blueprint routes) adımına geçilecek.
