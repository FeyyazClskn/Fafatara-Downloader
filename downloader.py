import os
import re
import yt_dlp


class Downloader:

    def __init__(self, output_dir=None):

        self.output_dir = output_dir or os.path.join(
            os.path.expanduser("~"),
            "Downloads",
            "Fafatara Downloader"
        )

        os.makedirs(
            self.output_dir,
            exist_ok=True
        )

    # =====================================================
    # DOSYA ADI
    # =====================================================

    @staticmethod
    def clean_filename(name):

        name = re.sub(
            r'[<>:"/\\|?*]',
            '',
            name
        )

        name = name.strip()

        if not name:
            name = "Fafatara Download"

        return name

    # =====================================================
    # PROGRESS
    # =====================================================

    def _progress_hook(
        self,
        data,
        callback
    ):

        if callback is None:
            return

        status = data.get("status")

        filename = data.get(
            "filename",
            ""
        )

        if status == "downloading":

            callback({
                "status": "downloading",

                "percent": data.get(
                    "_percent_str",
                    "0%"
                ),

                "speed": data.get(
                    "_speed_str",
                    "0 B/s"
                ),

                "eta": data.get(
                    "_eta_str",
                    "?"
                ),

                "filename": filename
            })

        elif status == "finished":

            callback({
                "status": "finished",

                "percent": "100%",

                "speed": "",

                "eta": "0",

                "filename": filename
            })

    # =====================================================
    # ORTAK YT-DLP AYARLARI
    # =====================================================

    def _common_options(
        self,
        progress_callback=None
    ):

        return {

            # Konsola gereksiz çıktıları bastırma
            "quiet": True,

            "no_warnings": True,

            # Tekrar deneme
            "retries": 10,

            "fragment_retries": 10,

            # Parçalı indirmelerde paralellik
            "concurrent_fragment_downloads": 4,

            # Devam eden indirmeyi sürdür
            "continuedl": True,

            # Yarım dosyaları koru
            "nopart": False,

            # Dosya adları
            "windowsfilenames": True,

            "restrictfilenames": False,

            # Üzerine yazma
            "overwrites": False,

            # Deno
            "js_runtimes": {
                "deno": {}
            },

            # EJS
            "remote_components": {
                "ejs:github"
            },

            # Progress
            "progress_hooks": [
                lambda data:
                self._progress_hook(
                    data,
                    progress_callback
                )
            ]
        }

    # =====================================================
    # PLAYLIST ANALİZ
    # =====================================================

    def get_playlist_info(
        self,
        url
    ):

        options = {

            "quiet": True,

            "no_warnings": True,

            "extract_flat": True,

            "skip_download": True,

            "ignoreerrors": True,

            "noplaylist": False,

            "js_runtimes": {
                "deno": {}
            },

            "remote_components": {
                "ejs:github"
            }
        }

        with yt_dlp.YoutubeDL(
            options
        ) as ydl:

            info = ydl.extract_info(
                url,
                download=False
            )

        if not info:

            raise Exception(
                "YouTube bilgileri alınamadı."
            )

        is_playlist = (
            info.get("_type") == "playlist"
            or info.get("entries") is not None
        )

        # -------------------------------------------------
        # TEK VIDEO
        # -------------------------------------------------

        if not is_playlist:

            return {

                "is_playlist": False,

                "title": info.get(
                    "title",
                    "Video"
                ),

                "count": 1,

                "entries": [
                    {
                        "title": info.get(
                            "title",
                            "Video"
                        ),

                        "url": url
                    }
                ]
            }

        # -------------------------------------------------
        # PLAYLIST
        # -------------------------------------------------

        entries = []

        for entry in (
            info.get("entries") or []
        ):

            if not entry:
                continue

            title = entry.get(
                "title",
                "Bilinmeyen video"
            )

            entry_url = entry.get(
                "url"
            )

            if not entry_url:

                video_id = entry.get(
                    "id"
                )

                if video_id:

                    entry_url = (
                        "https://www.youtube.com/watch?v="
                        + video_id
                    )

            if entry_url:

                entries.append({
                    "title": title,
                    "url": entry_url
                })

        return {

            "is_playlist": True,

            "title": info.get(
                "title",
                "Playlist"
            ),

            "count": len(entries),

            "entries": entries
        }

    # =====================================================
    # ANA DOWNLOAD
    # =====================================================

    def download(
        self,
        url,
        mode,
        quality,
        progress_callback=None,
        audio_quality="320"
    ):

        if mode.lower() == "mp3":

            self.download_mp3(
                url,
                audio_quality,
                progress_callback
            )

        else:

            self.download_mp4(
                url,
                quality,
                progress_callback
            )

    # =====================================================
    # ÇIKTI KLASÖRÜ
    # =====================================================

    def _get_output_directory(
        self,
        url
    ):

        try:

            info = self.get_playlist_info(
                url
            )

        except Exception:

            info = {
                "is_playlist": False
            }

        if info.get(
            "is_playlist",
            False
        ):

            playlist_name = self.clean_filename(
                info.get(
                    "title",
                    "Playlist"
                )
            )

            output_dir = os.path.join(
                self.output_dir,
                playlist_name
            )

            os.makedirs(
                output_dir,
                exist_ok=True
            )

            return output_dir

        return self.output_dir

    # =====================================================
    # MP4
    # =====================================================

    def download_mp4(
        self,
        url,
        quality,
        progress_callback=None
    ):

        output_dir = self._get_output_directory(
            url
        )

        # -------------------------------------------------
        # KALİTE
        # -------------------------------------------------

        try:

            height = int(
                str(
                    quality
                ).replace(
                    "p",
                    ""
                )
            )

        except Exception:

            height = 1080

        # -------------------------------------------------
        # FORMAT 1
        #
        # Önce HTTPS DASH.
        # -------------------------------------------------

        format_https = (
            f"bestvideo[height<={height}]"
            "[protocol=https]+"
            "bestaudio[protocol=https]/"
            f"best[height<={height}]"
            "[protocol=https]"
        )

        # -------------------------------------------------
        # FORMAT 2
        #
        # HTTPS sorun çıkarırsa HLS.
        # YouTube'da test ettiğimiz 312 gibi
        # formatlar bu gruba giriyor.
        # -------------------------------------------------

        format_hls = (
            f"bestvideo[height<={height}]"
            "[protocol^=m3u8]+"
            "bestaudio/"
            f"best[height<={height}]"
            "[protocol^=m3u8]"
        )

        # -------------------------------------------------
        # FORMAT 3
        #
        # Son fallback.
        # -------------------------------------------------

        format_any = (
            f"bestvideo[height<={height}]"
            "+bestaudio/"
            f"best[height<={height}]"
        )

        # -------------------------------------------------
        # OPTIONS
        # -------------------------------------------------

        options = self._common_options(
            progress_callback
        )

        options.update({

            "format":
                format_https
                + "/"
                + format_hls
                + "/"
                + format_any,

            "merge_output_format":
                "mp4",

            "outtmpl":
                os.path.join(
                    output_dir,
                    "%(title)s.%(ext)s"
                ),

            "noplaylist":
                False,

            # Dosya adı başına playlist index EKLEME
            "outtmpl_na_placeholder":
                "",

            "postprocessors": []
        })

        # -------------------------------------------------
        # DOWNLOAD
        # -------------------------------------------------

        with yt_dlp.YoutubeDL(
            options
        ) as ydl:

            ydl.download([
                url
            ])

    # =====================================================
    # MP3
    # =====================================================

    def download_mp3(
        self,
        url,
        audio_quality="320",
        progress_callback=None
    ):

        output_dir = self._get_output_directory(
            url
        )

        # -------------------------------------------------
        # BITRATE
        # -------------------------------------------------

        try:

            audio_quality = int(
                str(
                    audio_quality
                )
                .replace(
                    " kbps",
                    ""
                )
            )

        except Exception:

            audio_quality = 320

        allowed = [
            320,
            256,
            192,
            128,
            96
        ]

        if audio_quality not in allowed:

            audio_quality = 320

        # -------------------------------------------------
        # OPTIONS
        # -------------------------------------------------

        options = self._common_options(
            progress_callback
        )

        options.update({

            # Önce HTTPS audio
            "format":
                "bestaudio[protocol=https]/"
                "bestaudio/",

            "outtmpl":
                os.path.join(
                    output_dir,
                    "%(title)s.%(ext)s"
                ),

            "noplaylist":
                False,

            "postprocessors": [

                {
                    "key":
                        "FFmpegExtractAudio",

                    "preferredcodec":
                        "mp3",

                    "preferredquality":
                        str(
                            audio_quality
                        )
                },

                {
                    "key":
                        "FFmpegMetadata"
                }
            ]
        })

        with yt_dlp.YoutubeDL(
            options
        ) as ydl:

            ydl.download([
                url
            ])

    # =====================================================
    # İNDİRİLEN DOSYALAR
    # =====================================================

    def get_downloaded_files(
        self
    ):

        files = []

        if not os.path.exists(
            self.output_dir
        ):

            return files

        for root, dirs, filenames in os.walk(
            self.output_dir
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

        return files

    # =====================================================
    # PLAYLISTLER
    # =====================================================

    def get_downloaded_playlists(
        self
    ):

        playlists = []

        if not os.path.exists(
            self.output_dir
        ):

            return playlists

        for name in os.listdir(
            self.output_dir
        ):

            path = os.path.join(
                self.output_dir,
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

            if count > 0:

                playlists.append({

                    "name":
                        name,

                    "count":
                        count,

                    "path":
                        path
                })

        return playlists