import os
import sys
import json

from PySide6.QtCore import (
    Qt,
    QThread,
    Signal
)

from PySide6.QtGui import (
    QIcon,
    QPixmap
)

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QProgressBar,
    QMessageBox,
    QFrame,
    QListWidget,
    QListWidgetItem,
    QCheckBox,
    QFileDialog,
    QStackedWidget
)


APP_NAME = "Fafatara Downloader"

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

ASSETS_DIR = os.path.join(
    BASE_DIR,
    "assets"
)

LOGO_PATH = os.path.join(
    ASSETS_DIR,
    "logo.png"
)

SETTINGS_PATH = os.path.join(
    BASE_DIR,
    "settings.json"
)


# =========================================================
# SETTINGS
# =========================================================


# =========================================================
# LANGUAGE / TRANSLATIONS
# =========================================================

LANGUAGES = {
    "en": "English",
    "tr": "Türkçe",
    "de": "Deutsch",
    "es": "Español",
    "fr": "Français",
    "it": "Italiano",
    "pt": "Português",
    "ru": "Русский",
    "zh": "简体中文",
}

TRANSLATIONS = {
    "tr": {
        "Hoş Geldin 👋": "Hoş Geldin 👋",
        "Videolarını, müziklerini ve playlistlerini kolayca indir.": "Videolarını, müziklerini ve playlistlerini kolayca indir.",
        "İndirmeler": "İndirmeler", "Daha önce indirdiğin dosyalar.": "Daha önce indirdiğin dosyalar.",
        "Playlist": "Playlist", "Playlistler": "Playlistler", "Daha önce indirdiğin playlistler.": "Daha önce indirdiğin playlistler.",
        "Ayarlar": "Ayarlar", "Fafatara Downloader ayarlarını buradan yönet.": "Fafatara Downloader ayarlarını buradan yönet.",
        "Hakkında": "Hakkında", "FORMAT": "FORMAT", "KALİTE": "KALİTE", "İNDİRME KONUMU": "İNDİRME KONUMU",
        "Tümünü Seç": "Tümünü Seç", "🔗  YouTube bağlantısını buraya yapıştır...": "🔗  YouTube bağlantısını buraya yapıştır...",
        "⌕  ANALİZ ET": "⌕  ANALİZ ET", "🦋   İNDİRMEYİ BAŞLAT": "🦋   İNDİRMEYİ BAŞLAT",
        "Hazır": "Hazır", "Henüz indirme başlatılmadı.": "Henüz indirme başlatılmadı.",
        "İndirme Konumu": "İndirme Konumu", "İndirilen dosyaların kaydedileceği ana klasör.": "İndirilen dosyaların kaydedileceği ana klasör.",
        "📁 Klasör Seç": "📁 Klasör Seç", "Varsayılan Format": "Varsayılan Format",
        "Uygulama açıldığında seçili olacak format.": "Uygulama açıldığında seçili olacak format.",
        "Varsayılan Video Kalitesi": "Varsayılan Video Kalitesi", "MP4 indirirken kullanılacak varsayılan kalite.": "MP4 indirirken kullanılacak varsayılan kalite.",
        "Varsayılan MP3 Kalitesi": "Varsayılan MP3 Kalitesi", "MP3 indirirken kullanılacak ses kalitesi.": "MP3 indirirken kullanılacak ses kalitesi.",
        "✓  AYARLARI KAYDET": "✓  AYARLARI KAYDET", "↻  Yenile": "↻  Yenile",
        "Sürüm 1.0.0": "Sürüm 1.0.0", "Dil": "Dil", "Uygulama dili": "Uygulama dili",
        "Ayarlar başarıyla kaydedildi.": "Ayarlar başarıyla kaydedildi.", "Önce YouTube bağlantısını gir.": "Önce YouTube bağlantısını gir.",
        "Bağlantı analiz ediliyor...": "Bağlantı analiz ediliyor...", "Video hazır.": "Video hazır.",
        "Analiz başarısız.": "Analiz başarısız.", "YouTube bağlantısı gir.": "YouTube bağlantısı gir.",
        "İndirme başlıyor...": "İndirme başlıyor...", "İndiriliyor  •  ": "İndiriliyor  •  ",
        "Dosya işleniyor...": "Dosya işleniyor...", "✓  İndirme tamamlandı": "✓  İndirme tamamlandı",
        "İndirme başarıyla tamamlandı.": "İndirme başarıyla tamamlandı.", "✕  İndirme başarısız": "✕  İndirme başarısız",
        "İndirme Hatası": "İndirme Hatası", "İndirme klasörü seç": "İndirme klasörü seç",
        "Henüz indirilen dosya yok.": "Henüz indirilen dosya yok.", "Henüz playlist indirilmedi.": "Henüz playlist indirilmedi.",
        "about_text": "Fafatara Downloader, internet üzerindeki video ve müzik indirme deneyimini daha sade, temiz ve kullanışlı hale getirmek amacıyla geliştirilmiştir.\n\nİnternette kullanıcıları gereksiz reklamlar, açılır pencereler ve şüpheli indirme butonlarıyla karşı karşıya bırakan birçok indirme sitesi bulunmaktadır.\n\nFafatara Downloader bu karmaşık deneyime karşı sade bir masaüstü alternatif sunmayı amaçlar.\n\nUygulama MP4, MP3, yüksek kaliteli video, ses kalitesi ve playlist indirme özelliklerini tek bir arayüzde bir araya getirir.\n\nFafatara Downloader bağımsız olarak geliştirilmektedir.",
        "footer": "🦋 Fafatara Downloader  •  Made with ❤️ by Feyyaz",
        "video hazır.": "video hazır.",
        "Bilinmeyen video": "Bilinmeyen video",
    },
    "en": {
        "Hoş Geldin 👋": "Welcome 👋", "Videolarını, müziklerini ve playlistlerini kolayca indir.": "Download your videos, music and playlists with ease.",
        "İndirmeler": "Downloads", "Daha önce indirdiğin dosyalar.": "Your previously downloaded files.",
        "Playlist": "Playlist", "Playlistler": "Playlists", "Daha önce indirdiğin playlistler.": "Your previously downloaded playlists.",
        "Ayarlar": "Settings", "Fafatara Downloader ayarlarını buradan yönet.": "Manage Fafatara Downloader settings here.",
        "Hakkında": "About", "FORMAT": "FORMAT", "KALİTE": "QUALITY", "İNDİRME KONUMU": "DOWNLOAD LOCATION",
        "Tümünü Seç": "Select All", "🔗  YouTube bağlantısını buraya yapıştır...": "🔗  Paste YouTube link here...",
        "⌕  ANALİZ ET": "⌕  ANALYZE", "🦋   İNDİRMEYİ BAŞLAT": "🦋   START DOWNLOAD",
        "Hazır": "Ready", "Henüz indirme başlatılmadı.": "No download started yet.",
        "İndirme Konumu": "Download Location", "İndirilen dosyaların kaydedileceği ana klasör.": "Main folder where downloaded files are saved.",
        "📁 Klasör Seç": "📁 Choose Folder", "Varsayılan Format": "Default Format",
        "Uygulama açıldığında seçili olacak format.": "The format selected when the application starts.",
        "Varsayılan Video Kalitesi": "Default Video Quality", "MP4 indirirken kullanılacak varsayılan kalite.": "Default quality for MP4 downloads.",
        "Varsayılan MP3 Kalitesi": "Default MP3 Quality", "MP3 indirirken kullanılacak ses kalitesi.": "Audio quality for MP3 downloads.",
        "✓  AYARLARI KAYDET": "✓  SAVE SETTINGS", "↻  Yenile": "↻  Refresh",
        "Sürüm 1.0.0": "Version 1.0.0", "Dil": "Language", "Uygulama dili": "Application language",
        "Ayarlar başarıyla kaydedildi.": "Settings saved successfully.", "Önce YouTube bağlantısını gir.": "Enter a YouTube link first.",
        "Bağlantı analiz ediliyor...": "Analyzing link...", "Video hazır.": "Video ready.",
        "Analiz başarısız.": "Analysis failed.", "YouTube bağlantısı gir.": "Enter a YouTube link.",
        "İndirme başlıyor...": "Starting download...", "İndiriliyor  •  ": "Downloading  •  ",
        "Dosya işleniyor...": "Processing file...", "✓  İndirme tamamlandı": "✓  Download completed",
        "İndirme başarıyla tamamlandı.": "Download completed successfully.", "✕  İndirme başarısız": "✕  Download failed",
        "İndirme Hatası": "Download Error", "İndirme klasörü seç": "Choose download folder",
        "Henüz indirilen dosya yok.": "No downloaded files yet.", "Henüz playlist indirilmedi.": "No playlists downloaded yet.",
        "about_text": "Fafatara Downloader was developed to make downloading videos and music from the internet simpler, cleaner and easier to use.\n\nMany download sites expose users to unnecessary ads, pop-ups and suspicious download buttons.\n\nFafatara Downloader aims to provide a simple desktop alternative to this complicated experience.\n\nThe application brings MP4, MP3, high-quality video, audio quality and playlist downloads together in one interface.\n\nFafatara Downloader is developed independently.",
        "footer": "🦋 Fafatara Downloader  •  Made with ❤️ by Feyyaz",
    },
}

