🦋 Fafatara Downloader
Modern, hızlı ve kullanımı kolay YouTube video, müzik ve oynatma listesi indirme uygulaması.
✨ Özellikler
🎬 MP4 video indirme
🎵 MP3 müzik indirme
📋 YouTube oynatma listesi indirme
📁 Oynatma listelerini ayrı klasörlerde saklama
⚡ Yüksek kaliteli video indirme
🎧 MP3 kalite seçimi
📊 Gerçek zamanlı indirme yüzdesi
📂 İndirme konumu seçme
🕘 Önceki indirmeleri görüntüleme
📋 Daha önce indirilen oynatma listelerini görüntüleme
⚙️ İndirme ayarlarını özelleştirme
🦋 Modern ve kullanıcı dostu arayüz
🪟 Windows desteği
🐧 Linux desteği
---
🪟 Windows
Windows sürümünü GitHub Releases bölümünden indirebilirsiniz.
Arşivi çıkardıktan sonra:
    Fafatara Downloader.exe

dosyasını çalıştırmanız yeterlidir.
Python, pip veya ek bir kurulum gerektirmeden hazırlanmış sürüm için GitHub Releases bölümündeki hazır paketi kullanabilirsiniz.
---
🐧 Linux
Linux sürümünü GitHub Releases bölümünden indirebilirsiniz.
Arşivi çıkardıktan sonra uygulamanın bulunduğu klasöre girin.
Terminal üzerinden:
    ./Fafatara\ Downloader/Fafatara\ Downloader

komutuyla çalıştırabilirsiniz.
Eğer çalıştırma izni verilmemişse:
    chmod +x "Fafatara Downloader/Fafatara Downloader"

ardından:
    ./Fafatara\ Downloader/Fafatara\ Downloader

komutunu kullanabilirsiniz.
---
🛠️ Geliştirme
Gereksinimler
Python 3.11
FFmpeg
Deno
Git
Projeyi klonlama
    git clone https://github.com/KULLANICI_ADIN/Fafatara-Downloader.git

Proje klasörüne girin:
    cd Fafatara-Downloader

---
🐍 Sanal ortam oluşturma
Windows
    python -m venv .venv

Sanal ortamı etkinleştirin:
    .venv\Scripts\activate

Linux
    python3 -m venv .venv

Sanal ortamı etkinleştirin:
    source .venv/bin/activate

---
📦 Bağımlılıkları yükleme
Sanal ortam aktifken:
    python -m pip install -r requirements.txt

---
▶️ Uygulamayı çalıştırma
Windows:
    python main.py

Linux:
    python3 main.py

---
🏗️ Windows Build
Windows üzerinde:
    build_windows.bat

komutunu çalıştırın.
Build tamamlandığında:
    dist/
    └── Fafatara Downloader/
        └── Fafatara Downloader.exe

oluşturulur.
---
🏗️ Linux Build
Linux üzerinde:
    chmod +x build_linux.sh

ardından:
    ./build_linux.sh

Build tamamlandığında:
    dist/
    └── Fafatara Downloader/
        └── Fafatara Downloader

oluşturulur.
---
🤖 GitHub Actions
Proje GitHub'a gönderildiğinde GitHub Actions otomatik olarak Windows ve Linux sürümlerini oluşturabilir.
Workflow dosyası:
    .github/
    └── workflows/
        └── build.yml

GitHub'daki Actions sekmesinden build işlemlerini takip edebilirsiniz.
Build başarılı olduğunda Windows ve Linux paketleri Actions içerisindeki Artifacts bölümünden alınabilir.
---
📁 Proje Yapısı
    Fafatara-Downloader/
    │
    ├── main.py
    ├── downloader.py
    ├── requirements.txt
    ├── logo.ico
    ├── logo.png
    │
    ├── build_windows.bat
    ├── build_linux.sh
    │
    ├── README.md
    ├── LICENSE
    ├── .gitignore
    │
    └── .github/
        └── workflows/
            └── build.yml

---
📥 İndirme Klasörü
Fafatara Downloader varsayılan olarak kullanıcının Downloads klasörü içerisinde:
    Fafatara Downloader

adında bir klasör oluşturur.
Örneğin Windows'ta:
    C:\Users\KullanıcıAdı\Downloads\Fafatara Downloader

Oynatma listeleri ise kendi adlarıyla ayrı klasörlerde saklanır:
    Fafatara Downloader/
    │
    ├── Video 1.mp4
    ├── Video 2.mp4
    ├── Müzik.mp3
    │
    └── Playlist Adı/
        ├── Video A.mp4
        ├── Video B.mp4
        └── Video C.mp4

Oynatma listesindeki dosyaların başına otomatik olarak 1-, 2-, 3- gibi numaralar eklenmez.
---
⚙️ Ayarlar
Uygulamanın Ayarlar bölümünden:
İndirme konumu
Varsayılan video kalitesi
Varsayılan MP3 kalitesi
gibi seçenekler değiştirilebilir.
---
📜 Lisans
Bu proje MIT lisansı altında yayımlanmaktadır.
Detaylar için LICENSE dosyasına bakabilirsiniz.
---
⚠️ Sorumluluk
Fafatara Downloader, kullanıcıların internet üzerindeki içeriklere daha kolay erişebilmesi amacıyla geliştirilmiş bir yazılımdır.
İndirdiğiniz içeriklerin telif haklarına, kullanım koşullarına ve ilgili platformların kurallarına uymak kullanıcının sorumluluğundadır.
Yalnızca indirme ve kullanma hakkınız bulunan içerikleri indirmeniz önerilir.
---
🦋 Fafatara Downloader
Reklamlarla, yanıltıcı indirme butonlarıyla ve gereksiz yazılımlarla dolu indirme sitelerine alternatif olarak; sade, kullanışlı ve kullanıcı deneyimine odaklanan bir masaüstü uygulaması olarak geliştirilmiştir.
Amaç, kullanıcıya mümkün olduğunca temiz ve anlaşılır bir indirme deneyimi sunmaktır.
---
❤️ Geliştirici
Made with ❤️ by Feyyaz
🦋 Fafatara Downloader