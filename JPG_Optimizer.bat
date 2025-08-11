@echo off
chcp 65001 >nul
title JPG Оптимизатор

echo ========================================
echo         JPG Оптимизатор
echo ========================================
echo.
echo ПРОСТОЕ ИСПОЛЬЗОВАНИЕ:
echo 1. Перетащите папку с JPG изображениями на этот файл
echo 2. Или запустите файл и введите путь к папке
echo.
echo Выберите режим оптимизации:
echo.
echo 1. Сохранить оригиналы (создать _optimized файлы)
echo 2. Заменить оригиналы (удалить оригиналы)
echo.
set /p CHOICE="Введите номер (1 или 2): "

if "%CHOICE%"=="1" (
    echo.
    echo Режим: Сохранение оригиналов
    echo.
    if "%~1"=="" (
        set /p FOLDER="Введите путь к папке: "
    ) else (
        set "FOLDER=%~1"
    )
    
    if exist "!FOLDER!" (
        echo Обрабатываю папку: !FOLDER!
        call "%~dp0optimize_jpg_keep_originals.bat" "!FOLDER!"
    ) else (
        echo ОШИБКА: Папка не найдена!
        echo Проверьте правильность пути.
        echo.
        echo Окно закроется через 3 секунды...
        timeout /t 3 /nobreak >nul
        exit /b 1
    )
) else if "%CHOICE%"=="2" (
    echo.
    echo РЕЖИМ: ЗАМЕНА ОРИГИНАЛОВ
    echo ВНИМАНИЕ: Оригиналы будут удалены!
    echo.
    set /p CONFIRM="Вы уверены? Введите 'YES' для подтверждения: "
    
    if /i "!CONFIRM!"=="YES" (
        if "%~1"=="" (
            set /p FOLDER="Введите путь к папке: "
        ) else (
            set "FOLDER=%~1"
        )
        
        if exist "!FOLDER!" (
            echo Обрабатываю папку: !FOLDER!
            call "%~dp0optimize_jpg_replace_originals.bat" "!FOLDER!"
        ) else (
            echo ОШИБКА: Папка не найдена!
            echo Проверьте правильность пути.
            echo.
            echo Окно закроется через 3 секунды...
            timeout /t 3 /nobreak >nul
            exit /b 1
        )
    ) else (
        echo Операция отменена.
        echo.
        echo Окно закроется через 3 секунды...
        timeout /t 3 /nobreak >nul
        exit /b 0
    )
) else (
    echo Неверный выбор!
    echo.
    echo Окно закроется через 3 секунды...
    timeout /t 3 /nobreak >nul
    exit /b 1
)

echo.
echo Оптимизация завершена!