# Additional languages. Unlisted strings fall back to English so every
# control remains usable even if a future text is added.
TRANSLATIONS.update({
    "de": {"Hoş Geldin 👋":"Willkommen 👋","Videolarını, müziklerini ve playlistlerini kolayca indir.":"Lade Videos, Musik und Playlists einfach herunter.","İndirmeler":"Downloads","Daha önce indirdiğin dosyalar.":"Zuvor heruntergeladene Dateien.","Playlist":"Playlist","Playlistler":"Playlists","Daha önce indirdiğin playlistler.":"Zuvor heruntergeladene Playlists.","Ayarlar":"Einstellungen","Fafatara Downloader ayarlarını buradan yönet.":"Verwalte hier die Einstellungen von Fafatara Downloader.","Hakkında":"Über","KALİTE":"QUALITÄT","İNDİRME KONUMU":"DOWNLOAD-ORDNER","Tümünü Seç":"Alle auswählen","🔗  YouTube bağlantısını buraya yapıştır...":"🔗  YouTube-Link hier einfügen...","⌕  ANALİZ ET":"⌕  ANALYSIEREN","🦋   İNDİRMEYİ BAŞLAT":"🦋   DOWNLOAD STARTEN","Hazır":"Bereit","Henüz indirme başlatılmadı.":"Noch kein Download gestartet.","İndirme Konumu":"Download-Ordner","İndirilen dosyaların kaydedileceği ana klasör.":"Hauptordner für heruntergeladene Dateien.","📁 Klasör Seç":"📁 Ordner auswählen","Varsayılan Format":"Standardformat","Uygulama açıldığında seçili olacak format.":"Format beim Start.","Varsayılan Video Kalitesi":"Standard-Videoqualität","Varsayılan MP3 Kalitesi":"Standard-MP3-Qualität","✓  AYARLARI KAYDET":"✓  EINSTELLUNGEN SPEICHERN","↻  Yenile":"↻  Aktualisieren","Dil":"Sprache","Uygulama dili":"Anwendungssprache","Ayarlar başarıyla kaydedildi.":"Einstellungen gespeichert.","Önce YouTube bağlantısını gir.":"Gib zuerst einen YouTube-Link ein.","Bağlantı analiz ediliyor...":"Link wird analysiert...","Video hazır.":"Video bereit.","Analiz başarısız.":"Analyse fehlgeschlagen.","YouTube bağlantısı gir.":"Gib einen YouTube-Link ein.","İndirme başlıyor...":"Download wird gestartet...","İndiriliyor  •  ":"Wird heruntergeladen  •  ","Dosya işleniyor...":"Datei wird verarbeitet...","✓  İndirme tamamlandı":"✓  Download abgeschlossen","İndirme başarıyla tamamlandı.":"Download erfolgreich abgeschlossen.","✕  İndirme başarısız":"✕  Download fehlgeschlagen","İndirme Hatası":"Download-Fehler","İndirme klasörü seç":"Download-Ordner auswählen","Henüz indirilen dosya yok.":"Noch keine Dateien heruntergeladen.","Henüz playlist indirilmedi.":"Noch keine Playlists heruntergeladen.","about_text":"Fafatara Downloader wurde entwickelt, um das Herunterladen von Videos und Musik aus dem Internet einfacher und übersichtlicher zu machen.\n\nDie Anwendung bietet eine einfache Desktop-Alternative zu komplizierten Download-Seiten.\n\nMP4, MP3, hochwertige Video-, Audio- und Playlist-Downloads werden in einer Oberfläche vereint.","footer":"🦋 Fafatara Downloader  •  Made with ❤️ by Feyyaz"},
    "es": {"Hoş Geldin 👋":"Bienvenido 👋","Videolarını, müziklerini ve playlistlerini kolayca indir.":"Descarga vídeos, música y listas de reproducción fácilmente.","İndirmeler":"Descargas","Daha önce indirdiğin dosyalar.":"Tus archivos descargados.","Playlist":"Lista","Playlistler":"Listas","Daha önce indirdiğin playlistler.":"Tus listas descargadas.","Ayarlar":"Ajustes","Fafatara Downloader ayarlarını buradan yönet.":"Gestiona aquí los ajustes de Fafatara Downloader.","Hakkında":"Acerca de","KALİTE":"CALIDAD","İNDİRME KONUMU":"UBICACIÓN DE DESCARGA","Tümünü Seç":"Seleccionar todo","🔗  YouTube bağlantısını buraya yapıştır...":"🔗  Pega el enlace de YouTube aquí...","⌕  ANALİZ ET":"⌕  ANALIZAR","🦋   İNDİRMEYİ BAŞLAT":"🦋   INICIAR DESCARGA","Hazır":"Listo","Henüz indirme başlatılmadı.":"No se ha iniciado ninguna descarga.","İndirme Konumu":"Ubicación de descarga","📁 Klasör Seç":"📁 Elegir carpeta","Varsayılan Format":"Formato predeterminado","Varsayılan Video Kalitesi":"Calidad de vídeo predeterminada","Varsayılan MP3 Kalitesi":"Calidad MP3 predeterminada","✓  AYARLARI KAYDET":"✓  GUARDAR AJUSTES","↻  Yenile":"↻  Actualizar","Dil":"Idioma","Uygulama dili":"Idioma de la aplicación","Ayarlar başarıyla kaydedildi.":"Ajustes guardados correctamente.","Önce YouTube bağlantısını gir.":"Introduce primero un enlace de YouTube.","Bağlantı analiz ediliyor...":"Analizando enlace...","Video hazır.":"Vídeo listo.","Analiz başarısız.":"Error de análisis.","YouTube bağlantısı gir.":"Introduce un enlace de YouTube.","İndirme başlıyor...":"Iniciando descarga...","İndiriliyor  •  ":"Descargando  •  ","Dosya işleniyor...":"Procesando archivo...","✓  İndirme tamamlandı":"✓  Descarga completada","İndirme başarıyla tamamlandı.":"Descarga completada correctamente.","✕  İndirme başarısız":"✕  Descarga fallida","İndirme Hatası":"Error de descarga","İndirme klasörü seç":"Elegir carpeta de descarga","Henüz indirilen dosya yok.":"Aún no hay archivos descargados.","Henüz playlist indirilmedi.":"Aún no hay listas descargadas.","about_text":"Fafatara Downloader fue desarrollado para hacer más sencilla y cómoda la descarga de vídeos y música de Internet.","footer":"🦋 Fafatara Downloader  •  Made with ❤️ by Feyyaz"},
    "fr": {"Hoş Geldin 👋":"Bienvenue 👋","Videolarını, müziklerini ve playlistlerini kolayca indir.":"Téléchargez facilement vos vidéos, musiques et playlists.","İndirmeler":"Téléchargements","Daha önce indirdiğin dosyalar.":"Vos fichiers téléchargés.","Playlist":"Playlist","Playlistler":"Playlists","Daha önce indirdiğin playlistler.":"Vos playlists téléchargées.","Ayarlar":"Paramètres","Fafatara Downloader ayarlarını buradan yönet.":"Gérez les paramètres de Fafatara Downloader ici.","Hakkında":"À propos","KALİTE":"QUALITÉ","İNDİRME KONUMU":"EMPLACEMENT DE TÉLÉCHARGEMENT","Tümünü Seç":"Tout sélectionner","🔗  YouTube bağlantısını buraya yapıştır...":"🔗  Collez le lien YouTube ici...","⌕  ANALİZ ET":"⌕  ANALYSER","🦋   İNDİRMEYİ BAŞLAT":"🦋   DÉMARRER LE TÉLÉCHARGEMENT","Hazır":"Prêt","Henüz indirme başlatılmadı.":"Aucun téléchargement démarré.","İndirme Konumu":"Emplacement de téléchargement","📁 Klasör Seç":"📁 Choisir un dossier","Varsayılan Format":"Format par défaut","Varsayılan Video Kalitesi":"Qualité vidéo par défaut","Varsayılan MP3 Kalitesi":"Qualité MP3 par défaut","✓  AYARLARI KAYDET":"✓  ENREGISTRER","↻  Yenile":"↻  Actualiser","Dil":"Langue","Uygulama dili":"Langue de l’application","Ayarlar başarıyla kaydedildi.":"Paramètres enregistrés.","Önce YouTube bağlantısını gir.":"Entrez d’abord un lien YouTube.","Bağlantı analiz ediliyor...":"Analyse du lien...","Video hazır.":"Vidéo prête.","Analiz başarısız.":"Échec de l’analyse.","YouTube bağlantısı gir.":"Entrez un lien YouTube.","İndirme başlıyor...":"Démarrage du téléchargement...","İndiriliyor  •  ":"Téléchargement  •  ","Dosya işleniyor...":"Traitement du fichier...","✓  İndirme tamamlandı":"✓  Téléchargement terminé","İndirme başarıyla tamamlandı.":"Téléchargement terminé avec succès.","✕  İndirme başarısız":"✕  Échec du téléchargement","İndirme Hatası":"Erreur de téléchargement","İndirme klasörü seç":"Choisir le dossier de téléchargement","Henüz indirilen dosya yok.":"Aucun fichier téléchargé.","Henüz playlist indirilmedi.":"Aucune playlist téléchargée.","about_text":"Fafatara Downloader a été conçu pour rendre le téléchargement de vidéos et de musique depuis Internet plus simple et pratique.","footer":"🦋 Fafatara Downloader  •  Made with ❤️ by Feyyaz"},
    "it": {"Hoş Geldin 👋":"Benvenuto 👋","Videolarını, müziklerini ve playlistlerini kolayca indir.":"Scarica facilmente video, musica e playlist.","İndirmeler":"Download","Daha önce indirdiğin dosyalar.":"I tuoi file scaricati.","Playlist":"Playlist","Playlistler":"Playlist","Daha önce indirdiğin playlistler.":"Le tue playlist scaricate.","Ayarlar":"Impostazioni","Fafatara Downloader ayarlarını buradan yönet.":"Gestisci qui le impostazioni di Fafatara Downloader.","Hakkında":"Informazioni","KALİTE":"QUALITÀ","İNDİRME KONUMU":"POSIZIONE DOWNLOAD","Tümünü Seç":"Seleziona tutto","🔗  YouTube bağlantısını buraya yapıştır...":"🔗  Incolla qui il link di YouTube...","⌕  ANALİZ ET":"⌕  ANALIZZA","🦋   İNDİRMEYİ BAŞLAT":"🦋   AVVIA DOWNLOAD","Hazır":"Pronto","Henüz indirme başlatılmadı.":"Nessun download avviato.","İndirme Konumu":"Posizione download","📁 Klasör Seç":"📁 Scegli cartella","Varsayılan Format":"Formato predefinito","Varsayılan Video Kalitesi":"Qualità video predefinita","Varsayılan MP3 Kalitesi":"Qualità MP3 predefinita","✓  AYARLARI KAYDET":"✓  SALVA IMPOSTAZIONI","↻  Yenile":"↻  Aggiorna","Dil":"Lingua","Uygulama dili":"Lingua dell’applicazione","Ayarlar başarıyla kaydedildi.":"Impostazioni salvate.","Önce YouTube bağlantısını gir.":"Inserisci prima un link YouTube.","Bağlantı analiz ediliyor...":"Analisi del link...","Video hazır.":"Video pronto.","Analiz başarısız.":"Analisi non riuscita.","YouTube bağlantısı gir.":"Inserisci un link YouTube.","İndirme başlıyor...":"Avvio download...","İndiriliyor  •  ":"Download  •  ","Dosya işleniyor...":"Elaborazione file...","✓  İndirme tamamlandı":"✓  Download completato","İndirme başarıyla tamamlandı.":"Download completato.","✕  İndirme başarısız":"✕  Download non riuscito","İndirme Hatası":"Errore di download","İndirme klasörü seç":"Scegli cartella download","Henüz indirilen dosya yok.":"Nessun file scaricato.","Henüz playlist indirilmedi.":"Nessuna playlist scaricata.","about_text":"Fafatara Downloader è stato sviluppato per rendere più semplice e pratico il download di video e musica da Internet.","footer":"🦋 Fafatara Downloader  •  Made with ❤️ by Feyyaz"},
    "pt": {"Hoş Geldin 👋":"Bem-vindo 👋","Videolarını, müziklerini ve playlistlerini kolayca indir.":"Baixe vídeos, músicas e playlists facilmente.","İndirmeler":"Downloads","Daha önce indirdiğin dosyalar.":"Seus arquivos baixados.","Playlist":"Playlist","Playlistler":"Playlists","Daha önce indirdiğin playlistler.":"Suas playlists baixadas.","Ayarlar":"Configurações","Fafatara Downloader ayarlarını buradan yönet.":"Gerencie as configurações do Fafatara Downloader aqui.","Hakkında":"Sobre","KALİTE":"QUALIDADE","İNDİRME KONUMU":"LOCAL DE DOWNLOAD","Tümünü Seç":"Selecionar tudo","🔗  YouTube bağlantısını buraya yapıştır...":"🔗  Cole o link do YouTube aqui...","⌕  ANALİZ ET":"⌕  ANALISAR","🦋   İNDİRMEYİ BAŞLAT":"🦋   INICIAR DOWNLOAD","Hazır":"Pronto","Henüz indirme başlatılmadı.":"Nenhum download iniciado.","İndirme Konumu":"Local de download","📁 Klasör Seç":"📁 Escolher pasta","Varsayılan Format":"Formato padrão","Varsayılan Video Kalitesi":"Qualidade de vídeo padrão","Varsayılan MP3 Kalitesi":"Qualidade MP3 padrão","✓  AYARLARI KAYDET":"✓  SALVAR CONFIGURAÇÕES","↻  Yenile":"↻  Atualizar","Dil":"Idioma","Uygulama dili":"Idioma do aplicativo","Ayarlar başarıyla kaydedildi.":"Configurações salvas.","Önce YouTube bağlantısını gir.":"Insira primeiro um link do YouTube.","Bağlantı analiz ediliyor...":"Analisando link...","Video hazır.":"Vídeo pronto.","Analiz başarısız.":"Falha na análise.","YouTube bağlantısı gir.":"Insira um link do YouTube.","İndirme başlıyor...":"Iniciando download...","İndiriliyor  •  ":"Baixando  •  ","Dosya işleniyor...":"Processando arquivo...","✓  İndirme tamamlandı":"✓  Download concluído","İndirme başarıyla tamamlandı.":"Download concluído com sucesso.","✕  İndirme başarısız":"✕  Falha no download","İndirme Hatası":"Erro de download","İndirme klasörü seç":"Escolher pasta de download","Henüz indirilen dosya yok.":"Nenhum arquivo baixado.","Henüz playlist indirilmedi.":"Nenhuma playlist baixada.","about_text":"O Fafatara Downloader foi desenvolvido para tornar o download de vídeos e músicas da Internet mais simples e prático.","footer":"🦋 Fafatara Downloader  •  Made with ❤️ by Feyyaz"},
    "ru": {"Hoş Geldin 👋":"Добро пожаловать 👋","Videolarını, müziklerini ve playlistlerini kolayca indir.":"Легко скачивайте видео, музыку и плейлисты.","İndirmeler":"Загрузки","Daha önce indirdiğin dosyalar.":"Ранее загруженные файлы.","Playlist":"Плейлист","Playlistler":"Плейлисты","Daha önce indirdiğin playlistler.":"Ранее загруженные плейлисты.","Ayarlar":"Настройки","Fafatara Downloader ayarlarını buradan yönet.":"Управляйте настройками Fafatara Downloader здесь.","Hakkında":"О программе","KALİTE":"КАЧЕСТВО","İNDİRME KONUMU":"ПАПКА ЗАГРУЗКИ","Tümünü Seç":"Выбрать все","🔗  YouTube bağlantısını buraya yapıştır...":"🔗  Вставьте ссылку YouTube сюда...","⌕  ANALİZ ET":"⌕  АНАЛИЗИРОВАТЬ","🦋   İNDİRMEYİ BAŞLAT":"🦋   НАЧАТЬ ЗАГРУЗКУ","Hazır":"Готово","Henüz indirme başlatılmadı.":"Загрузка ещё не начата.","İndirme Konumu":"Папка загрузки","📁 Klasör Seç":"📁 Выбрать папку","Varsayılan Format":"Формат по умолчанию","Varsayılan Video Kalitesi":"Качество видео по умолчанию","Varsayılan MP3 Kalitesi":"Качество MP3 по умолчанию","✓  AYARLARI KAYDET":"✓  СОХРАНИТЬ НАСТРОЙКИ","↻  Yenile":"↻  Обновить","Dil":"Язык","Uygulama dili":"Язык приложения","Ayarlar başarıyla kaydedildi.":"Настройки сохранены.","Önce YouTube bağlantısını gir.":"Сначала введите ссылку YouTube.","Bağlantı analiz ediliyor...":"Анализ ссылки...","Video hazır.":"Видео готово.","Analiz başarısız.":"Ошибка анализа.","YouTube bağlantısı gir.":"Введите ссылку YouTube.","İndirme başlıyor...":"Начало загрузки...","İndiriliyor  •  ":"Загрузка  •  ","Dosya işleniyor...":"Обработка файла...","✓  İndirme tamamlandı":"✓  Загрузка завершена","İndirme başarıyla tamamlandı.":"Загрузка успешно завершена.","✕  İndirme başarısız":"✕  Загрузка не удалась","İndirme Hatası":"Ошибка загрузки","İndirme klasörü seç":"Выбрать папку загрузки","Henüz indirilen dosya yok.":"Загруженных файлов пока нет.","Henüz playlist indirilmedi.":"Плейлисты пока не загружены.","about_text":"Fafatara Downloader создан для того, чтобы сделать загрузку видео и музыки из Интернета проще и удобнее.","footer":"🦋 Fafatara Downloader  •  Made with ❤️ by Feyyaz"},
    "zh": {"Hoş Geldin 👋":"欢迎 👋","Videolarını, müziklerini ve playlistlerini kolayca indir.":"轻松下载视频、音乐和播放列表。","İndirmeler":"下载","Daha önce indirdiğin dosyalar.":"之前下载的文件。","Playlist":"播放列表","Playlistler":"播放列表","Daha önce indirdiğin playlistler.":"之前下载的播放列表。","Ayarlar":"设置","Fafatara Downloader ayarlarını buradan yönet.":"在这里管理 Fafatara Downloader 设置。","Hakkında":"关于","KALİTE":"质量","İNDİRME KONUMU":"下载位置","Tümünü Seç":"全选","🔗  YouTube bağlantısını buraya yapıştır...":"🔗  在此粘贴 YouTube 链接...","⌕  ANALİZ ET":"⌕  分析","🦋   İNDİRMEYİ BAŞLAT":"🦋   开始下载","Hazır":"就绪","Henüz indirme başlatılmadı.":"尚未开始下载。","İndirme Konumu":"下载位置","📁 Klasör Seç":"📁 选择文件夹","Varsayılan Format":"默认格式","Varsayılan Video Kalitesi":"默认视频质量","Varsayılan MP3 Kalitesi":"默认 MP3 质量","✓  AYARLARI KAYDET":"✓  保存设置","↻  Yenile":"↻  刷新","Dil":"语言","Uygulama dili":"应用语言","Ayarlar başarıyla kaydedildi.":"设置已保存。","Önce YouTube bağlantısını gir.":"请先输入 YouTube 链接。","Bağlantı analiz ediliyor...":"正在分析链接...","Video hazır.":"视频已准备好。","Analiz başarısız.":"分析失败。","YouTube bağlantısı gir.":"请输入 YouTube 链接。","İndirme başlıyor...":"开始下载...","İndiriliyor  •  ":"正在下载  •  ","Dosya işleniyor...":"正在处理文件...","✓  İndirme tamamlandı":"✓  下载完成","İndirme başarıyla tamamlandı.":"下载成功完成。","✕  İndirme başarısız":"✕  下载失败","İndirme Hatası":"下载错误","İndirme klasörü seç":"选择下载文件夹","Henüz indirilen dosya yok.":"暂无下载文件。","Henüz playlist indirilmedi.":"暂无下载的播放列表。","about_text":"Fafatara Downloader 旨在让从互联网下载视频和音乐变得更加简单、清晰和方便。","footer":"🦋 Fafatara Downloader  •  Made with ❤️ by Feyyaz"},
})

