@echo off

title Fafatara Downloader - Windows Build

echo ==========================================
echo       FAFATARA DOWNLOADER
echo          WINDOWS BUILD
echo ==========================================
echo.

call .venv\Scripts\activate

if errorlevel 1 (
    echo [HATA] .venv bulunamadi.
    pause
    exit /b 1
)

echo [1/4] Python paketleri kontrol ediliyor...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo [HATA] Python paketleri yuklenemedi.
    pause
    exit /b 1
)

echo.
echo [2/4] Eski build temizleniyor...

rmdir /s /q build 2>nul
rmdir /s /q dist 2>nul
del /q "Fafatara Downloader.spec" 2>nul

echo.
echo [3/4] Fafatara Downloader olusturuluyor...

python -m PyInstaller ^
    --noconfirm ^
    --clean ^
    --windowed ^
    --onedir ^
    --name "Fafatara Downloader" ^
    --icon "assets\logo.ico" ^
    --collect-all yt_dlp ^
    --collect-all yt_dlp_ejs ^
    main.py

if errorlevel 1 (
    echo.
    echo [HATA] Build basarisiz oldu.
    pause
    exit /b 1
)

echo.
echo [4/4] Build tamamlandi.
echo.

echo ==========================================
echo        FAFATARA DOWNLOADER HAZIR
echo ==========================================
echo.
echo Konum:
echo dist\Fafatara Downloader\
echo.
echo Uygulama:
echo dist\Fafatara Downloader\Fafatara Downloader.exe
echo.

pause