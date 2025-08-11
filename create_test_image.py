#!/usr/bin/env python3
"""
Скрипт для создания тестового JPG изображения
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_test_image():
    # Создаем изображение 800x600 с градиентом
    width, height = 800, 600
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Рисуем градиент
    for y in range(height):
        r = int(255 * y / height)
        g = int(128 + 127 * y / height)
        b = int(255 * (1 - y / height))
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Добавляем текст
    try:
        # Пытаемся использовать системный шрифт
        font = ImageFont.truetype("arial.ttf", 48)
    except:
        # Если не получилось, используем стандартный
        font = ImageFont.load_default()
    
    text = "Test JPG Image"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Рисуем текст с обводкой
    draw.text((x+2, y+2), text, fill='black', font=font)
    draw.text((x, y), text, fill='white', font=font)
    
    # Сохраняем в test_images
    if not os.path.exists('test_images'):
        os.makedirs('test_images')
    
    output_path = 'test_images/test_image.jpg'
    img.save(output_path, 'JPEG', quality=95)
    print(f"Тестовое изображение создано: {output_path}")
    print(f"Размер файла: {os.path.getsize(output_path)} байт")
    
    return output_path

if __name__ == "__main__":
    create_test_image()