DEFAULT_SETTINGS = {
    "download_folder": "",
    "format": "MP4",
    "quality": "1080p",
    "audio_quality": "320",
    "language": "en"
}


def load_settings():

    settings = DEFAULT_SETTINGS.copy()

    if os.path.exists(
        SETTINGS_PATH
    ):

        try:

            with open(
                SETTINGS_PATH,
                "r",
                encoding="utf-8"
            ) as file:

                saved = json.load(
                    file
                )

                if isinstance(
                    saved,
                    dict
                ):

                    settings.update(
                        saved
                    )

        except Exception:
            pass

    if not settings.get(
        "download_folder"
    ):

        downloads = os.path.join(
            os.path.expanduser("~"),
            "Downloads"
        )

        settings[
            "download_folder"
        ] = os.path.join(
            downloads,
            "Fafatara Downloader"
        )

    os.makedirs(
        settings[
            "download_folder"
        ],
        exist_ok=True
    )

    return settings


def save_settings(
    settings
):

    with open(
        SETTINGS_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            settings,
            file,
            ensure_ascii=False,
            indent=4
        )


# =========================================================
# DOWNLOAD THREAD
# =========================================================

class DownloadThread(QThread):

    progress = Signal(dict)

    finished_signal = Signal()

    error = Signal(str)

    def __init__(
        self,
        url,
        mode,
        quality,
        audio_quality,
        output_dir
    ):

        super().__init__()

        self.url = url

        self.mode = mode

        self.quality = quality

        self.audio_quality = audio_quality

        self.output_dir = output_dir

    def run(self):

        try:

            from downloader import Downloader

            downloader = Downloader(
                self.output_dir
            )

            downloader.download(
                self.url,
                self.mode,
                self.quality,
                self.progress.emit,
                self.audio_quality
            )

            self.finished_signal.emit()

        except Exception as e:

            self.error.emit(
                str(e)
            )


