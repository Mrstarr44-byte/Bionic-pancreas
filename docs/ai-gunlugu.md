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
Git/GitHub altyapısının kurulması, projenin anayasası niteliğindeki README.md (kısıtlamalar ve görev listesi) dosyasının oluşturulması, Görev 1.1 (Klasör Yapısı) ve Görev 1.2 (requirements.txt) adımlarının tamamlanması.

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
"Terminal Command Auto Execution: Request Review" ayarının hayat kurtarıcı olduğunu bizzat tecrübe ettim. Ajan arka planda kafasına göre komut çalıştıramadığı için her adımda ne yaptığını denetleme şansım oldu. Ayrıca, README.md dosyasını bir "sabit hafıza" olarak kullandığımda, modeli Gemini'den Claude'a geçirsem bile yeni modelin README'yi okuyarak hiçbir context (bağlam) kaybı yaşamadan aynı kurallarla yola devam edebildiğini öğrendim.
