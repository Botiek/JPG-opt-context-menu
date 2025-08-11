@echo off
chcp 65001 >nul
title JPG Оптимизатор - Замена оригиналов

echo Установка зависимостей...
python -m pip install -r "%~dp0requirements.txt" --quiet

echo.
echo Запуск оптимизации JPG изображений...
echo ВНИМАНИЕ: Оригиналы будут заменены оптимизированными версиями!
echo.

REM Проверяем, передан ли аргумент
if "%~1"=="" (
    echo ОШИБКА: Не указан путь к папке или файлу!
    echo Использование: %~nx0 "путь_к_папке_или_файлу"
    echo.
    echo Окно закроется через 3 секунды...
    timeout /t 3 /nobreak >nul
    exit /b 1
)

python "%~dp0jpg_optimizer.py" "%~1" --delete-originals
