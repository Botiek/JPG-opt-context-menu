@echo off
chcp 65001 >nul
title Создание ярлыков JPG Оптимизатора

echo ========================================
echo    Создание ярлыков на рабочем столе
echo ========================================
echo.
echo Этот скрипт создаст ярлыки для оптимизации JPG
echo на рабочем столе и в панели быстрого запуска.
echo.

set "DESKTOP=%USERPROFILE%\Desktop"
set "SCRIPT_DIR=%~dp0"

echo Создание ярлыков...

REM Создаем ярлык "Оптимизировать JPG (сохранить оригиналы)"
echo @echo off > "%DESKTOP%\JPG Оптимизатор - Сохранить оригиналы.bat"
echo cd /d "%SCRIPT_DIR%" >> "%DESKTOP%\JPG Оптимизатор - Сохранить оригиналы.bat"
echo echo Выберите папку с JPG изображениями... >> "%DESKTOP%\JPG Оптимизатор - Сохранить оригиналы.bat"
echo set /p FOLDER="Введите путь к папке: " >> "%DESKTOP%\JPG Оптимизатор - Сохранить оригиналы.bat"
echo if exist "%%FOLDER%%" ( >> "%DESKTOP%\JPG Оптимизатор - Сохранить оригиналы.bat"
echo   call "optimize_jpg_keep_originals.bat" "%%FOLDER%%" >> "%DESKTOP%\JPG Оптимизатор - Сохранить оригиналы.bat"
echo ) else ( >> "%DESKTOP%\JPG Оптимизатор - Сохранить оригиналы.bat"
echo   echo Папка не найдена! >> "%DESKTOP%\JPG Оптимизатор - Сохранить оригиналы.bat"
echo   pause >> "%DESKTOP%\JPG Оптимизатор - Сохранить оригиналы.bat"
echo ) >> "%DESKTOP%\JPG Оптимизатор - Сохранить оригиналы.bat"

REM Создаем ярлык "Оптимизировать JPG (заменить оригиналы)"
echo @echo off > "%DESKTOP%\JPG Оптимизатор - Заменить оригиналы.bat"
echo cd /d "%SCRIPT_DIR%" >> "%DESKTOP%\JPG Оптимизатор - Заменить оригиналы.bat"
echo echo ВНИМАНИЕ: Оригиналы будут заменены! >> "%DESKTOP%\JPG Оптимизатор - Заменить оригиналы.bat"
echo echo Выберите папку с JPG изображениями... >> "%DESKTOP%\JPG Оптимизатор - Заменить оригиналы.bat"
echo set /p FOLDER="Введите путь к папке: " >> "%DESKTOP%\JPG Оптимизатор - Заменить оригиналы.bat"
echo if exist "%%FOLDER%%" ( >> "%DESKTOP%\JPG Оптимизатор - Заменить оригиналы.bat"
echo   call "optimize_jpg_replace_originals.bat" "%%FOLDER%%" >> "%DESKTOP%\JPG Оптимизатор - Заменить оригиналы.bat"
echo ) else ( >> "%DESKTOP%\JPG Оптимизатор - Заменить оригиналы.bat"
echo   echo Папка не найдена! >> "%DESKTOP%\JPG Оптимизатор - Заменить оригиналы.bat"
echo   pause >> "%DESKTOP%\JPG Оптимизатор - Заменить оригиналы.bat"
echo ) >> "%DESKTOP%\JPG Оптимизатор - Заменить оригиналы.bat"

echo.
echo ========================================
echo    Ярлыки созданы успешно!
echo ========================================
echo.
echo На рабочем столе появились:
echo  - "JPG Оптимизатор - Сохранить оригиналы.bat"
echo  - "JPG Оптимизатор - Заменить оригиналы.bat"
echo.
echo Как использовать:
echo 1. Двойной клик на нужный ярлык
echo 2. Введите путь к папке с JPG изображениями
echo 3. Нажмите Enter
echo 4. Дождитесь завершения оптимизации
echo.

echo Нажмите любую клавишу для выхода...
pause >nul
