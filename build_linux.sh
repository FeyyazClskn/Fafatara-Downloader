#!/usr/bin/env bash

set -e

APP_NAME="Fafatara Downloader"

echo "=========================================="
echo "       FAFATARA DOWNLOADER"
echo "          LINUX BUILD"
echo "=========================================="
echo

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

rm -rf build
rm -rf dist

python3 -m PyInstaller \
    --noconfirm \
    --clean \
    --windowed \
    --onedir \
    --name "$APP_NAME" \
    --collect-all yt_dlp \
    --collect-all yt_dlp_ejs \
    main.py

echo
echo "=========================================="
echo "        BUILD TAMAMLANDI"
echo "=========================================="
echo
echo "Konum:"
echo "dist/Fafatara Downloader/"
echo