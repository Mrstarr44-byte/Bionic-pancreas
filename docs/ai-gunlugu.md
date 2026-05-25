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