# =========================================================
# PLAYLIST THREAD
# =========================================================

class PlaylistThread(QThread):

    result = Signal(dict)

    error = Signal(str)

    def __init__(
        self,
        url
    ):

        super().__init__()

        self.url = url

    def run(self):

        try:

            from downloader import Downloader

            downloader = Downloader()

            result = downloader.get_playlist_info(
                self.url
            )

            self.result.emit(
                result
            )

        except Exception as e:

            self.error.emit(
                str(e)
            )


# =========================================================
# MAIN WINDOW
# =========================================================

class FafataraDownloader(
    QWidget
):

    def __init__(self):

        super().__init__()

        self.settings = load_settings()

        self.download_thread = None

        self.playlist_thread = None

        self.setWindowTitle(
            APP_NAME
        )

        self.setMinimumSize(
            1100,
            680
        )

        self.resize(
            1250,
            760
        )

        if os.path.exists(
            LOGO_PATH
        ):

            self.setWindowIcon(
                QIcon(
                    LOGO_PATH
                )
            )

        self.build_ui()

        self.register_translation_widgets()
        self.retranslate_ui()

        self.apply_theme()

        self.show_home()

    def t(self, key):
        language = self.settings.get("language", "en")
        if language not in TRANSLATIONS:
            language = "en"
        return TRANSLATIONS.get(language, {}).get(
            key,
            TRANSLATIONS["en"].get(key, key)
        )

    def register_translation_widgets(self):
        self._translation_widgets = []
        for widget in self.findChildren(QWidget):
            if isinstance(widget, (QLabel, QPushButton, QCheckBox)):
                value = widget.text()
                if value in TRANSLATIONS["tr"] or value in TRANSLATIONS["en"]:
                    widget.setProperty("_translation_key", value)
                    self._translation_widgets.append(("text", widget))
            if isinstance(widget, QLineEdit):
                value = widget.placeholderText()
                if value in TRANSLATIONS["tr"] or value in TRANSLATIONS["en"]:
                    widget.setProperty("_translation_placeholder", value)
                    self._translation_widgets.append(("placeholder", widget))

    def retranslate_ui(self):
        for kind, widget in getattr(self, "_translation_widgets", []):
            if kind == "text":
                key = widget.property("_translation_key")
                widget.setText(self.t(key))
            else:
                key = widget.property("_translation_placeholder")
                widget.setPlaceholderText(self.t(key))

        if hasattr(self, "about_text"):
            self.about_text.setText(self.t("about_text"))

        if hasattr(self, "footer"):
            self.footer.setText(self.t("footer"))

        if hasattr(self, "settings_language"):
            current = self.settings.get("language", "en")
            self.settings_language.blockSignals(True)
            self.settings_language.clear()
            for code, name in LANGUAGES.items():
                self.settings_language.addItem(name, code)
            self.settings_language.setCurrentIndex(
                max(0, self.settings_language.findData(current))
            )
            self.settings_language.blockSignals(False)

    def change_language(self, index):
        if not hasattr(self, "settings_language"):
            return
        code = self.settings_language.itemData(index)
        if code not in LANGUAGES:
            return
        self.settings["language"] = code
        save_settings(self.settings)
        self.retranslate_ui()

    # =====================================================
    # BUILD
    # =====================================================

    def build_ui(self):

        root = QHBoxLayout()

        root.setContentsMargins(
            0,
            0,
            0,
            0
        )

        root.setSpacing(
            0
        )

        # =================================================
        # SIDEBAR
        # =================================================

        sidebar = QFrame()

        sidebar.setObjectName(
            "sidebar"
        )

        sidebar.setFixedWidth(
            230
        )

        sidebar_layout = QVBoxLayout()

        sidebar_layout.setContentsMargins(
            18,
            20,
            18,
            15
        )

        sidebar_layout.setSpacing(
            7
        )

        # LOGO

        logo = QLabel()

        if os.path.exists(
            LOGO_PATH
        ):

            pixmap = QPixmap(
                LOGO_PATH
            )

            pixmap = pixmap.scaled(
                100,
                100,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            logo.setPixmap(
                pixmap
            )

        else:

            logo.setText(
                "🦋"
            )

        logo.setAlignment(
            Qt.AlignCenter
        )

        logo.setObjectName(
            "logoImage"
        )

        sidebar_layout.addWidget(
            logo
        )

        logo_title = QLabel(
            "FAFATARA"
        )

        logo_title.setObjectName(
            "logoTitle"
        )

        logo_title.setAlignment(
            Qt.AlignCenter
        )

        sidebar_layout.addWidget(
            logo_title
        )

        logo_subtitle = QLabel(
            "DOWNLOADER"
        )

        logo_subtitle.setObjectName(
            "logoSubtitle"
        )

        logo_subtitle.setAlignment(
            Qt.AlignCenter
        )

        sidebar_layout.addWidget(
            logo_subtitle
        )

        sidebar_layout.addSpacing(
            18
        )

        self.home_button = self.sidebar_button(
            "⌂",
            "Ana Sayfa"
        )

        self.downloads_button = self.sidebar_button(
            "↓",
            "İndirmeler"
        )

        self.playlist_button = self.sidebar_button(
            "☷",
            "Playlist"
        )

        self.settings_button = self.sidebar_button(
            "⚙",
            "Ayarlar"
        )

        self.about_button = self.sidebar_button(
            "ⓘ",
            "Hakkında"
        )

        self.home_button.clicked.connect(
            self.show_home
        )

        self.downloads_button.clicked.connect(
            self.show_downloads
        )

        self.playlist_button.clicked.connect(
            self.show_playlists
        )

        self.settings_button.clicked.connect(
            self.show_settings
        )

        self.about_button.clicked.connect(
            self.show_about
        )

        sidebar_layout.addWidget(
            self.home_button
        )

        sidebar_layout.addWidget(
            self.downloads_button
        )

        sidebar_layout.addWidget(
            self.playlist_button
        )

        sidebar_layout.addWidget(
            self.settings_button
        )

        sidebar_layout.addWidget(
            self.about_button
        )

        sidebar_layout.addStretch()

        version = QLabel(
            "FAFATARA\nv1.0.0"
        )

        version.setObjectName(
            "version"
        )

        version.setAlignment(
            Qt.AlignCenter
        )

        sidebar_layout.addWidget(
            version
        )

        sidebar.setLayout(
            sidebar_layout
        )

        root.addWidget(
            sidebar
        )

        # =================================================
        # PAGES
        # =================================================

        self.pages = QStackedWidget()

        self.home_page = self.create_home_page()

        self.downloads_page = self.create_downloads_page()

        self.playlists_page = self.create_playlists_page()

        self.settings_page = self.create_settings_page()

        self.about_page = self.create_about_page()

        self.pages.addWidget(
            self.home_page
        )

        self.pages.addWidget(
            self.downloads_page
        )

        self.pages.addWidget(
            self.playlists_page
        )

        self.pages.addWidget(
            self.settings_page
        )

        self.pages.addWidget(
            self.about_page
        )

        root.addWidget(
            self.pages,
            1
        )

        self.setLayout(
            root
        )

    # =====================================================
    # SIDEBAR BUTTON
    # =====================================================

    def sidebar_button(
        self,
        icon,
        text
    ):

        button = QPushButton(
            f"{icon}    {text}"
        )

        button.setObjectName(
            "sidebarButton"
        )

        button.setMinimumHeight(
            45
        )

        return button

    # =====================================================
    # HOME
    # =====================================================

    def create_home_page(
        self
    ):

        page = QWidget()

        layout = QVBoxLayout()

        layout.setContentsMargins(
            35,
            25,
            35,
            10
        )

        layout.setSpacing(
            14
        )

        # HEADER

        header = QHBoxLayout()

        header_text = QVBoxLayout()

        title = QLabel(
            "Hoş Geldin 👋"
        )

        title.setObjectName(
            "mainTitle"
        )

        subtitle = QLabel(
            "Videolarını, müziklerini ve playlistlerini kolayca indir."
        )

        subtitle.setObjectName(
            "mainSubtitle"
        )

        header_text.addWidget(
            title
        )

        header_text.addWidget(
            subtitle
        )

        header.addLayout(
            header_text
        )

        header.addStretch()

        youtube = QLabel(
            "▶ YouTube"
        )

        youtube.setObjectName(
            "youtube"
        )

        header.addWidget(
            youtube
        )

        layout.addLayout(
            header
        )

        # URL

        url_card = QFrame()

        url_card.setObjectName(
            "card"
        )

        url_layout = QHBoxLayout()

        url_layout.setContentsMargins(
            18,
            14,
            18,
            14
        )

        self.url_input = QLineEdit()

        self.url_input.setPlaceholderText(
            "🔗  YouTube bağlantısını buraya yapıştır..."
        )

        self.url_input.setMinimumHeight(
            46
        )

        self.analyze_button = QPushButton(
            "⌕  ANALİZ ET"
        )

        self.analyze_button.setObjectName(
            "analyzeButton"
        )

        self.analyze_button.setMinimumHeight(
            46
        )

        self.analyze_button.setMinimumWidth(
            140
        )

        self.analyze_button.clicked.connect(
            self.analyze_playlist
        )

        url_layout.addWidget(
            self.url_input
        )

        url_layout.addWidget(
            self.analyze_button
        )

        url_card.setLayout(
            url_layout
        )

        layout.addWidget(
            url_card
        )

        # OPTIONS

        options = QHBoxLayout()

        options.setSpacing(
            14
        )

        # FORMAT

        format_card = QFrame()

        format_card.setObjectName(
            "card"
        )

        format_card.setMinimumWidth(
            170
        )

        format_layout = QVBoxLayout()

        format_title = QLabel(
            "FORMAT"
        )

        format_title.setObjectName(
            "smallTitle"
        )

        self.format_combo = QComboBox()

        self.format_combo.addItems([
            "MP4",
            "MP3"
        ])

        self.format_combo.setMinimumHeight(
            40
        )

        self.format_combo.setMinimumWidth(
            150
        )

        current_format = self.settings.get(
            "format",
            "MP4"
        )

        index = self.format_combo.findText(
            current_format
        )

        if index >= 0:

            self.format_combo.setCurrentIndex(
                index
            )

        self.format_combo.currentTextChanged.connect(
            self.update_quality_options
        )

        format_layout.addWidget(
            format_title
        )

        format_layout.addWidget(
            self.format_combo
        )

        format_card.setLayout(
            format_layout
        )

        options.addWidget(
            format_card,
            2
        )

        # QUALITY

        quality_card = QFrame()

        quality_card.setObjectName(
            "card"
        )

        quality_card.setMinimumWidth(
            190
        )

        quality_layout = QVBoxLayout()

        quality_title = QLabel(
            "KALİTE"
        )

        quality_title.setObjectName(
            "smallTitle"
        )

        self.quality_combo = QComboBox()

        self.quality_combo.setMinimumHeight(
            40
        )

        self.quality_combo.setMinimumWidth(
            175
        )

        quality_layout.addWidget(
            quality_title
        )

        quality_layout.addWidget(
            self.quality_combo
        )

        quality_card.setLayout(
            quality_layout
        )

        options.addWidget(
            quality_card,
            2
        )

        # FOLDER

        folder_card = QFrame()

        folder_card.setObjectName(
            "card"
        )

        folder_layout = QVBoxLayout()

        folder_title = QLabel(
            "İNDİRME KONUMU"
        )

        folder_title.setObjectName(
            "smallTitle"
        )

        folder_row = QHBoxLayout()

        self.folder_input = QLineEdit(
            self.settings[
                "download_folder"
            ]
        )

        self.folder_input.setReadOnly(
            True
        )

        folder_button = QPushButton(
            "📁"
        )

        folder_button.setFixedWidth(
            48
        )

        folder_button.clicked.connect(
            self.choose_folder
        )

        folder_row.addWidget(
            self.folder_input
        )

        folder_row.addWidget(
            folder_button
        )

        folder_layout.addWidget(
            folder_title
        )

        folder_layout.addLayout(
            folder_row
        )

        folder_card.setLayout(
            folder_layout
        )

        options.addWidget(
            folder_card,
            3
        )

        layout.addLayout(
            options
        )

        # PLAYLIST

        self.playlist_card = QFrame()

        self.playlist_card.setObjectName(
            "card"
        )

        playlist_layout = QVBoxLayout()

        playlist_header = QHBoxLayout()

        self.playlist_info = QLabel(
            "Playlist"
        )

        self.playlist_info.setObjectName(
            "playlistTitle"
        )

        self.select_all = QCheckBox(
            "Tümünü Seç"
        )

        self.select_all.setChecked(
            True
        )

        self.select_all.stateChanged.connect(
            self.toggle_all
        )

        playlist_header.addWidget(
            self.playlist_info
        )

        playlist_header.addStretch()

        playlist_header.addWidget(
            self.select_all
        )

        self.playlist_list = QListWidget()

        self.playlist_list.setMinimumHeight(
            100
        )

        playlist_layout.addLayout(
            playlist_header
        )

        playlist_layout.addWidget(
            self.playlist_list
        )

        self.playlist_card.setLayout(
            playlist_layout
        )

        self.playlist_card.setVisible(
            False
        )

        layout.addWidget(
            self.playlist_card
        )

        # DOWNLOAD

        self.download_button = QPushButton(
            "🦋   İNDİRMEYİ BAŞLAT"
        )

        self.download_button.setObjectName(
            "downloadButton"
        )

        self.download_button.setMinimumHeight(
            56
        )

        self.download_button.clicked.connect(
            self.start_download
        )

        layout.addWidget(
            self.download_button
        )

        # PROGRESS

        progress_card = QFrame()

        progress_card.setObjectName(
            "progressCard"
        )

        progress_layout = QVBoxLayout()

        progress_layout.setContentsMargins(
            12,
            10,
            12,
            10
        )

        progress_header = QHBoxLayout()

        self.status_label = QLabel(
            "Hazır"
        )

        self.status_label.setObjectName(
            "statusTitle"
        )

        self.percent_label = QLabel(
            "0%"
        )

        self.percent_label.setObjectName(
            "percent"
        )

        progress_header.addWidget(
            self.status_label
        )

        progress_header.addStretch()

        progress_header.addWidget(
            self.percent_label
        )

        self.progress_bar = QProgressBar()

        self.progress_bar.setValue(
            0
        )

        self.progress_bar.setTextVisible(
            False
        )

        self.file_label = QLabel(
            "Henüz indirme başlatılmadı."
        )

        self.file_label.setObjectName(
            "fileLabel"
        )

        progress_layout.addLayout(
            progress_header
        )

        progress_layout.addWidget(
            self.progress_bar
        )

        progress_layout.addWidget(
            self.file_label
        )

        progress_card.setLayout(
            progress_layout
        )

        layout.addWidget(
            progress_card
        )

        # FOOTER

        self.footer = QLabel(
            self.t("footer")
        )

        self.footer.setObjectName(
            "footer"
        )

        self.footer.setAlignment(
            Qt.AlignCenter
        )

        layout.addWidget(
            self.footer
        )

        page.setLayout(
            layout
        )

        # İlk kalite listesi

        self.update_quality_options(
            self.format_combo.currentText()
        )

        return page

    # =====================================================
    # QUALITY
    # =====================================================

    def update_quality_options(
        self,
        format_name
    ):

        if not hasattr(
            self,
            "quality_combo"
        ):

            return

        old_value = self.quality_combo.currentText()

        self.quality_combo.blockSignals(
            True
        )

        self.quality_combo.clear()

        if format_name == "MP3":

            qualities = [
                "320 kbps",
                "256 kbps",
                "192 kbps",
                "128 kbps",
                "96 kbps"
            ]

            saved = (
                self.settings.get(
                    "audio_quality",
                    "320"
                )
                + " kbps"
            )

            self.quality_combo.addItems(
                qualities
            )

            if old_value in qualities:

                self.quality_combo.setCurrentText(
                    old_value
                )

            elif saved in qualities:

                self.quality_combo.setCurrentText(
                    saved
                )

            else:

                self.quality_combo.setCurrentText(
                    "320 kbps"
                )

        else:

            qualities = [
                "4320p",
                "2160p",
                "1440p",
                "1080p",
                "720p",
                "480p",
                "360p"
            ]

            saved = self.settings.get(
                "quality",
                "1080p"
            )

            self.quality_combo.addItems(
                qualities
            )

            if old_value in qualities:

                self.quality_combo.setCurrentText(
                    old_value
                )

            elif saved in qualities:

                self.quality_combo.setCurrentText(
                    saved
                )

            else:

                self.quality_combo.setCurrentText(
                    "1080p"
                )

        self.quality_combo.blockSignals(
            False
        )

    # =====================================================
    # DOWNLOADS PAGE
    # =====================================================

    def create_downloads_page(
        self
    ):

        page = QWidget()

        layout = QVBoxLayout()

        layout.setContentsMargins(
            35,
            25,
            35,
            20
        )

        title = QLabel(
            "İndirmeler"
        )

        title.setObjectName(
            "pageTitle"
        )

        subtitle = QLabel(
            "Daha önce indirdiğin dosyalar."
        )

        subtitle.setObjectName(
            "pageSubtitle"
        )

        self.downloads_list = QListWidget()

        refresh = QPushButton(
            "↻  Yenile"
        )

        refresh.clicked.connect(
            self.refresh_downloads
        )

        layout.addWidget(
            title
        )

        layout.addWidget(
            subtitle
        )

        layout.addWidget(
            self.downloads_list
        )

        layout.addWidget(
            refresh
        )

        page.setLayout(
            layout
        )

        return page

    # =====================================================
    # PLAYLIST PAGE
    # =====================================================

    def create_playlists_page(
        self
    ):

        page = QWidget()

        layout = QVBoxLayout()

        layout.setContentsMargins(
            35,
            25,
            35,
            20
        )

        title = QLabel(
            "Playlistler"
        )

        title.setObjectName(
            "pageTitle"
        )

        subtitle = QLabel(
            "Daha önce indirdiğin playlistler."
        )

        subtitle.setObjectName(
            "pageSubtitle"
        )

        self.playlists_list = QListWidget()

        refresh = QPushButton(
            "↻  Yenile"
        )

        refresh.clicked.connect(
            self.refresh_playlists
        )

        layout.addWidget(
            title
        )

        layout.addWidget(
            subtitle
        )

        layout.addWidget(
            self.playlists_list
        )

        layout.addWidget(
            refresh
        )

        page.setLayout(
            layout
        )

        return page

    # =====================================================
    # SETTINGS PAGE
    # =====================================================

    def create_settings_page(
        self
    ):

        page = QWidget()

        layout = QVBoxLayout()

        layout.setContentsMargins(
            35,
            25,
            35,
            20
        )

        layout.setSpacing(
            12
        )

        title = QLabel(
            "Ayarlar"
        )

        title.setObjectName(
            "pageTitle"
        )

        subtitle = QLabel(
            "Fafatara Downloader ayarlarını buradan yönet."
        )

        subtitle.setObjectName(
            "pageSubtitle"
        )

        layout.addWidget(
            title
        )

        layout.addWidget(
            subtitle
        )

        # -------------------------------------------------
        # LANGUAGE
        # -------------------------------------------------

        language_card = QFrame()
        language_card.setObjectName("card")
        language_layout = QVBoxLayout()

        language_title = QLabel("Dil")
        language_title.setObjectName("settingTitle")

        language_desc = QLabel("Uygulama dili")
        language_desc.setObjectName("settingDescription")

        self.settings_language = QComboBox()
        for code, name in LANGUAGES.items():
            self.settings_language.addItem(name, code)
        self.settings_language.setCurrentIndex(
            max(0, self.settings_language.findData(self.settings.get("language", "en")))
        )
        self.settings_language.currentIndexChanged.connect(self.change_language)

        language_layout.addWidget(language_title)
        language_layout.addWidget(language_desc)
        language_layout.addWidget(self.settings_language)
        language_card.setLayout(language_layout)
        layout.addWidget(language_card)

        # -------------------------------------------------
        # DOWNLOAD FOLDER
        # -------------------------------------------------

        folder_card = QFrame()

        folder_card.setObjectName(
            "card"
        )

        folder_layout = QVBoxLayout()

        folder_title = QLabel(
            "İndirme Konumu"
        )

        folder_title.setObjectName(
            "settingTitle"
        )

        folder_desc = QLabel(
            "İndirilen dosyaların kaydedileceği ana klasör."
        )

        folder_desc.setObjectName(
            "settingDescription"
        )

        folder_row = QHBoxLayout()

        self.settings_folder = QLineEdit(
            self.settings[
                "download_folder"
            ]
        )

        self.settings_folder.setReadOnly(
            True
        )

        choose = QPushButton(
            "📁 Klasör Seç"
        )

        choose.clicked.connect(
            self.choose_settings_folder
        )

        folder_row.addWidget(
            self.settings_folder
        )

        folder_row.addWidget(
            choose
        )

        folder_layout.addWidget(
            folder_title
        )

        folder_layout.addWidget(
            folder_desc
        )

        folder_layout.addLayout(
            folder_row
        )

        folder_card.setLayout(
            folder_layout
        )

        layout.addWidget(
            folder_card
        )

        # -------------------------------------------------
        # FORMAT
        # -------------------------------------------------

        format_card = QFrame()

        format_card.setObjectName(
            "card"
        )

        format_layout = QVBoxLayout()

        format_title = QLabel(
            "Varsayılan Format"
        )

        format_title.setObjectName(
            "settingTitle"
        )

        format_desc = QLabel(
            "Uygulama açıldığında seçili olacak format."
        )

        format_desc.setObjectName(
            "settingDescription"
        )

        self.settings_format = QComboBox()

        self.settings_format.addItems([
            "MP4",
            "MP3"
        ])

        index = self.settings_format.findText(
            self.settings[
                "format"
            ]
        )

        if index >= 0:

            self.settings_format.setCurrentIndex(
                index
            )

        format_layout.addWidget(
            format_title
        )

        format_layout.addWidget(
            format_desc
        )

        format_layout.addWidget(
            self.settings_format
        )

        format_card.setLayout(
            format_layout
        )

        layout.addWidget(
            format_card
        )

        # -------------------------------------------------
        # VIDEO QUALITY
        # -------------------------------------------------

        quality_card = QFrame()

        quality_card.setObjectName(
            "card"
        )

        quality_layout = QVBoxLayout()

        quality_title = QLabel(
            "Varsayılan Video Kalitesi"
        )

        quality_title.setObjectName(
            "settingTitle"
        )

        quality_desc = QLabel(
            "MP4 indirirken kullanılacak varsayılan kalite."
        )

        quality_desc.setObjectName(
            "settingDescription"
        )

        self.settings_quality = QComboBox()

        self.settings_quality.addItems([
            "4320p",
            "2160p",
            "1440p",
            "1080p",
            "720p",
            "480p",
            "360p"
        ])

        index = self.settings_quality.findText(
            self.settings[
                "quality"
            ]
        )

        if index >= 0:

            self.settings_quality.setCurrentIndex(
                index
            )

        quality_layout.addWidget(
            quality_title
        )

        quality_layout.addWidget(
            quality_desc
        )

        quality_layout.addWidget(
            self.settings_quality
        )

        quality_card.setLayout(
            quality_layout
        )

        layout.addWidget(
            quality_card
        )

        # -------------------------------------------------
        # MP3 QUALITY
        # -------------------------------------------------

        audio_card = QFrame()

        audio_card.setObjectName(
            "card"
        )

        audio_layout = QVBoxLayout()

        audio_title = QLabel(
            "Varsayılan MP3 Kalitesi"
        )

        audio_title.setObjectName(
            "settingTitle"
        )

        audio_desc = QLabel(
            "MP3 indirirken kullanılacak ses kalitesi."
        )

        audio_desc.setObjectName(
            "settingDescription"
        )

        self.settings_audio_quality = QComboBox()

        self.settings_audio_quality.addItems([
            "320 kbps",
            "256 kbps",
            "192 kbps",
            "128 kbps",
            "96 kbps"
        ])

        saved_audio = (
            self.settings.get(
                "audio_quality",
                "320"
            )
            + " kbps"
        )

        index = self.settings_audio_quality.findText(
            saved_audio
        )

        if index >= 0:

            self.settings_audio_quality.setCurrentIndex(
                index
            )

        audio_layout.addWidget(
            audio_title
        )

        audio_layout.addWidget(
            audio_desc
        )

        audio_layout.addWidget(
            self.settings_audio_quality
        )

        audio_card.setLayout(
            audio_layout
        )

        layout.addWidget(
            audio_card
        )

        # SAVE

        save = QPushButton(
            "✓  AYARLARI KAYDET"
        )

        save.setObjectName(
            "downloadButton"
        )

        save.setMinimumHeight(
            52
        )

        save.clicked.connect(
            self.save_app_settings
        )

        layout.addWidget(
            save
        )

        layout.addStretch()

        page.setLayout(
            layout
        )

        return page

    # =====================================================
    # ABOUT
    # =====================================================

    def create_about_page(
        self
    ):

        page = QWidget()

        layout = QVBoxLayout()

        layout.setContentsMargins(
            35,
            25,
            35,
            20
        )

        title = QLabel(
            "Hakkında"
        )

        title.setObjectName(
            "pageTitle"
        )

        card = QFrame()

        card.setObjectName(
            "aboutCard"
        )

        card_layout = QVBoxLayout()

        logo = QLabel()

        if os.path.exists(
            LOGO_PATH
        ):

            pixmap = QPixmap(
                LOGO_PATH
            )

            pixmap = pixmap.scaled(
                130,
                130,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            logo.setPixmap(
                pixmap
            )

        else:

            logo.setText(
                "🦋"
            )

        logo.setAlignment(
            Qt.AlignCenter
        )

        card_layout.addWidget(
            logo
        )

        app_title = QLabel(
            "Fafatara Downloader"
        )

        app_title.setObjectName(
            "aboutTitle"
        )

        app_title.setAlignment(
            Qt.AlignCenter
        )

        card_layout.addWidget(
            app_title
        )

        version = QLabel(
            "Sürüm 1.0.0"
        )

        version.setObjectName(
            "aboutVersion"
        )

        version.setAlignment(
            Qt.AlignCenter
        )

        card_layout.addWidget(
            version
        )

        self.about_text = QLabel(self.t("about_text"))

        self.about_text.setObjectName(
            "aboutText"
        )

        self.about_text.setWordWrap(
            True
        )

        self.about_text.setAlignment(
            Qt.AlignCenter
        )

        card_layout.addWidget(
            self.about_text
        )

        card_layout.addStretch()

        card.setLayout(
            card_layout
        )

        layout.addWidget(
            title
        )

        layout.addWidget(
            card
        )

        layout.addStretch()

        page.setLayout(
            layout
        )

        return page

    # =====================================================
    # NAVIGATION
    # =====================================================

    def activate_sidebar(
        self,
        active
    ):

        buttons = [
            self.home_button,
            self.downloads_button,
            self.playlist_button,
            self.settings_button,
            self.about_button
        ]

        for button in buttons:

            if button == active:

                button.setObjectName(
                    "sidebarActive"
                )

            else:

                button.setObjectName(
                    "sidebarButton"
                )

            button.style().unpolish(
                button
            )

            button.style().polish(
                button
            )

    def show_home(self):

        self.pages.setCurrentWidget(
            self.home_page
        )

        self.activate_sidebar(
            self.home_button
        )

    def show_downloads(self):

        self.pages.setCurrentWidget(
            self.downloads_page
        )

        self.activate_sidebar(
            self.downloads_button
        )

        self.refresh_downloads()

    def show_playlists(self):

        self.pages.setCurrentWidget(
            self.playlists_page
        )

        self.activate_sidebar(
            self.playlist_button
        )

        self.refresh_playlists()

    def show_settings(self):

        self.pages.setCurrentWidget(
            self.settings_page
        )

        self.activate_sidebar(
            self.settings_button
        )

    def show_about(self):

        self.pages.setCurrentWidget(
            self.about_page
        )

        self.activate_sidebar(
            self.about_button
        )

    # =====================================================
    # FOLDER
    # =====================================================

    def choose_folder(self):

        folder = QFileDialog.getExistingDirectory(
            self,
            self.t("İndirme klasörü seç"),
            self.folder_input.text()
        )

        if folder:

            final_folder = os.path.join(
                folder,
                "Fafatara Downloader"
            )

            os.makedirs(
                final_folder,
                exist_ok=True
            )

            self.settings[
                "download_folder"
            ] = final_folder

            self.folder_input.setText(
                final_folder
            )

            self.settings_folder.setText(
                final_folder
            )

            save_settings(
                self.settings
            )

    def choose_settings_folder(
        self
    ):

        folder = QFileDialog.getExistingDirectory(
            self,
            self.t("İndirme klasörü seç"),
            self.settings_folder.text()
        )

        if folder:

            final_folder = os.path.join(
                folder,
                "Fafatara Downloader"
            )

            os.makedirs(
                final_folder,
                exist_ok=True
            )

            self.settings_folder.setText(
                final_folder
            )

    # =====================================================
    # SETTINGS SAVE
    # =====================================================

    def save_app_settings(
        self
    ):

        self.settings[
            "download_folder"
        ] = self.settings_folder.text()

        self.settings["language"] = self.settings_language.currentData()

        self.settings[
            "format"
        ] = self.settings_format.currentText()

        self.settings[
            "quality"
        ] = self.settings_quality.currentText()

        self.settings[
            "audio_quality"
        ] = (
            self.settings_audio_quality
            .currentText()
            .replace(
                " kbps",
                ""
            )
        )

        os.makedirs(
            self.settings[
                "download_folder"
            ],
            exist_ok=True
        )

        save_settings(
            self.settings
        )

        self.folder_input.setText(
            self.settings[
                "download_folder"
            ]
        )

        self.format_combo.setCurrentText(
            self.settings[
                "format"
            ]
        )

        self.update_quality_options(
            self.settings[
                "format"
            ]
        )

        if self.settings[
            "format"
        ] == "MP3":

            self.quality_combo.setCurrentText(
                self.settings[
                    "audio_quality"
                ] + " kbps"
            )

        else:

            self.quality_combo.setCurrentText(
                self.settings[
                    "quality"
                ]
            )

        QMessageBox.information(
            self,
            APP_NAME,
            self.t("Ayarlar başarıyla kaydedildi.")
        )

    # =====================================================
    # ANALYZE
    # =====================================================

    def analyze_playlist(
        self
    ):

        url = self.url_input.text().strip()

        if not url:

            QMessageBox.warning(
                self,
                APP_NAME,
                self.t("Önce YouTube bağlantısını gir.")
            )

            return

        self.analyze_button.setEnabled(
            False
        )

        self.status_label.setText(
            self.t("Bağlantı analiz ediliyor...")
        )

        self.playlist_thread = PlaylistThread(
            url
        )

        self.playlist_thread.result.connect(
            self.playlist_loaded
        )

        self.playlist_thread.error.connect(
            self.playlist_error
        )

        self.playlist_thread.start()

    def playlist_loaded(
        self,
        info
    ):

        self.analyze_button.setEnabled(
            True
        )

        if not info.get(
            "is_playlist",
            False
        ):

            self.playlist_card.setVisible(
                False
            )

            self.status_label.setText(
                self.t("Video hazır.")
            )

            return

        self.playlist_card.setVisible(
            True
        )

        self.playlist_info.setText(
            f"📋  {info['title']}  •  "
            f"{info['count']} video"
        )

        self.playlist_list.clear()

        for entry in info[
            "entries"
        ]:

            item = QListWidgetItem(
                entry.get(
                    "title",
                    self.t("Bilinmeyen video")
                )
            )

            item.setCheckState(
                Qt.Checked
            )

            self.playlist_list.addItem(
                item
            )

        self.status_label.setText(
            f"{info['count']} {self.t('video hazır.')}"
        )

    def playlist_error(
        self,
        message
    ):

        self.analyze_button.setEnabled(
            True
        )

        self.status_label.setText(
            self.t("Analiz başarısız.")
        )

        QMessageBox.critical(
            self,
            APP_NAME,
            message
        )

    # =====================================================
    # SELECT ALL
    # =====================================================

    def toggle_all(
        self,
        state
    ):

        checked = (
            Qt.Checked
            if state == Qt.Checked
            else Qt.Unchecked
        )

        for i in range(
            self.playlist_list.count()
        ):

            self.playlist_list.item(
                i
            ).setCheckState(
                checked
            )

    # =====================================================
    # DOWNLOAD
    # =====================================================

    def start_download(
        self
    ):

        url = self.url_input.text().strip()

        if not url:

            QMessageBox.warning(
                self,
                APP_NAME,
                self.t("YouTube bağlantısı gir.")
            )

            return

        mode = (
            self.format_combo
            .currentText()
            .lower()
        )

        selected_quality = (
            self.quality_combo
            .currentText()
        )

        if mode == "mp3":

            audio_quality = (
                selected_quality
                .replace(
                    " kbps",
                    ""
                )
            )

            quality = "best"

        else:

            audio_quality = "320"

            quality = (
                selected_quality
                .replace(
                    "p",
                    ""
                )
            )

        output_dir = (
            self.folder_input
            .text()
            .strip()
        )

        self.settings[
            "format"
        ] = self.format_combo.currentText()

        if mode == "mp3":

            self.settings[
                "audio_quality"
            ] = audio_quality

        else:

            self.settings[
                "quality"
            ] = selected_quality

        self.settings[
            "download_folder"
        ] = output_dir

        save_settings(
            self.settings
        )

        self.download_button.setEnabled(
            False
        )

        self.analyze_button.setEnabled(
            False
        )

        self.progress_bar.setValue(
            0
        )

        self.percent_label.setText(
            "0%"
        )

        self.status_label.setText(
            self.t("İndirme başlıyor...")
        )

        self.file_label.setText(
            ""
        )

        self.download_thread = DownloadThread(
            url,
            mode,
            quality,
            audio_quality,
            output_dir
        )

        self.download_thread.progress.connect(
            self.update_progress
        )

        self.download_thread.finished_signal.connect(
            self.download_finished
        )

        self.download_thread.error.connect(
            self.download_error
        )

        self.download_thread.start()

    # =====================================================
    # PROGRESS
    # =====================================================

    def update_progress(
        self,
        data
    ):

        if data.get(
            "status"
        ) == "downloading":

            percent = data.get(
                "percent",
                "0%"
            )

            try:

                value = float(
                    str(
                        percent
                    )
                    .replace(
                        "%",
                        ""
                    )
                    .replace(
                        "~",
                        ""
                    )
                    .strip()
                )

                value = max(
                    0,
                    min(
                        100,
                        value
                    )
                )

                self.progress_bar.setValue(
                    int(value)
                )

                self.percent_label.setText(
                    f"{int(value)}%"
                )

            except Exception:

                pass

            speed = data.get(
                "speed",
                "0 B/s"
            )

            eta = data.get(
                "eta",
                "?"
            )

            self.status_label.setText(
                f"{self.t('İndiriliyor  •  ')}"
                f"{speed}  •  "
                f"Kalan: {eta}"
            )

            filename = data.get(
                "filename",
                ""
            )

            if filename:

                self.file_label.setText(
                    os.path.basename(
                        filename
                    )
                )

        elif data.get(
            "status"
        ) == "finished":

            self.progress_bar.setValue(
                100
            )

            self.percent_label.setText(
                "100%"
            )

            self.status_label.setText(
                self.t("Dosya işleniyor...")
            )

    # =====================================================
    # FINISHED
    # =====================================================

    def download_finished(
        self
    ):

        self.download_button.setEnabled(
            True
        )

        self.analyze_button.setEnabled(
            True
        )

        self.progress_bar.setValue(
            100
        )

        self.percent_label.setText(
            "100%"
        )

        self.status_label.setText(
            self.t("✓  İndirme tamamlandı")
        )

        self.refresh_downloads()

        self.refresh_playlists()

        QMessageBox.information(
            self,
            APP_NAME,
            self.t("İndirme başarıyla tamamlandı.")
        )

    # =====================================================
    # ERROR
    # =====================================================

    def download_error(
        self,
        message
    ):

        self.download_button.setEnabled(
            True
        )

        self.analyze_button.setEnabled(
            True
        )

        self.status_label.setText(
            self.t("✕  İndirme başarısız")
        )

        QMessageBox.critical(
            self,
            self.t("İndirme Hatası"),
            message
        )

    # =====================================================
    # DOWNLOAD HISTORY
    # =====================================================

    def refresh_downloads(
        self
    ):

        self.downloads_list.clear()

        folder = self.settings[
            "download_folder"
        ]

        if not os.path.exists(
            folder
        ):

            self.downloads_list.addItem(
                "Henüz indirilen dosya yok."
            )

            return

        files = []

        for root, dirs, filenames in os.walk(
            folder
        ):

            for filename in filenames:

                if filename.lower().endswith(
                    (
                        ".mp4",
                        ".mp3",
                        ".m4a",
                        ".webm",
                        ".mkv"
                    )
                ):

                    files.append(
                        os.path.join(
                            root,
                            filename
                        )
                    )

        files.sort(
            key=lambda x:
            os.path.getmtime(x),
            reverse=True
        )

        if not files:

            self.downloads_list.addItem(
                "Henüz indirilen dosya yok."
            )

            return

        for path in files:

            size = os.path.getsize(
                path
            )

            size_mb = size / (
                1024 * 1024
            )

            relative = os.path.relpath(
                path,
                folder
            )

            item = QListWidgetItem(
                f"📄  {relative}  •  "
                f"{size_mb:.1f} MB"
            )

            item.setToolTip(
                path
            )

            self.downloads_list.addItem(
                item
            )

    # =====================================================
    # PLAYLIST HISTORY
    # =====================================================

    def refresh_playlists(
        self
    ):

        self.playlists_list.clear()

        folder = self.settings[
            "download_folder"
        ]

        if not os.path.exists(
            folder
        ):

            self.playlists_list.addItem(
                "Henüz playlist indirilmedi."
            )

            return

        playlists = []

        for name in os.listdir(
            folder
        ):

            path = os.path.join(
                folder,
                name
            )

            if not os.path.isdir(
                path
            ):

                continue

            count = 0

            for root, dirs, files in os.walk(
                path
            ):

                for filename in files:

                    if filename.lower().endswith(
                        (
                            ".mp4",
                            ".mp3",
                            ".m4a",
                            ".webm",
                            ".mkv"
                        )
                    ):

                        count += 1

            if count:

                playlists.append(
                    (
                        name,
                        count,
                        path
                    )
                )

        playlists.sort(
            key=lambda x:
            os.path.getmtime(
                x[2]
            ),
            reverse=True
        )

        if not playlists:

            self.playlists_list.addItem(
                "Henüz playlist indirilmedi."
            )

            return

        for name, count, path in playlists:

            item = QListWidgetItem(
                f"📋  {name}  •  "
                f"{count} dosya"
            )

            item.setToolTip(
                path
            )

            self.playlists_list.addItem(
                item
            )

    # =====================================================
    # THEME
    # =====================================================

    def apply_theme(
        self
    ):

        self.setStyleSheet(
            """
            QWidget {
                background-color: #080c19;
                color: #f1f3ff;
                font-family: "Segoe UI";
                font-size: 14px;
            }

            QLabel {
                background: transparent;
                border: none;
            }

            QFrame#sidebar {
                background-color: #080d1d;
                border-right: 1px solid #1a2440;
            }

            QFrame#card {
                background-color: #0e1425;
                border: 1px solid #1b2745;
                border-radius: 13px;
            }

            QFrame#progressCard {
                background-color: #0d1427;
                border: 1px solid #293761;
                border-radius: 13px;
            }

            QFrame#aboutCard {
                background-color: #0e1425;
                border: 1px solid #1b2745;
                border-radius: 16px;
            }

            QLabel#logoTitle {
                color: white;
                font-size: 21px;
                font-weight: 800;
                letter-spacing: 2px;
            }

            QLabel#logoSubtitle {
                color: #b338ff;
                font-size: 10px;
                font-weight: 800;
                letter-spacing: 3px;
            }

            QLabel#version {
                color: #59627c;
                font-size: 11px;
            }

            QPushButton#sidebarButton,
            QPushButton#sidebarActive {
                text-align: left;
                border: none;
                border-radius: 10px;
                padding-left: 15px;
            }

            QPushButton#sidebarButton {
                background: transparent;
                color: #8993ad;
            }

            QPushButton#sidebarButton:hover {
                background: #141c34;
                color: white;
            }

            QPushButton#sidebarActive {
                background: qlineargradient(
                    x1: 0,
                    y1: 0,
                    x2: 1,
                    y2: 0,
                    stop: 0 #7131ff,
                    stop: 1 #b431ff
                );
                color: white;
                font-weight: 700;
            }

            QLabel#mainTitle {
                color: white;
                font-size: 29px;
                font-weight: 800;
            }

            QLabel#mainSubtitle,
            QLabel#pageSubtitle {
                color: #69748f;
                font-size: 13px;
            }

            QLabel#youtube {
                color: #ff3b65;
                font-size: 16px;
                font-weight: 700;
            }

            QLabel#smallTitle {
                color: #7181a4;
                font-size: 10px;
                font-weight: 800;
                letter-spacing: 1px;
            }

            QLabel#playlistTitle {
                color: white;
                font-size: 15px;
                font-weight: 700;
            }

            QLabel#statusTitle {
                color: #d9ddf2;
                font-weight: 700;
            }

            QLabel#percent {
                color: #bd48ff;
                font-size: 17px;
                font-weight: 800;
            }

            QLabel#fileLabel {
                color: #687590;
                font-size: 11px;
            }

            QLabel#footer {
                color: #59657f;
                font-size: 11px;
            }

            QLabel#pageTitle {
                color: white;
                font-size: 30px;
                font-weight: 800;
            }

            QLabel#settingTitle {
                color: white;
                font-size: 16px;
                font-weight: 700;
            }

            QLabel#settingDescription {
                color: #65718d;
                font-size: 12px;
            }

            QLabel#aboutTitle {
                color: white;
                font-size: 24px;
                font-weight: 800;
            }

            QLabel#aboutVersion {
                color: #9d45ff;
                font-size: 12px;
            }

            QLabel#aboutText {
                color: #8994ad;
                font-size: 14px;
                padding: 20px;
            }

            QLineEdit,
            QComboBox {
                background-color: #080e1d;
                border: 1px solid #273451;
                border-radius: 9px;
                padding: 7px 12px;
                color: #eef0ff;
                selection-background-color: #7136dd;
            }

            QLineEdit:focus,
            QComboBox:focus {
                border: 1px solid #9147ff;
            }

            QComboBox QAbstractItemView {
                background-color: #10172a;
                color: white;
                border: 1px solid #273451;
                selection-background-color: #7136dd;
            }

            QPushButton {
                background-color: #172039;
                color: white;
                border: 1px solid #283653;
                border-radius: 9px;
                padding: 8px 16px;
                font-weight: 600;
            }

            QPushButton:hover {
                background-color: #232e4c;
            }

            QPushButton:disabled {
                background-color: #121827;
                color: #4d5870;
            }

            QPushButton#analyzeButton {
                background: qlineargradient(
                    x1: 0,
                    y1: 0,
                    x2: 1,
                    y2: 0,
                    stop: 0 #7035ff,
                    stop: 1 #ad39ff
                );
                border: none;
            }

            QPushButton#downloadButton {
                background: qlineargradient(
                    x1: 0,
                    y1: 0,
                    x2: 1,
                    y2: 0,
                    stop: 0 #6731ff,
                    stop: 0.5 #9239ff,
                    stop: 1 #c43cff
                );
                border: none;
                color: white;
                font-size: 16px;
                font-weight: 800;
            }

            QPushButton#downloadButton:hover {
                background: #a53cff;
            }

            QListWidget {
                background-color: #090f1d;
                border: 1px solid #1c2844;
                border-radius: 10px;
                padding: 6px;
                color: #dce1f3;
            }

            QListWidget::item {
                background: transparent;
                padding: 10px;
                border-radius: 7px;
            }

            QListWidget::item:hover {
                background: #141d35;
            }

            QListWidget::item:selected {
                background: #1b2750;
            }

            QCheckBox {
                background: transparent;
                color: #aeb7cd;
            }

            QProgressBar {
                background-color: #171f35;
                border: none;
                border-radius: 7px;
                height: 14px;
            }

            QProgressBar::chunk {
                background: qlineargradient(
                    x1: 0,
                    y1: 0,
                    x2: 1,
                    y2: 0,
                    stop: 0 #7035ff,
                    stop: 0.5 #a73dff,
                    stop: 1 #d03bff
                );
                border-radius: 7px;
            }

            QScrollBar:vertical {
                background: #080d19;
                width: 8px;
            }

            QScrollBar::handle:vertical {
                background: #303b5b;
                border-radius: 4px;
                min-height: 30px;
            }
            """
        )


# =========================================================
# START
# =========================================================

if __name__ == "__main__":

    app = QApplication(
        sys.argv
    )

    app.setApplicationName(
        APP_NAME
    )

    app.setApplicationDisplayName(
        APP_NAME
    )

    if os.path.exists(
        LOGO_PATH
    ):

        app.setWindowIcon(
            QIcon(
                LOGO_PATH
            )
        )

    window = FafataraDownloader()

    window.show()

    sys.exit(
        app.exec()
    )