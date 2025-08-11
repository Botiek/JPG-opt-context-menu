#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для оптимизации JPG изображений без потерь качества
Использует библиотеку Pillow для сжатия изображений
"""

import os
import sys
import time
from PIL import Image
import argparse
from pathlib import Path

def optimize_jpg(input_path, output_path, quality=85):
    """
    Оптимизирует JPG изображение без потерь качества
    
    Args:
        input_path (str): Путь к исходному изображению
        output_path (str): Путь для сохранения оптимизированного изображения
        quality (int): Качество сжатия (1-100)
    """
    try:
        with Image.open(input_path) as img:
            # Конвертируем в RGB если изображение в другом режиме
            if img.mode in ('RGBA', 'LA', 'P'):
                # Создаем белый фон для прозрачных изображений
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Сохраняем с оптимизацией
            img.save(output_path, 'JPEG', quality=quality, optimize=True, progressive=True)
            
        return True
    except Exception as e:
        print(f"Ошибка при оптимизации {input_path}: {e}")
        return False

def get_file_size(file_path):
    """Возвращает размер файла в байтах"""
    return os.path.getsize(file_path)

def format_file_size(size_bytes):
    """Форматирует размер файла в читаемом виде"""
    if size_bytes == 0:
        return "0B"
    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    return f"{size_bytes:.1f}{size_names[i]}"

def optimize_images_in_folder(folder_path, delete_originals=False, quality=85):
    """
    Оптимизирует все JPG изображения в папке
    
    Args:
        folder_path (str): Путь к папке с изображениями
        delete_originals (bool): Удалять ли оригиналы после оптимизации
        quality (int): Качество сжатия
    """
    folder_path = Path(folder_path)
    jpg_files = list(folder_path.glob("*.jpg")) + list(folder_path.glob("*.jpeg"))
    
    if not jpg_files:
        print("JPG изображения не найдены в указанной папке.")
        return
    
    print(f"Найдено {len(jpg_files)} JPG изображений для оптимизации...")
    print(f"Качество сжатия: {quality}%")
    print("-" * 50)
    
    total_original_size = 0
    total_optimized_size = 0
    success_count = 0
    
    for jpg_file in jpg_files:
        original_size = get_file_size(jpg_file)
        total_original_size += original_size
        
        # Создаем имя для оптимизированного файла
        if delete_originals:
            # Временно сохраняем с другим именем
            temp_name = jpg_file.with_suffix('.tmp')
            output_path = temp_name
        else:
            # Добавляем суффикс _optimized
            output_path = jpg_file.with_stem(jpg_file.stem + '_optimized')
        
        print(f"Обрабатываю: {jpg_file.name}")
        
        if optimize_jpg(str(jpg_file), str(output_path), quality):
            optimized_size = get_file_size(output_path)
            total_optimized_size += optimized_size
            success_count += 1
            
            # Показываем статистику
            savings = original_size - optimized_size
            savings_percent = (savings / original_size) * 100 if original_size > 0 else 0
            
            print(f"  Размер: {format_file_size(original_size)} → {format_file_size(optimized_size)}")
            print(f"  Экономия: {format_file_size(savings)} ({savings_percent:.1f}%)")
            
            if delete_originals:
                # Заменяем оригинал оптимизированным файлом
                jpg_file.unlink()
                output_path.rename(jpg_file)
                print(f"  Оригинал заменен оптимизированной версией")
            else:
                print(f"  Сохранено как: {output_path.name}")
        else:
            print(f"  ОШИБКА: Не удалось оптимизировать")
        
        print()
    
    # Итоговая статистика
    print("=" * 50)
    print("ИТОГИ ОПТИМИЗАЦИИ:")
    print(f"Успешно обработано: {success_count}/{len(jpg_files)}")
    
    if success_count > 0:
        total_savings = total_original_size - total_optimized_size
        total_savings_percent = (total_savings / total_original_size) * 100 if total_original_size > 0 else 0
        
        print(f"Общий размер: {format_file_size(total_original_size)} → {format_file_size(total_optimized_size)}")
        print(f"Общая экономия: {format_file_size(total_savings)} ({total_savings_percent:.1f}%)")
    
    if delete_originals:
        print("Оригинальные файлы удалены")
    else:
        print("Оригинальные файлы сохранены")

def main():
    parser = argparse.ArgumentParser(description='Оптимизация JPG изображений без потерь качества')
    parser.add_argument('path', help='Путь к папке с изображениями или к отдельному JPG файлу')
    parser.add_argument('--delete-originals', action='store_true', 
                       help='Удалить оригиналы после оптимизации')
    parser.add_argument('--quality', type=int, default=85, choices=range(1, 101),
                       help='Качество сжатия (1-100, по умолчанию 85)')
    
    args = parser.parse_args()
    
    print("JPG Оптимизатор")
    print("=" * 50)
    
    path = Path(args.path)
    
    if path.is_file() and path.suffix.lower() in ['.jpg', '.jpeg']:
        # Обрабатываем отдельный JPG файл
        print(f"Обрабатываю отдельный файл: {path.name}")
        print("-" * 50)
        
        original_size = get_file_size(path)
        
        # Создаем имя для оптимизированного файла
        if args.delete_originals:
            # Временно сохраняем с другим именем
            temp_name = path.with_suffix('.tmp')
            output_path = temp_name
        else:
            # Добавляем суффикс _optimized
            output_path = path.with_stem(path.stem + '_optimized')
        
        if optimize_jpg(str(path), str(output_path), args.quality):
            optimized_size = get_file_size(output_path)
            savings = original_size - optimized_size
            savings_percent = (savings / original_size) * 100 if original_size > 0 else 0
            
            print(f"Размер: {format_file_size(original_size)} → {format_file_size(optimized_size)}")
            print(f"Экономия: {format_file_size(savings)} ({savings_percent:.1f}%)")
            
            if args.delete_originals:
                # Заменяем оригинал оптимизированным файлом
                path.unlink()
                output_path.rename(path)
                print(f"Оригинал заменен оптимизированной версией")
            else:
                print(f"Сохранено как: {output_path.name}")
        else:
            print(f"ОШИБКА: Не удалось оптимизировать файл")
            sys.exit(1)
            
    elif path.is_dir():
        # Обрабатываем папку
        optimize_images_in_folder(args.path, args.delete_originals, args.quality)
    else:
        print(f"Ошибка: '{args.path}' не является папкой или JPG файлом")
        sys.exit(1)
    
    print("\nОптимизация завершена!")
    print("Окно закроется через 3 секунды...")
    time.sleep(3)

if __name__ == "__main__":
    main()
