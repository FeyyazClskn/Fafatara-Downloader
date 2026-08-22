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

DEFAULT_SETTINGS = {
    "download_folder": "",
    "format": "MP4",
    "quality": "1080p",
    "audio_quality": "320"
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

        self.apply_theme()

        self.show_home()

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

        footer = QLabel(
            "🦋 Fafatara Downloader  •  Made with ❤️ by Feyyaz"
        )

        footer.setObjectName(
            "footer"
        )

        footer.setAlignment(
            Qt.AlignCenter
        )

        layout.addWidget(
            footer
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

        text = QLabel(
            "Fafatara Downloader, internet üzerindeki "
            "video ve müzik indirme deneyimini daha sade, "
            "temiz ve kullanışlı hale getirmek amacıyla "
            "geliştirilmiştir."
            "\n\n"
            "İnternette kullanıcıları gereksiz reklamlar, "
            "açılır pencereler ve şüpheli indirme butonlarıyla "
            "karşı karşıya bırakan birçok indirme sitesi "
            "bulunmaktadır."
            "\n\n"
            "Fafatara Downloader bu karmaşık deneyime "
            "karşı sade bir masaüstü alternatif sunmayı "
            "amaçlar."
            "\n\n"
            "Uygulama MP4, MP3, yüksek kaliteli video, "
            "ses kalitesi ve playlist indirme özelliklerini "
            "tek bir arayüzde bir araya getirir."
            "\n\n"
            "Fafatara Downloader bağımsız olarak "
            "geliştirilmektedir."
        )

        text.setObjectName(
            "aboutText"
        )

        text.setWordWrap(
            True
        )

        text.setAlignment(
            Qt.AlignCenter
        )

        card_layout.addWidget(
            text
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
            "İndirme klasörü seç",
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
            "İndirme klasörü seç",
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
            "Ayarlar başarıyla kaydedildi."
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
                "Önce YouTube bağlantısını gir."
            )

            return

        self.analyze_button.setEnabled(
            False
        )

        self.status_label.setText(
            "Bağlantı analiz ediliyor..."
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
                "Video hazır."
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
                    "Bilinmeyen video"
                )
            )

            item.setCheckState(
                Qt.Checked
            )

            self.playlist_list.addItem(
                item
            )

        self.status_label.setText(
            f"{info['count']} video hazır."
        )

    def playlist_error(
        self,
        message
    ):

        self.analyze_button.setEnabled(
            True
        )

        self.status_label.setText(
            "Analiz başarısız."
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
                "YouTube bağlantısı gir."
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
            "İndirme başlıyor..."
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
                f"İndiriliyor  •  "
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
                "Dosya işleniyor..."
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
            "✓  İndirme tamamlandı"
        )

        self.refresh_downloads()

        self.refresh_playlists()

        QMessageBox.information(
            self,
            APP_NAME,
            "İndirme başarıyla tamamlandı."
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
            "✕  İndirme başarısız"
        )

        QMessageBox.critical(
            self,
            "İndirme Hatası",
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